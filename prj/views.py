from django.views.generic.base import TemplateView

#                                                   ch11 1/2
# 테이블 레코드를 생성하기 위한 폼을 보여주고,
# 폼 입력에 따라 테이블 레코드를 생성하는 편집용 제네릭 뷰
# cf: CreateView, UpdateView, DeleteView, FormView
from django.views.generic.edit import CreateView
# User 모델의 객체 생성 폼
from django.contrib.auth.forms import UserCreationForm
# reverse_lazy() 및 reverse() 함수는 URL 패턴명을 인자로 전달 받는데,
# URL 패턴명을 인식하려면 urls.py 모듈이 메모리에 적재되어야 하고,
# 이를 최대한 지연시키기 위하여 reverse()가 아닌 reverse_lazy()를 적용
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# TemplateView 제네릭 뷰를 상속받아서 HomeView 클래스 작성
from blog.models import Post


# class HomeView(TemplateView):
#   # TemplateView를 상속받을 때 template_name 클래스 변수 오버라이딩은 필수
#   # 템플릿 파일의 이름을 지정하는데, 파일의 위치는 settings.TEMPLATES.DIRS 항목에서 정의함
#   template_name = 'home.html'

# 계정 등록                                         ch11 2/2
class UserCreateView(CreateView):
  template_name = 'registration/register.html'
  form_class = UserCreationForm
  success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
  template_name = 'registration/register_done.html'

class LoginRequiredMixin(object):
  @classmethod
  def as_view(cls, **initkwargs):
    view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
    return login_required(view)



from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from blog.models import Post
from shop.models import Item



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.order_by('-updated_at')[:6]
        context['item_list'] = Item.objects.order_by('-price')[:4]

        return context

