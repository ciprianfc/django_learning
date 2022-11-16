from django.urls import path, reverse_lazy
from . import views

app_name = 'well'
urlpatterns = [
    path('', views.PostListView.as_view(), name='all'),
    path('post/<int:pk>',views.PostDetailView.as_view(), name='post_detail'),
    path('post/create', 
        views.PostCreateView.as_view(success_url=reverse_lazy('well:all')),name='post_create'),
    path('post/<int:pk>/update',
        views.PostUpdateView.as_view(success_url=reverse_lazy('well:all')),name='post_update'),
    path('post/<int:pk>/delete',
        views.PostDeleteView.as_view(success_url=reverse_lazy('well:all')),name='post_delete'),
]
