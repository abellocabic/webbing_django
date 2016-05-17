from django.contrib import admin
from .models import Post, Comment

#Custom Admin

class PostModelAdmin(admin.ModelAdmin):

	list_display = ["title","category", "timestamp"]
	list_filter = ["title", "timestamp"]
	search_fields = ["title", 'content']

	class Meta:
		model = Post


# Register your models here.
admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment)
