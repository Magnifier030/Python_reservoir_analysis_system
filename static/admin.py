from django.contrib import admin
from static.models import Water_data, User_data
# Register your models here.
@admin.register(Water_data)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('Reservoir_id','Reservoir_name', 'WaterLevel', 'EffectiveWaterStorageCapacity')

@admin.register(User_data)
class user(admin.ModelAdmin):
    list_display = ('user_name', 'password', 'name', 'city', 'region')