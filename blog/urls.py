from django.urls import path
from blog.views import PostCreateView, PostUpdateView, PostListView, PostDeleteView, PostDetail, PostView

app_name = "blog"

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='id'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('list/', PostListView.as_view(), name='list'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),


]