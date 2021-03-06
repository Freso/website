# pylint: disable=C0103, C0301
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import forms
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login,
        {'template_name': 'accounts/login.html',
         'authentication_form': forms.LoginForm},
        name='login'),
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'accounts/logout.html'},
        name='logout'),
    url(r'^password/change/$', auth_views.password_change,
        kwargs={'template_name': "accounts/password_change.html"},
        name='password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done,
        kwargs={'template_name': "accounts/password_change_done.html"},
        name='password_change_done'),
    url(r'^password/reset/$', auth_views.password_reset,
        kwargs={'template_name': "accounts/password_reset.html"},
        name='password_reset'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  # noqa
        auth_views.password_reset_confirm,
        kwargs={'template_name': "accounts/password_reset_confirm.html"},
        name='password_reset_confirm'),
    url(r'^password/reset/done/$', auth_views.password_reset_done,
        kwargs={'template_name': "accounts/password_reset_done.html"},
        name='password_reset_done'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete,
        kwargs={'template_name': "accounts/password_reset_complete.html"},
        name='password_reset_complete'),

    url(r'^register/$', views.register, name="register"),
    url(r'^auth/$', views.client_auth, name="client_auth"),
    url(r'^verify/$', views.client_verify),
    url(r'^associate-steam/', views.associate_steam, name="associate_steam"),
    url(r'^(?P<username>.*)/library/$', views.library_show,
        name="library_show"),
    url(r'^library/add/(?P<slug>[\w-]+)/$', views.library_add,
        name="add_to_library"),
    url(r'^library/remove/(?P<slug>[\w-]+)/$', views.library_remove,
        name="remove_from_library"),
    url(r'^library/steam-sync/', views.library_steam_sync,
        name="library_steam_sync"),
    url(r'profile/$', views.profile, name="profile"),
    url(r'(.*)/edit/$', views.profile_edit, name='profile_edit'),
    url(r'(.*)/$', views.user_account, name="user_account"),
    url(r'send-confirmation$', views.user_send_confirmation, name='user_send_confirmation'),
    url(r'confirm$', views.user_email_confirm, name='user_email_confirm'),
    url(r'discourse-sso$', views.discourse_sso, name='discourse_sso'),
]
