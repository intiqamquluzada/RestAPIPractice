from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, \
    CreateAPIView

from .filters import PostFilter
from .models import Post
from .serializers import PostSerializer, PostCreateSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwner


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter

    # def get_queryset(self):
    #     queryset = Post.objects.filter(draft=False)
    #     return queryset


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"


class PostDeleteView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"


class PostUpdateView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"
    permission_classes = (IsOwner,)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
