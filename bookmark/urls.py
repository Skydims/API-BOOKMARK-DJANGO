from django.urls import path
from .views import bookmark_list, bookmark_create, bookmark_update, bookmark_delete

urlpatterns = [
    path('', bookmark_list, name='bookmark-list'),
    path('create/', bookmark_create, name='bookmark-create'),
    path('<int:pk>/update/', bookmark_update, name='bookmark-update'),
    path('<int:pk>/delete/', bookmark_delete, name='bookmark-delete'),
]
