import re
from django.shortcuts import HttpResponse,redirect,render
from django.utils.deprecation import MiddlewareMixin
from nbapp import models
class PermissionMiddleWare(MiddlewareMixin):
    def process_request(self,request):


        for i in ['/login/','/admin/.*','get_valid_img/',]:
            ret=re.search(i,request.path)
            # print(ret)
            if ret:
                return None

        user=request.session.get('_auth_user_id')
        # print('middle',user)
        if not user:
            return redirect('login')

        # print('------',request.path)
        # print(request.session['permission_list'])

        request.bread_crumb=[{
            'title':'首页',
            'url':'/index/',
            'pid':4,

        }]
        try:

            for item in request.session['permisson_list']:

                reg='^%s$'%item['url']    #缺了一个斜线
                res=request.path
                # print(res)
                # print(item['url'])
                # print('000000000',reg)
                ret=re.search(reg,res)



                if ret:
                    request.show_id=item['pid']  #
                    if item['pid']==item['pk']:

                        request.bread_crumb.append({
                            'title':item['title'],
                            'url':request.path,
                            'pid':item['pid']
                        })

                    else:
                        print(item['pid'])
                        obj=models.Permission.objects.filter(pk=item['pid']).first()
                        print(obj)
                        l1=[
                            {
                            'title':obj.title,
                            'url':obj.url,
                                'pid':item['pid']

                        },
                            {
                                'title':item['title'],
                                'url':request.path,
                                'pid':item['pid']

                            }

                        ]

                        request.bread_crumb.extend(l1)
                    print(request.bread_crumb)

                    # print('>>>>----',item)
                    # print('>>>>----',ret)
                    return None

        except:
            return None

        else:
            return HttpResponse('权限禁止！！')