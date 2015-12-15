from django.contrib import admin

from .models import *

class BlogAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # prepopulate owner field with currently logged-in user
        if db_field.name == "owner":
            "set the current user as a default value for drop down"
            kwargs["initial"] = request.user.id 
        return super(BlogAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
     
class ImageInline(admin.StackedInline):
    # to support uploading images in-line during creation of post
    model = Image

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

	
admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

