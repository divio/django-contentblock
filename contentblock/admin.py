from django.contrib import admin
from contentblock.models import ContentBlock
from multilingual.admin import MultilingualModelAdmin, MultilingualInlineAdmin
from cms.admin.placeholderadmin import PlaceholderAdmin

class ContentBlockAdmin(MultilingualModelAdmin, PlaceholderAdmin):
    list_display = ('code','name',)
admin.site.register(ContentBlock, ContentBlockAdmin)