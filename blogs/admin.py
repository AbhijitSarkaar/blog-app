from django.contrib import admin
from .models import Category, Blog, About, SocialLink, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

    list_display = ('title', 'category', 'author', 'is_featured', 'created_at', 'status')

    search_fields = ('id', 'category__category_name', 'status')

    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(About)
admin.site.register(SocialLink)
admin.site.register(Comment)
