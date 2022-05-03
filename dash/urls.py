from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from dash.core.views import (
    homeviews
)

router = DefaultRouter()

#router.register(r'nome_rota', view.funcao, basename='name')

urlpatterns = [
    path('', homeviews.index, name="index"),
    path('api/', include(router.urls)),
]
