from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from dummy_data_app.serializers import NewsSerializer
from dummy_data_app.models import News

class NewsViewset(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    # TODO: Limit modification requests only to admin users