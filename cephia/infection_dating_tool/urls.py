from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

# app_name = 'infection_dating_tool'
urlpatterns = [
    #url(r'^$', views.tools_home, name='tools_home'),
    # url(r'^$', views.home, name='home'),
    # url(r'^register/$', views.idt_user_registration, name='registration'),
    # url(r'^register/info/$', views.idt_user_registration_info, name='registration_info'),
    # url(r'^login/$', views.idt_login, name='login'),
    # url(r'^logout/$', views.idt_logout, name='logout'),
    
    # url(r'^data_files/$', views.data_files, name='data_files'),
    # url(r'^help/$', views.help_page, name='help_page'),
    
    # url(r'^tests/$', views.tests, name='tests'),
    # url(r'^tests/(?P<test_id>\d+)/edit/$', views.edit_test, name='edit_test'),
    # url(r'^tests/create/$', views.create_test, name='create_test'),
    
    # url(r'^test_mapping/$', views.test_mapping, name='test_mapping'),
    # url(r'^test_mapping/(?P<file_id>\d+)/$', views.test_mapping, name='test_mapping'),
    # url(r'^test_mapping/create/$', views.create_test_mapping, name='create_test_mapping'),
    # url(r'^test_mapping/edit/$', views.edit_test_mapping, name='edit_test_mapping'),
    # url(r'^test_mapping/edit/(?P<save_map_id>\d+)/$', views.edit_test_mapping, name='edit_test_mapping_save'),
    
    # url(r'^data_files/(?P<file_id>\d+)/delete', views.delete_data_file, name='delete_data_file'),
    # url(r'^data_files/(?P<file_id>\d+)/process_data', views.process_data_file, name='process_data_file'),
    
    # url(r'^validate_mapping/(?P<file_id>\d+)/', views.validate_mapping_from_page, name='validate_mapping_from_page'),

    # url(r'^results/(?P<file_id>\d+)/$', views.results, name='results'),
    # url(r'^results/(?P<file_id>\d+)/download/$', views.download_results, name='download_results'),

    # url(r'^user_registration/finalise/(?P<token>.*)/$', views.finalise_user_account, name='finalise_user_account'),

]
urlpatterns += staticfiles_urlpatterns()
