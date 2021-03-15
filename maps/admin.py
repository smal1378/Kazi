from django.contrib import admin

# Register your models here.
from .models import Map, Part, Col, Row, Watered

admin.site.register(Map)
admin.site.register(Part)
admin.site.register(Col)
admin.site.register(Row)
admin.site.register(Watered)
