from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog, Comment
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseNotFound

# Create your views here.


def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
        page = 1
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'posts': posts, 'pages': range(1, paginator.num_pages+1), 'current': int(page), 'user': request.user })


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    postComment = Comment.objects.filter(blog=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail, 'comments': postComment, 'user': request.user, 'blog_id': str(blog_id)})


def write(request):
    if request.user.is_authenticated:
        return render(request, 'write.html',{'user': request.user})   
    else:
        return redirect('login')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pup_date = timezone.datetime.now()
    blog.author = request.user
    blog.save()
    return redirect('/blog/'+str(blog.id))

def comment(request, blog_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment = Comment()
            comment.comment = request.POST['inputComment']
            comment.pup_date = timezone.datetime.now()
            comment.author = request.user
            comment.blog = Blog.objects.get(id=blog_id)
            comment.save()
            return redirect('/blog/'+str(blog_id))
        else:
            return redirect('login')
    else:
        return HttpResponseNotFound("없는 페이지 입니다.")

def search(request):
    if request.method == 'POST':
        blogList = Blog.objects.filter(title__icontains=request.POST['search'])
        print(blogList)
        return render(request, 'search.html', {'posts': blogList, 'user': request.user })
    else:
        return HttpResponseNotFound("없는 페이지 입니다.")