from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from dash.core.views import (
    homeviews,
    vulnerability_report
)

router = DefaultRouter()

router.register(r'vulnerability_report', vulnerability_report.ReportViewSet, basename='vulnerability_report')

urlpatterns = [
    path('', homeviews.index, name="index"),
    path('api/', include(router.urls)),
]
