from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification  # استدعاء الموديل
from rest_framework.generics import get_object_or_404


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # 🔔 هنا نضيف Notification
        if post.author != request.user:  # منطق بسيط: ما تبعتش إشعار لنفسك
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post
            )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
        return Response({"detail": "You have not liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)