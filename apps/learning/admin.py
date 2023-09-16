from django.contrib import admin

from apps.learning.models import Section, Material, Test, Question, Answer, UserAnswer


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'preview', 'description',)
    list_filter = ('section_name',)
    search_fields = ('section_name', 'description',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_name', 'description', 'preview', 'text', 'section',)
    list_filter = ('material_name', 'section',)
    search_fields = ('material_name', 'description', 'text',)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'description', 'material',)
    list_filter = ('test_name', 'material',)
    search_fields = ('test_name', 'description',)
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'text',)
    list_filter = ('test',)
    search_fields = ('text',)
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text',)
    list_filter = ('question',)
    search_fields = ('text',)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'question', 'user', 'is_passed',)
    list_filter = ('user', 'question', 'is_passed',)
    search_fields = ('answer',)

