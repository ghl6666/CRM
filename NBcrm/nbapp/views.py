import random
import os
from NBcrm import settings
from nbapp import form
from django.shortcuts import render,HttpResponse,redirect
from nbapp import models
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from nbapp import permission_input
from django.views import View
from nbapp import form
# Create your views here.

#注册
def register(request):
    if request.method == 'GET':
        form_obj = form.UserForm()

        return render(request,'register.html',{'form_obj':form_obj})
    else:
        form_obj = form.UserForm(request.POST)
        if form_obj.is_valid():
            data = form_obj.cleaned_data
            data.pop('r_password')
            models.UserInfo.objects.create_user(**data)

            # auth.login(request,user_obj) 注册完之后可以自动进行登录

            return redirect('login')
        else:
            return render(request, 'register.html', {'form_obj': form_obj})

#登录
def login(request):
    '''
    响应的状态码:
    成功:1000
    验证码失败:1001
    用户名密码失败:1002
    :param request:
    :return:
    '''
    response_msg = {'code':None,'msg':None}
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        valid_bode = request.POST.get('valid_code')
        #1 首先验证验证码是否正确
        if valid_bode.upper() == request.session.get('valid_str').upper():
             # 2 验证用户名和密码是不是存在
            user_obj = auth.authenticate(username=username,password=password)
            # user_obj=models.UserInfo.objects.filter(username=username,password=password).first()
            print(user_obj)
        #用户名密码正确
            if user_obj:
                # 3 保存session
                auth.login(request,user_obj)
                # request.session['user']=user_obj.username
                print(user_obj.username)


                # permissions=models.Permission.objects.filter(role__userinfo__username=user_obj.username).values('menu__icon','menu__title','menu__pk','title','menu_id',)
                permission_input.initial_session(request,user_obj)



                # print(permissions)
                # permission_list=[]
                # permission_menu_list={}
                # for per in permissions.distinct():
                #     permission_list.append(per)
                #
                #
                #
                # # permission_list=[i.url for i in permissions]
                # print(permission_list)
                # request.session['permission_list']=permission_list
                #
                # permission_menu_list=[]
                # for per in permission_list:
                #     if per['is_menus']:
                #         permission_menu_list.append(per)
                #
                # request.session['permission_menu_list'] = permission_menu_list
                response_msg['code'] = 1000

                response_msg['msg'] = '登录成功!'
                # return redirect('index.html')
            else:
                response_msg['code'] = 1002
                response_msg['msg'] = '用户名或者密码输入有误!'

        #验证码失败报错
        else:
            response_msg['code'] = 1001
            response_msg['msg'] = '验证码输入有误!'
        print(response_msg['code'])

        return JsonResponse(response_msg)

#注销
def logout(request):
    auth.logout(request)
    return redirect('login')


def get_valid_img(request):

    def get_random_color():
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    from PIL import Image, ImageDraw, ImageFont
    img_obj = Image.new('RGB', (200, 34), get_random_color())
    draw_obj = ImageDraw.Draw(img_obj)
    font_path = os.path.join(settings.BASE_DIR,'statics/font/arial.ttf')
    font_obj = ImageFont.truetype(font_path,16)
    sum_str = ''
    for i in range(6):
        a = random.choice([str(random.randint(0,9)), chr(random.randint(97,122)), chr(random.randint(65,90))])  #4  a  5  D  6  S
        sum_str += a
    print(sum_str)
    draw_obj.text((64,10),sum_str,fill=get_random_color(),font=font_obj)

    width=200
    height=34
    for i in range(5):
        x1=random.randint(0,width)
        x2=random.randint(0,width)
        y1=random.randint(0,height)
        y2=random.randint(0,height)
        draw_obj.line((x1,y1,x2,y2),fill=get_random_color())
    # # 添加噪点
    for i in range(10):
        #这是添加点，50个点
        draw_obj.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        #下面是添加很小的弧线，看上去类似于一个点，50个小弧线
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw_obj.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    from io import BytesIO
    f = BytesIO()
    img_obj.save(f,'png')
    data = f.getvalue()

    #验证码对应的数据保存到session里面
    request.session['valid_str'] = sum_str

    return HttpResponse(data)


