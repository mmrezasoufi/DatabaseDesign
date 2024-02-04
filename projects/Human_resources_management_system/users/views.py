from rest_framework.generics import ListAPIView
from .models import User
from .serializers import UserSerializer
from utils import CustomPagination


class UserList(ListAPIView):
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        users = User.objects.prefetch_related("was_employeed", "addresses", "phone_numbers").all()
        return users
    