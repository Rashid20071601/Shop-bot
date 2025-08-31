"""
URL configuration for admin_panel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog import views as catalog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog_views.admin_dashboard, name='admin_dashboard'),
    path('products/', catalog_views.product_list, name='product_list'),
    path('products/add/', catalog_views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', catalog_views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', catalog_views.delete_product, name='delete_product'),
    path('categories/', catalog_views.category_list, name='category_list'),
    path('categories/add/', catalog_views.add_category, name='add_category'),
    path('categories/edit/<int:category_id>/', catalog_views.edit_category, name='edit_category'),
    path('categories/delete/<int:category_id>/', catalog_views.delete_category, name='delete_category'),
    path('users/', catalog_views.user_list, name='user_list'),
    path('user/delete/<int:user_id>/', catalog_views.delete_user, name='delete_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)