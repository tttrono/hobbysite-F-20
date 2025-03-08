from django.contrib import admin

from .models import Commission, Comment

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    
    search_fields = ('title', 'description')
    list_display = ('title',)
    
class CommentAdmin(admin.ModelAdmin):
    model = Comment

    list_display = ('entry',)

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
