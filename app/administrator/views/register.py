from django.http import JsonResponse
from rest_framework.views import APIView
from app.administrator.models import Administrator, Password
from django.contrib.auth.hashers import make_password
import json


class RegisterView(APIView):

    def post(self, request):
        """
        注册
        :param request:
        :return:
        """
        try:
            jsonParams = json.loads((request.body).decode('utf-8'))

            idCard = jsonParams.get('idCard', '')
            password = make_password(jsonParams.get('password', ''))
            name = jsonParams.get('name', '')
            gender = jsonParams.get('gender', '')
            role = jsonParams.get('role', '')

            new_password = Password.objects.create(password=password)

            new_Administrator = Administrator.objects.create(
                idCard=idCard,
                password=new_password,
                name=name,
                gender=gender,
                role=role
            )

            return JsonResponse({
                'status': True,
                'id': new_Administrator.idCard
            })
        except Exception as ex:
            return JsonResponse({
                'status': False,
                'errMsg': '错误信息：' + str(ex)
            }, status=403)
