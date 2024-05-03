from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    # 1. 字段排序
    # fields = ["pub_date", "question_text"]

    # 2. 自定义字段集
    fieldsets = [
        ("基础信息", {'fields': ['question_text']}),
        ("时间信息", {'fields': ['pub_date']}),
    ]

    # inlines, 外键关联
    inlines = [ChoiceInline]

    # 列表展示，可以是函数
    list_display = ["question_text", "pub_date", "was_published_recently"]

    # 列表过滤，在页面右侧添加一个过滤栏
    list_filter = ["pub_date"]

    # 搜索字段
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
