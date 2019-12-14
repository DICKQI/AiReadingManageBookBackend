from app.administrator.models import Administrator
from rest_framework.views import APIView
from common.CommonFunc import check_login
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
import json


class BaseInfoView(APIView):

    @check_login
    def get(self, request):
        """
        检查是否
        :param request:
        :return:
        """
        return JsonResponse({
            'status': True,
            'idCard': request.session.get('login')
        })

    def post(self, request):
        """
        登录
        :param request:
        :return:
        """
        try:
            jsonParams = json.loads((request.body).decode('utf-8'))

            idCard = jsonParams.get('idCard', '')
            password = jsonParams.get('password', '')

            if idCard == '' or password == '':
                return JsonResponse({
                    'status': False,
                    'errMsg': '证件号或密码不能为空'
                }, status=401)

            user = Administrator.objects.filter(idCard=idCard)
            if not user.exists():
                return JsonResponse({
                    'status': False,
                    'errMsg': "用户不存在"
                }, status=404)
            user = user[0]
            if check_password(password, user.password.password):
                request.session['login'] = user.idCard
                import datetime
                user.last_login_time = datetime.datetime.now()
                user.save()
                return JsonResponse({
                    'status': True,
                    'id': idCard
                })
            else:
                return JsonResponse({
                    'status': False,
                    'errMsg': '密码错误'
                }, status=401)

        except Exception as ex:
            return JsonResponse({
                'status': False,
                'errMsg': '错误信息：' + str(ex)
            }, status=403)

    @check_login
    def delete(self, request):
        """
        用户登出
        :param request:
        :return:
        """
        request.session['login'] = None
        return JsonResponse({
            'status': False
        })
