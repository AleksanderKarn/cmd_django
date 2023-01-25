from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.views.generic.base import View
from django.urls import reverse_lazy
from blog.models import Post


class PostView(View):
    '''вывод записей'''
    def get(self, request):
        posts = Post.objects.filter(publication=True)
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(publication=True)




class PostDetail(View):
    '''Одна запись'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk, publication=True)
        post.view_count += 1
        post.save()
        return render(request, 'blog/blog_detail.html', {'post': post})



class PostCreateView(CreateView):
    model = Post
    fields = ('tittle', 'content', 'img', 'publication' )
    success_url = reverse_lazy('blog:list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['tittle', 'content', 'img', 'publication']
    success_url = reverse_lazy('blog:list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')

