from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from . import views

urlpatterns = [
    path("csrf/", views.set_csrf_token, name="csrf"),
    path("", include("authentication.urls")),
    path("", include("core.urls", namespace="core")),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
