from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
# post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('api', views.post_list_APIView.as_view(), name='api'),
    # path('api/<pk>', views.post_list_APIView.as_view(), name='api_detail')
]