from django.contrib import admin
from .models import *


# Register your models here.
class KeyInline(admin.TabularInline):
    model = Key
    extra = 5


class PredicateInline(admin.TabularInline):
    model = Predicate
    extra = 5


class ObjectInline(admin.TabularInline):
    model = Object
    extra = 5


class ContextAdmin(admin.ModelAdmin):
    list_display = ['url']
    list_filter = ['url']
    search_fields = ['url']
    inlines = [KeyInline]


class KeyAdmin(admin.ModelAdmin):
    list_display = ('property', 'context')
    list_filter = ['context__url', 'context__prefix', 'property']
    search_fields = ['prefix']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('value', 'context')
    list_filter = ['context__prefix', 'context__url', 'value']
    search_fields = ['value']
    inlines = [PredicateInline]


class PredicateAdmin(admin.ModelAdmin):
    list_display = ('subject', 'property', 'keyword')
    list_filter = ['property__context__prefix', 'property__context__url', 'subject', 'keyword']
    search_fields = ['subject', 'keyword']
    inlines = [ObjectInline]


class ObjectAdmin(admin.ModelAdmin):
    list_display = ('predicate', 'property', 'object', 'label')
    list_filter = ['property__context__prefix', 'property__context__url', 'predicate', 'object', 'label']
    search_fields = ['predicate', 'object', 'label']


admin.site.register(Context, ContextAdmin)
admin.site.register(Key, KeyAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Predicate, PredicateAdmin)
admin.site.register(Object, ObjectAdmin)
