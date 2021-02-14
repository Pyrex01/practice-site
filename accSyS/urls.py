from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index,name="home"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("get_otp",views.send_otp,name="get_otp"),
    path("logout",views.logout,name="logout"),
    path("forgot",views.forgot,name="forgot_password"),
    path("recover_chk",views.recover_chk,name="recover_chk"),
    path("pass_update",views.pass_update,name="pass_update"),
    path("view",views.view,name="view"),
    path('see/<int:id>',views.see,name="see"),
    path('my_item/<int:id>',views.my_item,name="my_item"),
    path('delete_item/<int:id>',views.delete_item,name="delete_item")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)