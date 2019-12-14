from app.book.models import Book
from rest_framework.views import APIView
from django.http import JsonResponse
from common.CommonFunc import check_login, model_to_dict


class BookListInfo(APIView):

    @check_login
    def get(self, request):
        """
        获取书本列表
        :param request:
        :return:
        """
        book = Book.objects.all()
        result = [model_to_dict(b) for b in book]
        return JsonResponse({
            'status': True,
            'book': result
        })
