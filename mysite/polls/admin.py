from django.contrib import admin
from .models import Question,Choice


# Register your models here.
class ChoiceInline(admin.StackedInline):
	model = Choice
class BlogAdmin(admin.ModelAdmin):
	inlines = [ChoiceInline]

admin.site.register(Question,BlogAdmin)
