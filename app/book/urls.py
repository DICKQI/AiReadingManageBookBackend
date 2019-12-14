from .views import *
from django.urls import path

app_name = 'Book'

urlpatterns = [
    path('', BookInfoView.as_view(), name='newBook'),
    path('file/<str:isbn>/', BookContentFileView.as_view(), name='bookContentFileInfo'),
    path('category/', CategoryInfoView.as_view(), name='categoryInfo'),
    path('<str:isbn>/', BookInfoView.as_view(), name='bookInfo'),
]
