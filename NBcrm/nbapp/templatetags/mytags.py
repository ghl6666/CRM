from django import template

import re
register=template.Library()

@register.inclusion_tag('left_menu.html')
def menu(request):
    path=request.path
    permisson_menu_dict=request.session['permisson_menu_dict']
    for key,per in permisson_menu_dict.items():
        # print('URL',per['url'])
        per['class']='hide'
        for child in per['children']:
            # if re.search('^{}$'.format(child['url']),path):

            if child['pk']==request.show_id:
                per['class']=''
                child['class']='active'


    return {'menu_dict':permisson_menu_dict}

@register.filter
def haspermission(url,request):

    permission_list=request.session['permisson_list']
    for i in permission_list:
        reg='^%s$'%i['url']
        ret=re.search(reg,url)
        if ret:
            return True
    return False



