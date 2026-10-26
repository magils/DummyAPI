from rest_framework.viewsets import ModelViewSet

from dummy_data_app.serializers import NewsSerializer
from dummy_data_app.models import News


# TODO: Limit modification requests only to admin users
class NewsViewset(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        q = News.objects.all()
        params = self.request.query_params

        if category := params.get("category"):
            q = q.filter(category__iexact=category)
        if country := params.get("country"):
            q = q.filter(country__iexact=country)
        if author := params.get("author"):
            q = q.filter(author_iexact=author)
        if featured := params.get("is_featured"):
            q = q.filter(is_featured=featured.lower() == "true")

        return q
