from django.http import JsonResponse
from common.CommonFunc import check_login, model_to_dict
from app.book.models import Category
from app.administrator.models import Administrator
from rest_framework.views import APIView
import json


class CategoryInfoView(APIView):

    @check_login
    def post(self, request):
        """
        新增分类
        :param request:
        :return:
        """
        try:
            user = Administrator.objects.get(idCard=request.session.get('login'))
            jsonParams = json.loads((request.body).decode('utf-8'))
            categoryName = jsonParams.get('name', '')
            if categoryName == '':
                return JsonResponse({
                    'status': False,
                    'errMsg': '目录名不能为空'
                }, status=401)
            if Category.objects.filter(name=categoryName).exists():
                return JsonResponse({
                    'status': False,
                    'errMsg': '该分类已存在'
                }, status=401)
            newCategory = Category.objects.create(
                name=categoryName,
                createUser=user
            )
            return JsonResponse({
                'status': True,
                'id': newCategory.id,
                'name': newCategory.name
            })
        except Exception as ex:
            return JsonResponse({
                'status': False,
                'errMsg': '错误信息：' + str(ex)
            }, status=403)

    @check_login
    def get(self, request):
        """
        获取分类列表
        :param request:
        :return:
        """
        categoryList = Category.objects.all()
        all_category = [model_to_dict(ca, exclude='createUser') for ca in categoryList]
        return JsonResponse({
            'status': True,
            'category': all_category
        })
