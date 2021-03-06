import datetime

from models import Article
from haystack import indexes

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author', faceted=True)
    sections = indexes.MultiValueField(faceted=True)
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Article


    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now()).filter(publish=True)

