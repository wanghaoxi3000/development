from django.shortcuts import render
from django.views.generic import View

from .models import CourseOrg, CityDict


class OrgView(View):
    """
    课程列表功能
    """

    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        all_cities = CityDict.objects.all()

        return render(request, 'org-list.html', {
            'all_orgs': all_orgs,
            'org_nums': org_nums,
            'all_cities': all_cities
        })
