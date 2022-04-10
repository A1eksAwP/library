from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, MyUser


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'