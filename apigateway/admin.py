from django.contrib import admin

# Register your models here.
from apigateway.models import Api, Consumer

admin.site.register(Api)
admin.site.register(Consumer)