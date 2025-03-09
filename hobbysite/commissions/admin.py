from django.contrib import admin

from .models import Commission, Comment

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    
    search_fields = ('title', 'description')
    list_display = ('title', 'description', 'created_on', 'updated_on')
    
class CommentAdmin(admin.ModelAdmin):
    model = Comment

    list_display = ('commission', 'entry', 'created_on')

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
