from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from .forms import BlogForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def all_blogs(request):
    blogs=Blog.objects.all().order_by('-created_at')
    return render(request, 'blogs/all_blogs.html',{"blogs":blogs})

@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect('all_blogs')

    else:
        form=BlogForm()
    return render(request, 'blogs/blog_form.html',{'form':form})

def blog_detail(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blogs/blog_detail.html',{'blog':blog})
    

@login_required
def delete_blog(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id,user=request.user)
    if request.method =="POST":
        blog.delete()
        return redirect("all_blogs")
    return render(request, 'blogs/blog_confirm_delete.html',{'blog':blog})

@login_required
def edit_blog(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id,user=request.user)
    if request.method == "POST":
        form=BlogForm(request.POST, request.FILES,instance=blog)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect("all_blogs")
    else:
        form=BlogForm(instance=blog)
    return render(request, 'blogs/blog_form.html',{'form':form})


def registerUser(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('all_blogs')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{"form":form})





def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        blogs = Blog.objects.filter(text__contains=search_query)
        # for blog in blogs:
        #     print(blog.text)
        return render(request, 'blogs/search_blog.html', {'query':search_query,'blogs':blogs})
    else:
        return render(request, 'blogs/search_blog.html',{})