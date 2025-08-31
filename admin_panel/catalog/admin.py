from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)


admin.site.site_header = 'Панель администратора'
admin.site.site_title = 'Управление магазином'