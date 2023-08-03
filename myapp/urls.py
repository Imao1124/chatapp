from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup_view.as_view(), name='signup_view'),
    path('login', views.login.as_view(), name='login_view'),
    path('friends', views.friends, name='friends'),
    path('talk_room/<int:pk>', views.talk_room.as_view(), name='talk_room'),
    path('setting', views.setting, name='setting'),
]

# CustomUser で img を画像へのリンクで記憶するための設定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)