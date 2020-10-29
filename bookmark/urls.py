from django.urls import path
from .views import *

urlpatterns = [
    path('', BookmarkListView.as_view(), name = 'List'), #클래스형 뷰일때는 .as_view()를 꼭 해줘야함
    path('add/',BookmarCreatetView.as_view(), name = 'add'),
    path('detail/<int:pk>/',BookmarkDetailView.as_view(),name = 'detail'), #pk 프라이머리 키
    path('update/<int:pk>/',BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',BookmarkDeleteView.as_view(), name='delete'),
]