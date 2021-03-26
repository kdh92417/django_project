from django.http                import HttpResponse
from django.views.generic       import View

class MyView(View):
    def get(self, request):
        # 뷰 로직 작성
        return HttpResponse('result')
