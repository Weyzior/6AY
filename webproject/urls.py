from django.contrib import admin
from django.urls import include, path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("output_format1/<str:name>/", views.output_format1, name="output_format1"),
    path("output_format2/<str:name>/", views.output_format2, name="output_format2"),
    path("template_view/<str:name>/", views.template_view, name="template_view"),
    path("contact/", views.contact, name="contact"),
]
