from django.db import models
from django.core.urlresolvers import reverse

from pypinyin import lazy_pinyin
from datetime import datetime


class Author(models.Model):
    """博客的作者信息"""

    # TODO: 头像
    name = models.CharField('昵称', max_length=30)
    email = models.EmailField(blank=True)
    introduce = models.CharField('介绍', max_length=150, blank=True, null=True)

    def __str__(self):
        return '%s' % self.name


class Category(models.Model):
    """每篇博文均属于一个类别"""

    category = models.CharField('类别', max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, editable=False)

    def __str__(self):
        return '%s' % self.category

    def save(self, *args, **kwargs):
        """覆盖默认的save方法，自动生成拼音slug"""

        cate_name = self.category
        py_cate = lazy_pinyin(cate_name)
        if len(py_cate) > 1:
            slug = '_'.join(py_cate)
        else:
            slug = py_cate[0]

        self.slug = slug

        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['category']


class Article(models.Model):
    """发布博文的具体信息"""

    property_choice = (
        ('original', '原创'),
        ('transshipment', '转载')
    )

    status_choice = (
        ('unpublished', '草稿'),
        ('published', '发布')
    )

    ownership = models.CharField('属性', max_length=30, choices=property_choice)
    title = models.CharField('标题', max_length=255)
    category = models.ForeignKey(Category, verbose_name='类别')
    read_num = models.IntegerField('阅读次数', default=0, editable=False)
    publish_time = models.DateTimeField('发布时间',  blank=True, null=True, editable=False)
    update_time = models.DateTimeField('修改时间', editable=False)
    status = models.CharField('状态', max_length=30, choices=status_choice, default=status_choice[0][0])
    content = models.TextField('内容')

    def __str__(self):
        return '%s %s %s %s %s' % (self.title, self.ownership, self.status,
                                   self.category.category, self.update_time.strftime('%Y-%m-%d %H:%M:%S'))

    def save(self, *args, **kwargs):
        current_time = datetime.now()
        if 'update_time' in kwargs:     # 自动设置update_time
            self.update_time = kwargs['update_time']
        else:
            self.update_time = current_time

        if self.publish_time is None and self.status == 'published':    # 发布时自动设置publish_time
            if 'publish_time' in kwargs:    # 自动设置publish_time
                self.publish_time = kwargs['publish_time']
            else:
                self.publish_time = current_time

        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publish_time', 'title']
        unique_together = ('title', 'category')

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[str(self.pk)])

    def publish_time_format(self):
        if getattr(self, 'publish_time') is None:
            return '-'
        return self.publish_time.strftime('%Y-%m-%d %H:%M:%S')
    publish_time_format.short_description = '发布时间'

    def update_time_format(self):
        return self.update_time.strftime('%Y-%m-%d %H:%M:%S')
    update_time_format.short_description = '修改时间'
