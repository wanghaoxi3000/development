from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg, CityDict


class OrgView(View):
    """
    课程列表功能
    """

    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_cities = CityDict.objects.all()
        hot_orgs = all_orgs.order_by("-click_num")[:3]

        # 筛选城市
        city_id = request.GET.get("city", "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        sort = request.GET.get('sort', "")
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('course_nums')

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)
        org_nums = all_orgs.count()

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'org_nums': org_nums,
            'all_cities': all_cities,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort,
        })
