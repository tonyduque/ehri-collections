"""
Admin config for suggestions.
"""
from django.contrib import admin
from suggestions.models import Suggestion, SuggestionType

admin.site.register(Suggestion)
admin.site.register(SuggestionType)


