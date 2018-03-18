from django.shortcuts import Http404
from django.views.generic import base, DetailView, ListView
from django.db.models import F

from . import models


class BlogBaseInfo(base.ContextMixin):

    def get_context_data(self, **kwargs):
        """重写get_context_data方法，获取各个页面共有的元素"""

        context = super(BlogBaseInfo, self).get_context_data(**kwargs)

        # 获取文章类别及数目
        categorys = []
        category_objs = models.Category.objects.all()
        for category in category_objs:
            article_num = models.Article.objects.filter(category=category).count()
            categorys.append(['%s (%d)' % (category, article_num), category.slug])

        context['categorys'] = categorys

        # 获取文章存档
        publishs = []
        publish_month = models.Article.objects.datetimes('publish_time', 'month')
        for pub in publish_month:
            pub_num = models.Article.objects.filter(publish_time__year=pub.year, publish_time__month=pub.month).count()
            publishs.append(['%d年%d月 (%d)' % (pub.year, pub.month, pub_num), '%d%02d' % (pub.year, pub.month)])

        publishs.reverse()
        context['publishs'] = publishs

        return context


class BlogList(BlogBaseInfo, ListView):
    context_object_name = 'blog_list'
    template_name = 'blog/index.html'
    paginate_by = 5

    show = ''   # 过滤显示的类别
    name = ''   # 过滤显示的参数

    def get_queryset(self):
        """动态过滤模型列表"""

        article_set = models.Article.objects.filter(status='published')

        self.show = self.kwargs.get('show', '')
        self.name = self.kwargs.get('name', '')

        if self.show == '' or self.name == '':
            return article_set
        elif self.show == 'category':    # 按类别来过滤
            return article_set.filter(category__slug=self.name)
        elif self.show == 'archive':     # 按存档日期来过滤
            if len(self.name) != 6:
                raise Http404
            return article_set.filter(publish_time__year=self.name[0:4], publish_time__month=self.name[4:6])

    def get_context_data(self, **kwargs):
        """为翻页功能修改对应的链接"""

        context = super(BlogList, self).get_context_data(**kwargs)
        context['show'] = self.show
        context['name'] = self.name

        return context


class ArticleDetail(BlogBaseInfo, DetailView):
    model = models.Article
    context_object_name = 'article'
    template_name = 'blog/article_detail.html'

    next_article = None     # 下一篇文章的链接
    prev_article = None     # 上一篇文章的链接

    def get_object(self, queryset=None):
        """获取指定文章对象, 增加阅读次数"""

        obj = super(ArticleDetail, self).get_object()

        # 获取前后文章的链接
        prev_article = models.Article.objects.filter(publish_time__lt=obj.publish_time).first()
        if prev_article is not None:
            self.prev_article = prev_article.get_absolute_url()
        else:
            self.prev_article = None

        next_article = models.Article.objects.filter(publish_time__gt=obj.publish_time).last()
        if next_article is not None:
            self.next_article = next_article.get_absolute_url()
        else:
            self.next_article = None

        # 增加阅读次数
        read_num = obj.read_num
        obj.read_num = F('read_num') + 1    # 通过F来避免竞态
        obj.save(update_fields=['read_num'])
        obj.read_num = read_num
        return obj

    def get_context_data(self, **kwargs):
        """将前后文章的链接添加到上下文中"""

        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['prev'] = self.prev_article
        context['next'] = self.next_article

        return context
