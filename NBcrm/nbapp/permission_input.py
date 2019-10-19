from nbapp import models


def initial_session(request, user_obj):
    permissions = models.Permission.objects.filter(role__userinfo__username=user_obj).values('title', 'url', 'pk', 'menu_id',
                                                                                         'menu__title', 'menu__icon',
                                                                                     'menu__pk', 'pid').distinct()

    # print(permissions)
    # print(permissions)

    '''  源数据
        [
            {
                'title': '客户列表',
                'url': '/customer/list/',
                'pk': 1,
                'menu_id': 1,
                'menu__title': '信息管理',
                'menu__icon': 'fa fa-connectdevelop',
                'menu__pk': 1
            }, {
                'title': '添加客户',
                'url': '/customer/add/',
                'pk': 2,
                'menu_id': None,
                'menu__title': None,
                'menu__icon': None,
                'menu__pk': None
            }
        ]

    '''
    '''目标数据结构
        {
            1:{  # 1--menu_id
                'title':'..',
                'icon':'xx',
                children:[
                    {'title':'二级','url':'xx'},
                    {'title':'二级','url':'xx'},
                ]
            },
            2:{  # 2--menu_id
                'title':'..',
                'icon':'xx',
                children:[
                    {'title':'二级','url':'xx'},
                    {'title':'二级','url':'xx'},
                ]
            }

        }

    '''

    permisson_list = []
    # permisson_menu_list = []
    permisson_menu_dict = {}
    for item in permissions:
        # permisson_list = [i.url for i in permissions]
        # permisson_list.append(item['url'])
        permisson_list.append({
            'pk': item['pk'],
            'url': item['url'],
            'pid': item['pid'],
            'title':item['title']
        })
        # 往session中注入菜单栏的数据

        if item['menu_id']:

            if item['menu_id'] in permisson_menu_dict:
                permisson_menu_dict[item['menu__pk']]['children'].append(
                    {'pk': item['pk'], 'title': item['title'], 'url': item['url'],'pid':item['pid']}
                )

            else:

                permisson_menu_dict[item['menu__pk']] = {
                    'title': item['menu__title'],
                    'icon': item['menu__icon'],
                    'children': [
                        {'pk': item['pk'], 'title': item['title'], 'url': item['url'],'pid':item['pid']}
                    ],
                }

            '''
            1:{  # 1--menu_id
                'title':'..',
                'icon':'xx',
                children:[
                    {'title':'二级','url':'xx'},

                ]
            },'''

            # permisson_menu_list.append({
            #     'title':item.title,
            #     'url':item.url,
            #     'icon':item.icon,
            # })

    '''
        [
            {'title':'客户列表','url':'/customer/list/','icon':'fa-..'},
            {'title':'客户列表','url':'/customer/list/','icon':'fa-..'},
        ]

    '''
    # print('permisson_menu_dict',permisson_menu_dict)
    # print(permisson_list)
    request.session['permisson_list'] = permisson_list
    # request.session['permisson_menu_list'] = permisson_menu_list
    request.session['permisson_menu_dict'] = permisson_menu_dict
    # print(permisson_menu_dict)
    # print(permisson_list)