# 如果记录用户想去的路径
# @login_required
# def shopping(request):
#     path = request.path
#     # return redirect('/login/'+'?next='+path)
#     # request.GET.get('next')
#     # return HttpResponse('shopping')

#这是一个简答的路由跳转测试
# @login_required
# def shopping(request):
#     return HttpResponse('shopping')


#首页
# @login_required
def index(request):
    # return render(request,'index.html')
    # print('>>>>>>>',request.session['user'])
    # print('>>>>>',request.user)
    return render(request,'index.html')

#展示公户和私户所有客户信息
def customers(request):
    #批量操作
    selected_id = request.POST.getlist('selected_id')
    if selected_id:
        batch(request)


    current_page_num=request.GET.get('page',1)
    if request.path==reverse('customers'):

        flag=0
        all_customers = models.Customer.objects.filter(consultant__isnull=True)
    else:
        flag=1
        all_customers=models.Customer.objects.filter(consultant=request.user)
    per_page_counts=5  #每页5条数据
    page_number=11  #显示的页码数
    total_count=all_customers.count() #数据的总数

    page_obj=page.PageNation(request.path,current_page_num,total_count,per_page_counts,page_number)
    all_customers=all_customers.order_by('-pk')[page_obj.start_num:page_obj.end_num]
    ret_html=page_obj.page_html()


    return render(request,'customers.html',{'all_customers':all_customers,'ret_html':ret_html,'flag':flag})

#展示私有客户信息
# def mycustomers(request):
#     all_customers=models.Customer.objects.filter(consultant=request.user)
#         # if my_customers:
#     return render(request,'mycustomers.html',{'all_customers':all_customers})
#     # else:
    #     return render(request,'customers.html')




# 分页
from nbapp import page
def test(request):
    current_page_num = request.GET.get('page',1)
    per_page_counts = 10 #每页显示10条
    page_number = 5  #总共显示5个页码



    all_data = models.Customer.objects.all()
    total_count = all_data.count()

    ret_html,start_num,end_num = page.pagenation(request.path, current_page_num,total_count,per_page_counts,page_number)

    all_data = models.Customer.objects.all()[start_num:end_num]
    all_data = models.Customer.objects.filter()

    return render(request,'test.html',{'all_data':all_data,'ret_html':ret_html})



def add(request):
    if request.method=="GET":
        form_obj=form.Costomer_Form()
        return render(request,'add.html',{'form_obj':form_obj})

    else:
        data=request.POST
        form_obj=form.Costomer_Form(data)
        if form_obj.is_valid():
            form_obj.save()

            return redirect('customers')

        else:

            return render(request,'add.html',{'form_obj':form_obj})

# 编辑

