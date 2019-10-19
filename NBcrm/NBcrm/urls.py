"""NBcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from nbapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #首页
    url(r'^index/', views.index,name='index'),

    #注册
    url(r'^register/', views.register, name='register'),

    #登录
    url(r'^login/', views.login, name='login'),

    #验证码
    url(r'^get_valid_img/', views.get_valid_img, name='get_valid_img'),

    #注销
    url(r'^logout/', views.logout, name='logout'),
    # url(r'^shopping/', views.shopping, name='shopping'),
    #展示所有公户客户信息
    url(r'^customers/list/', views.customers, name='customers'),

    # 私户信息展示
    url(r'^mycustomers/', views.customers, name='mycustomers'),


    #添加
    url(r'^add/', views.add, name='add'),

    #编辑
    url(r'^edit/(\d+)/', views.edit, name='edit'),

    #删除
    url(r'^delete/(\d+)/', views.delete, name='delete'),

    #搜索
    url(r'^se/', views.se, name='se'),

    url(r'^se_follow/', views.se_follow, name='se_follow'),


    #批量操作

    url(r'^batch/', views.batch, name='batch'),

    # 跟进批量操作

    url(r'^batch_follow/', views.batch_follow, name='batch_follow'),

    #跟进记录

    url(r'^follow/', views.follow, name='follow'),
    #添加跟进记录

    url(r'^add_follow/', views.add_follow, name='add_follow'),
    #编辑跟进记录

    url(r'^edit_follow/(\d+)/', views.edit_follow, name='edit_follow'),
    #删除跟进记录

    url(r'^delete_follow/(\d+)/', views.delete_follow, name='delete_follow'),


    #班级学习记录
    url(r'^class_record/',views.ClassRecordView.as_view(),name='class_record'),

    # 学生详细记录
    url(r'^study_decord/(\d+)/',views.StudyRecordDetialView.as_view(),name='study_decord'),

    #添加班级记录
    url(r'^add_record/',views.ClassRecordView_add.as_view(),name='add_record'),
    #编辑班级记录
    url(r'^edit_record/(\d+)/',views.ClassRecordView_edit.as_view(),name='edit_record'),

    #删除班级记录
    url(r'^del_record/(\d+)/',views.ClassRecordView_del.as_view(),name='del_record'),

    #权限分配
    url(r'^menu_list/',views.menu_list,name='menu_list'),


]



