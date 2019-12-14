from django.http import JsonResponse
from rest_framework.views import APIView
from app.book.models import Book
from common.CommonFunc import check_login
from django.core.files.uploadedfile import InMemoryUploadedFile
import json


class BookContentFileView(APIView):

    @check_login
    def post(self, request, isbn):
        """
        通过上传文件为图书新增内容
        :param request:
        :param isbn:
        :return:
        """
        try:
            memoryFile = request.FILES.get('file')
            file = memoryFile.open()
            content = (file.read()).decode('utf-8')
            book = Book.objects.filter(ISBN=isbn)
            if not book.exists():
                return JsonResponse({
                    'status': False,
                    'errMsg': '该图书不存在'
                })
            book = book[0]
            book.content = content
            book.save()
            return JsonResponse({
                'status': True,
                'isbn': isbn
            })
        except Exception as ex:
            return JsonResponse({
                'status': True,
                'errMsg': '错误信息：' + str(ex)
            }, status=403)
