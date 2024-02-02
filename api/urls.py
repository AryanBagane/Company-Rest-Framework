from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token'),

]
