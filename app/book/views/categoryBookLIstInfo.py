from app.book.models import Category, Book
from django.http import JsonResponse
from rest_framework.views import APIView
from common.CommonFunc import check_login, model_to_dict


class CategorySearchBookView(APIView):

    @check_login
    def get(self, request, categoryID):
        """
        通过目录名来获取图书
        :param request:
        :param category:
        :return:
        """
        categoryOBJ = Category.objects.filter(id=categoryID)
        if not categoryOBJ.exists():
            return JsonResponse({
                'status': False,
                'errMsg': '未找到分类'
            }, status=404)
        categoryOBJ = categoryOBJ[0]
        ca_book = Book.objects.filter(category=categoryOBJ)
        result = [model_to_dict(ca) for ca in ca_book]
        return JsonResponse({
            'status': True,
            'book': result
        })