def edit(request,pk):
    if request.method=="GET":

        co_obj=models.Customer.objects.filter(pk=pk).first()
        form_obj=form.Costomer_Form(instance=co_obj)

        return render(request,'edit.html',{'form_obj':form_obj},{'pk':pk})

    else:
        co_obj=models.Customer.objects.filter(pk=pk).first()
        form_obj=form.Costomer_Form(request.POST,instance=co_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('customers')
        else:
            return render(request,'edit.html',{'form_obj':form_obj})



        #删除
def delete(request,pk):
    if request.method=='GET':
        models.Customer.objects.filter(pk=pk).delete()
        return redirect('customers')


# 搜索
def se(request):

    wd = request.GET.get('wd', '')
    condition = request.GET.get('condition', '')
    print(wd)  # 小
    print(condition + '__contains')  # name
    # condition = condition + '__contains'
    # condition: name
    current_page_num = request.GET.get('page', 1)

    # get:condition=qq&wd=1&page=2

    # <QueryDict: {'condition': ['qq'], 'wd': ['1'], 'page': ['2']}> #condition=qq&wd=1&page=2

    if wd:
        # all_data = models.Customer.objects.filter(Q(qq__contains=wd)|Q(name__contains=wd))
        q = Q()
        # q.connector = 'or'  # 指定条件连接符号
        q.children.append((condition, wd))  # 默认是and的关系
        # q.children.append(('qq_name__contains'))

        # all_data = models.Customer.objects.filter(name__contains=wd)

        all_data = models.Customer.objects.filter(q)
        if not all_data:
            return render(request,'customers.html',{'flag':'找不到相关的内容'})

    else:
        all_data = models.Customer.objects.all()

    per_page_counts = 10  # 每页显示10条
    page_number = 7  # 总共显示5个页码

    total_count = all_data.count()

    # ret_html,start_num,end_num = page.pagenation(request.path, current_page_num,total_count,per_page_counts,page_number)
    p_obj = page.PageNation(request.path, current_page_num, total_count, request, per_page_counts, page_number)

    ret_html = p_obj.page_html()

    all_customers = all_data[p_obj.start_num:p_obj.end_num]

    return render(request, 'customers.html', {'all_customers': all_customers, 'ret_html': ret_html})


import sys
#从customer调用批量操作方法
def batch(request):
    print(request.path)

    if request.method=='POST':
        selected_id=request.POST.getlist('selected_id')
        action=request.POST.get('action')


        if hasattr(sys.modules[__name__],action):
            print('##########')

            getattr(sys.modules[__name__],action)(request,selected_id)
            print('2222222222')
            # return redirect(request.path)

    return redirect(request.path)

# 批量删除
def batch_delete(request,li):
    models.Customer.objects.filter(pk__in=li).delete()


#批量更新
def batch_update(request,li):

    for i  in li:
        if models.Customer.objects.filter(pk=int(i)).first().status=='未报名':
            models.Customer.objects.filter(pk=int(i)).update(status='已报名')

        else:
            models.Customer.objects.filter(pk=int(i)).update(status='未报名')

#批量公户转私户
def reverse_gs(request,li):
    name_li=[]
    # li=request.POST.getlist('selected_id')
    for i in li:
        obj=models.Customer.objects.filter(pk=i).filter(consultant__isnull=True)
        if obj:
            models.Customer.objects.filter(pk=i).update(consultant=request.user)
        else:

            name=models.Customer.objects.filter(pk=i).first().name
            name_li.append(name)




    return render(request,'customers.html',{'name_li':name_li})
#批量私户转公户
def reverse_sg(request,li):

    models.Customer.objects.filter(pk__in=li).update(consultant=None)


def follow(request):
    if request.method=='GET':
        current_page_num = request.GET.get('page', 1)
        all_customers = models.ConsultRecord.objects.filter(consultant=request.user)
        per_page_counts = 5  # 每页5条数据
        page_number = 11  # 显示的页码数
        total_count = all_customers.count()  # 数据的总数

        page_obj = page.PageNation(request.path, current_page_num, total_count, per_page_counts, page_number)
        form_obj = all_customers.order_by('-pk')[page_obj.start_num:page_obj.end_num]
        ret_html = page_obj.page_html()
        flag=2
        return render(request,'follow.html',{'form_obj':form_obj},{'ret_html':ret_html,'flag':flag},)

        # follow_obj=models.Customer.objects.filter(consultant=request.user)


# 跟进记录添加
def add_follow(request,pk=None):
    if request.method=='GET':

        form_obj=form.Costomer_Follow(request)
        return render(request,'add_follow.html',{'form_obj':form_obj})
    else:
        form_obj=form.Costomer_Follow(request,request.POST)
        if form_obj.is_valid():
            data=form_obj.cleaned_data
            models.ConsultRecord.objects.create(**data)

            return redirect('follow')

#跟进记录编辑
def edit_follow(request,pk=None):
    if request.method=='GET':
        form_obj=models.ConsultRecord.objects.filter(pk=pk).first()
        form_obj=form.Costomer_Follow(request,instance=form_obj)
        return render(request,'add_follow.html',{'form_obj':form_obj})
    else:
        form_obj=models.ConsultRecord.objects.filter(pk=pk).first()
        form_obj=form.Costomer_Follow(request,request.POST,instance=form_obj)
        if form_obj.is_valid():
            form_obj.save()
        return redirect('follow')

#跟进记录删除
def delete_follow(request,pk=None):
    if request.method=="GET":
        models.ConsultRecord.objects.filter(pk=pk).delete()
        return redirect('follow')



def batch_follow(request):
    if request.method=='POST':
        selected_id=request.POST.getlist('selected_id')
        action=request.POST.get('action')


        if hasattr(sys.modules[__name__],action):

            getattr(sys.modules[__name__],action)(request,selected_id)

            return redirect('follow')
# 跟进批量删除
def batch_delete_follow(request,li):
    models.ConsultRecord.objects.filter(pk__in=li).delete()


#跟进批量更新
def batch_update_follow(request,li):

    for i  in li:
        if models.ConsultRecord.objects.filter(pk=int(i)).first().status=='未报名':
            models.ConsultRecord.objects.filter(pk=int(i)).update(status='已报名')

        else:
            models.ConsultRecord.objects.filter(pk=int(i)).update(status='未报名')

# 搜索
def se_follow(request):
    wd = request.GET.get('wd', '')
    condition = request.GET.get('condition', '')
    print(wd)  # 小
    print(condition + '__contains')  # name
    # condition = condition + '__contains'
    # condition: name
    current_page_num = request.GET.get('page', 1)

    # get:condition=qq&wd=1&page=2

    # <QueryDict: {'condition': ['qq'], 'wd': ['1'], 'page': ['2']}> #condition=qq&wd=1&page=2

    if wd:
        # all_data = models.Customer.objects.filter(Q(qq__contains=wd)|Q(name__contains=wd))
        q = Q()
        # q.connector = 'or'  # 指定条件连接符号
        q.children.append((condition, wd))  # 默认是and的关系
        # q.children.append(('qq_name__contains'))

        # all_data = models.Customer.objects.filter(name__contains=wd)

        all_data = models.ConsultRecord.objects.filter(q)
        if not all_data:
            return render(request,'follow.html',{'flag':'找不到相关的内容'})

    else:
        all_data = models.ConsultRecord.objects.all()

    per_page_counts = 10  # 每页显示10条
    page_number = 7  # 总共显示5个页码

    total_count = all_data.count()

    # ret_html,start_num,end_num = page.pagenation(request.path, current_page_num,total_count,per_page_counts,page_number)
    p_obj = page.PageNation(request.path, current_page_num, total_count, request, per_page_counts, page_number)

    ret_html = p_obj.page_html()

    form_obj = all_data[p_obj.start_num:p_obj.end_num]

    return render(request, 'follow.html', {'form_obj': form_obj, 'ret_html': ret_html})



#?wd=郭海龙&condition=name__contains
#?wd=123&condition=customer__contains


class ClassRecordView(View):

    def get(self,request):


        all_obj=models.ClassStudyRecord.objects.all()
        return render(request,'student/classrecord.html',{'all_obj':all_obj})

    def post(self,request):

        action=request.POST.get('action')
        selected_id=request.POST.getlist('selected_id')
        if hasattr(self,action):

            getattr(self,action)(selected_id)
        return self.get(request)

    def batch_create(self,selected_id):
        for course_record_id in selected_id:
            all_students=models.ClassStudyRecord.objects.get(pk=course_record_id).class_obj.students.all()
            l1=[]
            for student in all_students:
                obj=models.StudentStudyRecord(
                    student=student,
                    classstudyrecord_id=course_record_id,

                )

                l1.append(obj)
            models.StudentStudyRecord.objects.bulk_create(l1)

class ClassRecordView_add(View):
    def get(self,request):
        form_obj=form.ClassRecordForm
        return render(request,'student/add_record.html',{'form_obj':form_obj})

    def post(self,request):
        data=request.POST


        form_obj=form.ClassRecordForm(data)
        if form_obj.is_valid():
            form_obj.save()

        return redirect(reverse('class_record'))

class ClassRecordView_del(View):
    def get(self,request,del_id):
        models.ClassStudyRecord.objects.filter(pk=del_id).delete()

        return redirect(reverse('class_record'))

class ClassRecordView_edit(View):

    def get(self,request,edit_id=None):
        obj=models.ClassStudyRecord.objects.filter(pk=edit_id).first()
        # print('>>>>',form_obj)
        form_obj=form.ClassRecordForm(instance=obj)
        return render(request,'student/add_record.html',{'form_obj':form_obj})


    def post(self,request,edit_id=None):
        # print(edit_id)
        # print(self.request)
        obj = models.ClassStudyRecord.objects.filter(pk=edit_id).first()
        data=request.POST
        form_obj=form.ClassRecordForm(data,instance=obj)
        if form_obj.is_valid():
            form_obj.save()

        return redirect(reverse('class_record'))






class StudyRecordDetailView2(View):
    def get(self,request,class_record_id):
        #查询对应的班级记录对象

        class_obj=models.ClassStudyRecord.objects.filter(pk=class_record_id).first()
        #查询对应班级的所有学生的学习信息
        all_students=models.StudentStudyRecord.objects.filter(classstudyrecord__pk=class_record_id).all()


        #
        score_choices=models.StudentStudyRecord.score_choices
        return render(request,'student/study_record_detail.html',{'all_sudents':all_students,'class_obj':class_obj,'score_choices':score_choices})

    def post(self,request,class_record_id):
        data=request.POST
        #<QueryDict: {'csrfmiddlewaretoken': ['sLjYEZfUB1aZHQmmWI0fPymfhfCPbH0QxYZaumYoPCnqMcTNtPnHWz1NE9P2xo6C'],
        # 'score_5': ['100'],
        # 'homework_note_5': [''],
        # 'score_6': ['100'],
        # 'homework_note_6': ['']}>
        print(data)

        data_dict={}
        for key,val in data.items():
            if key=='csrfmiddlewaretoken':
                continue

            field,pk=key.rsplit('_',1)
            if pk in data_dict:
                data_dict[pk][field]=val
            else:
                data_dict[pk]={
                    field:val
                }

        print(data_dict)

        for spk,sdata in data_dict.items():
            models.StudentStudyRecord.objects.filter(**{'pk':spk}).update(**sdata)

        return redirect(reverse('study_decord',args=(class_record_id)))



# formset
from django.forms.models import modelformset_factory  #通过forms中的models引入formset_factory
from django import forms
#modelfrom
class StudentRecordDetailModelForm(forms.ModelForm): #先创建一个modelfoem类给formset备用
    class Meta:
        model=models.StudentStudyRecord
        fields=['score','homework_note']

class StudyRecordDetialView(View):   #创建学系信息表
    def get(self,request,class_record_id):
        class_record_id=models.ClassStudyRecord.objects.get(pk=class_record_id)
        all_study_record=models.StudentStudyRecord.objects.filter(
            classstudyrecord=class_record_id,
        )
        form_set_obj=modelformset_factory(model=models.StudentStudyRecord,form=StudentRecordDetailModelForm,extra=0)
        formset=form_set_obj(queryset=all_study_record)

        return render(request,'student/study_record_detail.html',{'formset':formset})

    def post(self,request,class_record_id):
        # class_record_obj=models.ClassStudyRecord.objects.get(pk=class_record_id
        #                                                     )
        form_set_obj=modelformset_factory(model=models.StudentStudyRecord,form=StudentRecordDetailModelForm,extra=0)
        formset=form_set_obj(request.POST) #将接收到的数据进行实例化创建一个formset对象
        if formset.is_valid():
            formset.save()

        else:
            print(formset.errors)

        return redirect(reverse('study_decord',args=(class_record_id,)))


def menu_list(request):

    menu_obj=models.Menu.objects.all()
    role_obj=models.Role.objects.all()
    per_obj=models.Permission.objects.all()

    return render(request,'permission/menu.html',{'menu_obj':menu_obj,'role_obj':role_obj,'per_obj':per_obj})

