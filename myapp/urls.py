from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup.as_view(), name='signup_view'),
    path('login', views.login.as_view(), name='login_view'),
    path('friends', views.friends, name='friends'),
    path('talk_room/<int:pk>', views.talk_room, name='talk_room'),
    path('setting', views.setting, name='setting'),
    path('setting/<int:pk>/username_change', views.username_change.as_view(), name='username_change'),
    path('logout', views.logout.as_view(), name='logout_view'),
]

# CustomUser で img を画像へのリンクで記憶するための設定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)