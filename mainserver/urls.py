from django.conf.urls import url, include
from mainserver import views
from mainserver.views import LoginViewSet
from rest_framework.routers import DefaultRouter
# from rest_framework.schemas import get_schema_view



router = DefaultRouter()
router.register(r'main_login', views.LoginViewSet, base_name='login')
# router.register(r'get_bal', views.BalViewSet, base_name='balance')
# router.register(r'payment', views.PaymentViewSet)
# router.register(r'response', views.ResponseViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^get_bal/', views.Get_Bal.as_view()),
    url(r'^forget/$', views.Forget_password.as_view()),
    # url(r'^main_login/$', views.LoginViewSet.as_view()),
    # url(r'^schema/$', schema_view),
]
# urlpatterns += router.urls