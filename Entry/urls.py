from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout


app_name='Entry'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),

    url(r'^(?P<user_id>[0-9]+)/followed/$', views.FollowIndexView.as_view(),name='followed'),

    url(r'^(?P<user_id>[0-9]+)/followedby/$', views.FollowedByIndexView.as_view(),name='followedby'),

    url(r'^reviewer/register/$', views.ReviewerFormView.as_view(),name='reviewer-register'),

    url(r'^search-results/$', views.search,name='search-results'),

    url(r'^register/$', views.UserFormView.as_view(),name='register'),

    url(r'^login/$', views.LoginFormView.as_view(),name='login'),

    url(r'^logout/$', logout, {'next_page': '/entry/login'},name='logout'),


    url(r'^profile/add/$',views.ProfileCreate.as_view(),name='profile-create'),

    
    url(r'^profile/(?P<pk>[0-9]+)/$',views.ProfileUpdate.as_view(),name='profile-update'),


    url(r'^userdetail/(?P<pk>[0-9]+)/$',views.UserDetailView.as_view(),name='userdetail'),

    url(r'^userdetail/(?P<pk>[0-9]+)/follow/$',views.follow,name='follow'),

    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),

    url(r'^(?P<entry_id>[0-9]+)/rate/$',views.rate,name='rate'),

    

	url(r'^(?P<entry_id>[0-9]+)/like/$',views.like,name='like'),

    url(r'^(?P<entry_id>[0-9]+)/bookmark/$',views.bookmark,name='bookmark'),



	url(r'^entry/add/$',views.EntryCreate.as_view(),name='entry-add'),

    url(r'^entry/myworks/$',views.MyWorks.as_view(),name='myworks'),

    url(r'^entry/liked/$',views.MyLikes.as_view(),name='liked-entries'),

    url(r'^entry/bookmarked/$',views.MyBookmarks.as_view(),name='bookmarked-entries'),



	url(r'^entry/(?P<pk>[0-9]+)/$',views.EntryUpdate.as_view(),name='entry-update'),

	url(r'^entry/(?P<pk>[0-9]+)/delete/$',views.EntryDelete.as_view(),name='entry-delete'),

]