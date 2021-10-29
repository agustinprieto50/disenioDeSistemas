from django.contrib import admin
from django.urls import path
from .views import MutantViewSet

urlpatterns = [

    path('products', MutantViewSet.as_view({
        'post': 'is_mutant'
    }))


]