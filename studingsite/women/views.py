from lib2to3.fixes.fix_input import context

from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from unicodedata import category

from .forms import AddPostForm
from .models import Women, Category, TagPost

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]




# Create your views here.
def index(request):
    posts = Women.published.all().select_related('cat')
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': posts,
            'cat_selected': 0
            }
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})

def addpage(request):
    if request.method == 'POST':
        form =  AddPostForm(request.POST)
        if form.is_valid():
           # print(form.cleaned_data)
           #  try:
           #      Women.objects.create(**form.cleaned_data)
           #      return redirect('home')
           #  except:
           #      form.add_error(None, 'Ошибка при добавлении поста')
            form.save()
            return redirect('home')

    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form
    }
    return render(request, 'women/addpage.html', data)

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected':1
    }

    return render(request, 'women/post.html', data)

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')
    data = {'title': f'Рубрика {category}',
           'menu': menu,
           'posts': posts,
           'cat_selected': category.pk
           }
    return render(request, 'women/index.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')
    data = {
        'title': f'Тег: { tag.tag }',
        'menu': menu,
        'posts':posts,
        'cat_selected': None
    }

    return render(request, 'women/index.html', context=data)