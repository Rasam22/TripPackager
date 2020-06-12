from django.contrib import admin
from .models import WH
from .models import seasons
from .models import fixedItems
from .models import seasonalItems
# # Register your models here.
admin.site.register(WH)
admin.site.register(seasons)
admin.site.register(fixedItems)
admin.site.register(seasonalItems)
