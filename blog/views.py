from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import blogpost,blogcomment
from django.contrib.auth.models import User
from blog.templatetags import get_dict
# Create your views here.
def bloghome(request):
    blogs=blogpost.objects.all()
    params={'blogs':blogs}
    return render(request, 'blog/bloghome.html',params)
def blogposts(request,slug):
    blogs=blogpost.objects.filter(slug=slug)
    comments=blogcomment.objects.filter(blog=blogs[0],parent=None)
    replies=blogcomment.objects.filter(blog=blogs[0]).exclude(parent=None)
    rep={}
    for reply in replies:
      if reply.parent.srno not in rep.keys():
        rep[reply.parent.srno]=[reply]
      else:
        rep[reply.parent.srno].append(reply)
    params={'myblog':blogs,'comments':comments,'user':request.user,'rep':rep}
    return render(request, 'blog/blogpost.html',params)
def blogcomments(request):
    if request.method=="POST":
        user=request.user
        blogsno=request.POST.get('blogsno')
        blog=blogpost.objects.get(srno=blogsno)
        comment=request.POST.get('comment')
        parentsno=request.POST.get('parentsno')
        if parentsno=='':
            comments=blogcomment(comment=comment,user=user,blog=blog)
        else:
            parent=blogcomment.objects.get(srno=parentsno)
            pcomment=request.POST.get('pcomment')
            comments=blogcomment(comment=pcomment,user=user,blog=blog,parent=parent)
        comments.save()
        return redirect(f'/blog/{blog.slug}')
