from django.contrib import admin
from .models import Post

#Custom Admin

class PostModelAdmin(admin.ModelAdmin):

	list_display = ["title", "timestamp"]
	list_filter = ["title", "timestamp"]
	search_fields = ["title", 'content']

	class Meta:
		model = Post


# Register your models here.
admin.site.register(Post, PostModelAdmin)
