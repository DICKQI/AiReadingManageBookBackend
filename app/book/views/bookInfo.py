from django.http import JsonResponse
from rest_framework.views import APIView
from app.book.models import Book, Category
from app.administrator.models import Administrator
from common.CommonFunc import check_login, model_to_dict
import json


class BookInfoView(APIView):

    @check_login
    def post(self, request):
        """
        新增图书
        :param request:
        :return:
        """
        try:
            jsonParams = json.loads((request.body).decode('utf-8'))
            name = jsonParams.get('name', '')
            ISBN = jsonParams.get('ISBN', '')
            content = jsonParams.get('content', '')
            if Book.objects.filter(ISBN=ISBN).exists():
                return JsonResponse({
                    'status': False,
                    'errMsg': '该isbn已存在'
                }, status=401)
            category = Category.objects.get(name=jsonParams.get('category', ''))
            user = Administrator.objects.get(idCard=request.session.get('login'))
            newBook = Book.objects.create(
                name=name,
                ISBN=ISBN,
                content=content,
                category=category,
                createUser=user
            )
            category.count += 1
            category.save()
            return JsonResponse({
                'status': True,
                'id': newBook.id
            })
        except Exception as ex:
            return JsonResponse({
                'status': False,
                'errMsg': '错误信息：' + str(ex)
            }, status=403)

    @check_login
    def get(self, request, isbn):
        """
        获取图书详情
        :param request:
        :param isbn:
        :return:
        """
        book = Book.objects.filter(ISBN=isbn)
        if not book.exists():
            return JsonResponse({
                'status': False,
                'errMsg': '该编号的图书不存在'
            }, status=404)
        book = book[0]
        bookResult = model_to_dict(book)
        return JsonResponse({
            'status': True,
            'book': bookResult
        })

    @check_login
    def delete(self, request, isbn):
        """
        删除指定图书
        :param isbn:
        :param request:
        :return:
        """
        book = Book.objects.filter(ISBN=isbn)
        if not book.exists():
            return JsonResponse({
                'status': False,
                'errMsg': '该编号的图书不存在'
            }, status=404)
        book = book[0]
        book.delete()
        return JsonResponse({
            'status': True,
            'isbn': isbn
        })

    @check_login
    def put(self, request, isbn):
        """
        修改指定图书
        :param request:
        :param isbn:
        :return:
        """
        try:
            book = Book.objects.filter(ISBN=isbn)
            if not book.exists():
                return JsonResponse({
                    'status': False,
                    'errMsg': '该编号的图书不存在'
                }, status=404)
            book = book[0]
            jsonParams = json.loads((request.body).decode('utf-8'))
            name = jsonParams.get('content', book.name)
            content = jsonParams.get('content', book.content)
            category = Category.objects.get(name=jsonParams.get('category', book.category.name))
            book.name = name
            book.content = content
            book.category = category
            book.save()
            bookDetail = model_to_dict(book)

            return JsonResponse({
                'status': True,
                'book': bookDetail
            })
        except Exception as ex:
            return JsonResponse({
                'status': False,
                'errMsg': '错误信息：' + str(ex)
            })
