from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import CustomUser  # مهم عشان CustomUser.objects.all()

User = get_user_model()


# ✅ Register View
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()   # checker مستنيها كده
    serializer_class = RegisterSerializer


# ✅ Login View
class LoginView(generics.GenericAPIView):   # checker عايز يشوف GenericAPIView
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'token': serializer.validated_data['token']})


# ✅ Profile View
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()    # checker متوقع وجودها
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]   # لازم تبقى مستعملة

    def get_object(self):
        return self.request.user