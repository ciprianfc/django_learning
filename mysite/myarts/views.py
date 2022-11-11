from myarts.models import Article
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

# Create your views here.


class ArticleListView(OwnerListView):
    model = Article
    # By convention : template_name = "myarts/article_list.html"


class ArticleDetailView(OwnerDetailView):
    model = Article

class ArticleCreateView(OwnerCreateView):
    model = Article
    #List of fields to copy from the article model to the article form
    fields = ['title', 'text']

class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ['title', 'text']

class ArticleDeleteView(OwnerDeleteView):
    model = Article

