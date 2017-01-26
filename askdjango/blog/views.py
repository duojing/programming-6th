from django.http import HttpResponse
from django.shortcuts import render
import datetime


class NowTemplateView:
    @staticmethod
    def as_view(template_name=None):
        def view(request):
            now = datetime.datetime.now()
            if template_name is None:
                return HttpResponse('현재 시각은 {}입니다.'.format(now))
            return render(request, template_name, {
                'now': now,
            })
        return view


post_list = NowTemplateView.as_view('blog/post_list.html')

current_datetime = NowTemplateView.as_view()

def hello_none(request):
    return HttpResponse('그냥 안녕!')

def hello(request, name, age=None):
    if age:
        message = '안녕하세요. {}님. {}세이시네요.'.format(name, age)
    else:
        message = '안녕하세요. {}님. 나이도 안 알려주고.'.format(name)
    return HttpResponse(message)


def mysum(request, arg):
    # arg  # "11321/12312/1231//123123/1231231///13123/"
    result = sum(int(i or 0) for i in arg.split('/'))
    return HttpResponse('결과는 {}입니다.'.format(result))

