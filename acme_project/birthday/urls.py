from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('login_only/', views.simple_view),
    # path('', views.birthday, name='create'),
    # path('list/', views.birthday_list, name='list'),
    # path('<int:pk>/edit/', views.birthday, name='edit'),
    # path('<int:pk>/delete/', views.delete_birthday, name='delete'),
    # Декорируем вызов метода as_view(), без синтаксического сахара:
    #path('create/', login_required(views.BirthdayCreateView.as_view()), name='create'),
    path('create/', views.BirthdayCreateView.as_view(), name='create'),
    path('list/', views.BirthdayListView.as_view(), name='list'),
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
]
