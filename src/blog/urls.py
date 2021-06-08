from django.urls import path
from .views import (
	ArticleListView,
	ArticleCreateView,
	ArticleDetailView,
	ArticleUpdateView,
	ArticleDeleteView
)

app_name = 'articles_ns'
urlpatterns = [
	path('', ArticleListView.as_view(), name='article-list'),
	path('create/', ArticleCreateView.as_view(), name='article-create'),
	path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
	path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
	path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]