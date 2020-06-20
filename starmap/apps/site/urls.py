from django.urls.conf import path
# from starmap.apps.site.views.home import ViewSiteHome
# from starmap.apps.site.views.create import ViewSiteCreateStarMap
from starmap.apps.site.views.home import  ViewSiteUpdate, ViewNewStar,ViewNewStarBackup

urlpatterns = [

    # path('', ViewSiteHome.as_view(), name='home'),
    path('update/', ViewSiteUpdate.as_view(), name='update'),
    # path('create/', ViewSiteCreateStarMap.as_view(), name='create-star'),
    path('', ViewNewStar.as_view(), name='new'),
    path('new_bkup/', ViewNewStarBackup.as_view(), name='new_bkup'),


]