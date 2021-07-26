from django.views.generic import ListView, DetailView
from . models import Article
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class ArticlePageView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'Prashvi'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'new_article.html'
    fields = '__all__'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title','text']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    context_object_name = 'Prashvi'
    success_url = reverse_lazy('home')
