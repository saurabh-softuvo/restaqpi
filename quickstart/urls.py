
from django.contrib import admin
from django.urls import path
from quickstart1.views import employeeListView,userListView,employeeDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee', employeeListView),
    path('api/employees/<int:pk>', employeeDetailView),
    path('api/user', userListView),
]
