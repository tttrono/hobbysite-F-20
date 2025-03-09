from django.contrib import admin

from .models import Commission, Comment

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    
    list_display = ('title', 'description', 'created_on', 'updated_on')
    search_fields = ('title', 'description')
    
class CommentAdmin(admin.ModelAdmin):
    model = Comment

    list_display = ('commission', 'entry', 'created_on', 'updated_on')

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
