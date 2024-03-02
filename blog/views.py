from django.shortcuts import render,redirect
from .models import *
from category.models import Category
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from .import forms
from django.urls import reverse_lazy
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
# Create your views here.


def home(request,category_slug = None):
    blogs = Blog.objects.order_by('-created_date')
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        blogs = Blog.objects.filter(category  = category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'blogs' : blogs, 'category' : categories})
    

def blog(request,category_slug = None):
    blogs = Blog.objects.order_by('-created_date')
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        blogs = Blog.objects.filter(category  = category)
    categories = Category.objects.all()
    return render(request, 'blogs.html',{'blogs' : blogs, 'category' : categories})


@login_required
def MyBlog(request):
    blogs = Blog.objects.all()
    return render (request,'myblog.html',{'blogs':blogs})



@login_required
def Pagination(request):
    queryset = Blog.objects.all()
    paginated = Paginator(queryset, 3)
    page_number = request.GET.get('page') 
    
    page = paginated.get_page(page_number)
    
   
    return render(request, 'pagination.html', {'page':page})



@method_decorator(login_required, name='dispatch')
class Details(DetailView):
        model = Blog
        pk_url_kwarg = 'id'
        template_name = 'blog_details.html'
        context_object_name = 'Blogs'
        
        
@method_decorator(login_required, name='dispatch')       
class AddPostCreateView(CreateView):
    model = Blog
    form_class = forms.BlogForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    
    
@method_decorator(login_required, name='dispatch')   
class EditPostView(UpdateView):
    model = Blog
    form_class = forms.BlogForm
    template_name = 'edit_blog.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('myblog')
  
@method_decorator(login_required, name='dispatch')  
class DeletePostView(DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('myblog')
    pk_url_kwarg = 'id'

@login_required 
def profile(request):
    user_profile = Profile.objects.all()
    return render(request, 'profile.html',{'user_profile': user_profile})  

@login_required 
def add_fav(request, id):
    blogModel = Blog.objects.get(pk = id)
    blogModel.is_fav = True
    blogModel.save()
    mailsubject = "Favorite Blog"
    message = render_to_string('favBlog_email.html',{'blogModel': blogModel})
    to_email = request.user.email
    send_mail(mailsubject, message, None, [to_email])
    return redirect('blog')

@login_required 
def add_favList(request):
    AllBlog = Blog.objects.filter(is_fav=True)
    return render(request, 'favList.html',{'AllBlog': AllBlog})

@login_required    
def remove_fav(request, id):
    blogModel = Blog.objects.get(pk = id)
    blogModel.is_fav = False
    blogModel.save()
    
    return redirect('add_favlist')