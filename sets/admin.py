from django.contrib import admin
from .models import Set, Flashcard


class FlashcardInline(admin.TabularInline):
    model = Flashcard


class SetAdmin(admin.ModelAdmin):
    inlines = [
        FlashcardInline,
    ]


admin.site.register(Set, SetAdmin)
admin.site.register(Flashcard)
