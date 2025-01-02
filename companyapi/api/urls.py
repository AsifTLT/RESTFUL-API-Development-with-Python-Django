from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
admin.site.site_header = "COMPANY & EMPLOYEE API"
admin.site.site_title = "Company And Employee API"
admin.site.site_index_title = " Company And Employee API"
