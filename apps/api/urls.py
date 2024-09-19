from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from . import views

urlpatterns = [
    path("csrf/", views.set_csrf_token, name="csrf"),
    path("export/", views.export_to_excel, name='export_to_excel'),
    path("", include("authentication.urls")),
    path("", include("core.urls", namespace="core")),
    path("", include("novel_food.urls", namespace="novel_food")),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
