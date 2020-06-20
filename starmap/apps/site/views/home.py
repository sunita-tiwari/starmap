from django.shortcuts import render
from django.views.generic import TemplateView
from django import forms
import json
from starmap.apps.site.models.product import Product


# class ViewSiteHome(TemplateView):
#     """
#     This view show the homepage
#     """
#
#     template_name = "site/home.html"
#
#     def post(self, request, *args, **kwargs):
#         data = self.request.POST.get("json_data")
#         product_data = json.loads(data)
#         crt = Product.objects.create(**product_data)
#         request.session['user_uuid'] = str(crt.uuid)
#         return render(request, 'site/done.html')


class ViewSiteUpdate(TemplateView):
    """
    This view show the homepage
    """

    template_name = "site/update.html"

    def get(self, request, *args, **kwargs):
        if request.session.get('user_uuid', None) != None:
            uuid = request.session.get('user_uuid')
            obj = Product.objects.get(uuid = uuid)
            return render(request, 'site/update.html',{'data':obj})

class ViewNewStar(TemplateView):

    template_name = "site/new-star.html"

    def post(self, request, *args, **kwargs):
        data = self.request.POST.get("json_data")
        product_data = json.loads(data)
        crt = Product.objects.create(**product_data)
        request.session['user_uuid'] = str(crt.uuid)
        return render(request, 'site/done.html')

class ViewNewStarBackup(TemplateView):

    template_name = "site/new_starmap_bckup.html"