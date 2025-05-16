from django.contrib import admin

from .models import Commission

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    
    list_display = ('title', 'description', 'created_on', 'updated_on')
    search_fields = ('title', 'description')

admin.site.register(Commission, CommissionAdmin)
