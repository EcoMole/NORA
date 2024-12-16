from django.apps import apps
from django.conf import settings
from django.db.models import Case, CharField, F, Q, When
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class UserView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # get_queryset() would expect URL keyword argument named `pk` to
        # create queryset and thereby identify the object, but thanks to JWT I already have
        # user in the request so I can perform self.request.user

        # `self.request.user` doesn't merely contain user data from the request itself,
        # it actually does several steps under the hood: extracting the user's ID from JWT,
        # then retrieving the corresponding user record from the database similar to
        # performing User.objects.get(id=user_id)), attaching this data to request object so
        # the self.request.user refers to this user object freshly retreived from database.
        return self.request.user


class SettingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response = {}
        if self.request.user.is_staff or self.request.user.is_superuser:
            response["django_admin_path"] = settings.DJANGO_ADMIN_PATH
        return Response(response)


@api_view(["GET"])
def get_picklist(request):
    def get_choices_from_field(app_name, model_name, field_name):
        if not app_name or not model_name or not field_name:
            return None
        Model = apps.get_model(app_label=app_name, model_name=model_name)
        if not Model:
            raise ValueError(
                f"Model '{model_name}' in app '{app_name}' does not exist."
            )
        field = Model._meta.get_field(field_name)
        if hasattr(field, "choices"):
            return field.choices
        return None

    def get_limit_choices_to(app_name, model_name, field_name):
        if not app_name or not model_name or not field_name:
            return None
        Model = apps.get_model(app_label=app_name, model_name=model_name)
        if not Model:
            raise ValueError(
                f"Model '{model_name}' in app '{app_name}' does not exist."
            )
        field = Model._meta.get_field(field_name)

        limit_choices_to = None
        if (
            hasattr(field, "remote_field")
            and field.remote_field
            and hasattr(field.remote_field, "limit_choices_to")
        ):
            limit_choices_to = field.remote_field.limit_choices_to
        elif hasattr(field, "limit_choices_to"):
            limit_choices_to = field.limit_choices_to
        return limit_choices_to

    # Extract parameters
    django_app = request.query_params.get("djangoApp")
    django_model = request.query_params.get("djangoModel")
    django_field = request.query_params.get("djangoField")
    limitchoices_app = request.query_params.get("djangoLimitchoicesApp", None)
    limitchoices_model = request.query_params.get("djangoLimitchoicesModel", None)
    limitchoices_field = request.query_params.get("djangoLimitchoicesField", None)

    try:
        model = apps.get_model(django_app, django_model)
    except LookupError:
        return Response({"error": f"Model {django_model} not found."}, status=400)

    if not hasattr(model, django_field):
        return Response(
            {"error": f"Field {django_field} not found on model {django_model}."},
            status=400,
        )

    # for choice fields
    if choices := get_choices_from_field(django_app, django_model, django_field):
        res = [pair[0] for pair in choices]
        return Response(res)

    if limit_choices := get_limit_choices_to(
        limitchoices_app, limitchoices_model, limitchoices_field
    ):
        qs = model.objects.filter(limit_choices)
    else:
        qs = model.objects.all()

    # for taxonomy node fields
    if django_field == "short_name" and hasattr(model, "extended_name"):
        distinct_values = (
            qs.annotate(
                name=Case(
                    When(
                        Q(short_name__isnull=True) | Q(short_name__exact=""),
                        then=F("extended_name"),
                    ),
                    default=F("short_name"),
                    output_field=CharField(),
                )
            )
            .values_list("name", flat=True)
            .distinct()
        )
    else:
        # for other fields
        distinct_values = qs.order_by().values_list(django_field, flat=True).distinct()

    return Response(distinct_values)
