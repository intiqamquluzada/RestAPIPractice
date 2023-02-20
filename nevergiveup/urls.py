from django.urls import path
from nevergiveup.views import *

urlpatterns = [
    path("list/", PostListView.as_view(), name='list'),
    path("list/<slug>/", PostDetailView.as_view(), name='detail'),
    path("delete/<slug>", PostDeleteView.as_view(), name='delete'),
    path("update/<slug>/", PostUpdateView.as_view(), name='update'),
    path("create/", PostCreateView.as_view(), name='create'),
]
