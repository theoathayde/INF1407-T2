from django.shortcuts import render, get_object_or_404
from forum.models import Post
from django.views.generic.base import View
from forum.forms import PostForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from datetime import date, datetime
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin



class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        contexto = {'posts': posts, }
        return render(request, "forum/listaPosts.html", contexto)


class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': PostForm, }
        return render(request, "forum/criaPost.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            post = formulario.save()
            post.save()
            return HttpResponseRedirect(reverse_lazy("forum:lista-posts"))


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'data': date.today().strftime("%d de %B de %Y"),
            'hora' : datetime.now().strftime("%H:%M:%S"),
            'option': 1, 
            }
        return render(request,'forum/index.html',context)    


class PostVisualizarView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        contexto = {'post': post}
        return render(request, 'forum/visualizaPost.html', contexto)

class PostUpdateView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk, *args, **kwargs):
        post= Post.objects.get(pk=pk)
        formulario = PostForm(instance=post)
        context = {'post': formulario, }
        return render(request, 'forum/updatePost.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        formulario = PostForm(request.POST, instance=post)
        if formulario.is_valid():
            post = formulario.save() # cria uma pessoa com os dados do formulário
            post.save() # salva uma pessoa no banco de dados
            return HttpResponseRedirect(reverse_lazy("forum:lista-posts"))
        else:
            contexto = {'post': formulario, }
            return render(request, 'forum/updatePost.html', contexto)



class PostDeleteView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser
        
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        contexto = { 'post': post, }
        return render(request, 'forum/deletaPost.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        post.delete()
        return HttpResponseRedirect(reverse_lazy("forum:lista-posts"))



def homeSec(request):
    return render(request,"autent/homeSec.html")


def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    context = {'form': formulario, }
    return render(request,'autent/registro.html', context)

@login_required
def perfil(request):
    return render(request, 'autent/perfil.html')