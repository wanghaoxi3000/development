from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'ownership', 'category', 'read_num', 'status',
                    'publish_time_format', 'update_time_format')
    list_filter = ('ownership', 'category')
    # 时间过滤器 修改好后，页面中的列表顶端会有一个逐层深入的导航条，它从可用的年份开始，然后逐层细分到月乃至日
    date_hierarchy = 'publish_time'
    # 用于多对多字段显示，出现一个JS过滤器，允许你检索选项，然后将选中的tag从Available框移到Chosen框，还可以移回来
    # filter_horizontal = ('tags',)


admin.site.register(models.Author)
admin.site.register(models.Category)
admin.site.register(models.Article, ArticleAdmin)
