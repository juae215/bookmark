from django.shortcuts import render # 실제 서버에서 돌아가는 일을 관리

# Create your views here.
# CRUD : Creat, Read, Update, Delete
# List

#클래스, 함수형 뷰
#웹페이지에 접속 ->페이지를 본다  
#url입력 -> 웹 서비가 뷰를 찾아서 동작시킴

# 어떤 url을 쓸지 등록해줘야함 -> config urls에서 만듬

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy

class BookmarkListView(ListView):
    model = Bookmark

class BookmarCreatetView(CreateView):
    model = Bookmark
    fields =['site_name','url'] #해당 모델들 중에 어떤 필드내용들을 수정할 것이냐?
    success_url = reverse_lazy('List')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('List') #삭제하면 이곳으로 가라
    