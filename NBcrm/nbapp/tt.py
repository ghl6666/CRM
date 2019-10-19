
# a = '1.111'
# print(a.isdigit()) #True ,False
# print(a.isdecimal()) #False ,False






#
# if __name__ == "__main__":
#     import os
#     import random
#     import django
#     django.setup()
#     from nbapp import models
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NBcrm.settings")
#
#     obj_l=[]
#     l=[]
#     for i in range(1,101):
#         num_l=random.choices(range(1,10),k=9)
#         for i2 in num_l:
#             l.append(str(i2))
#         qq = ''.join(l)
#         obj_c=models.Customer(qq=qq,
#                               name=('lihua%s',i),
#                               sex=random.choice(['男','女']),
#                               source=random.choice(['官方网站','自介绍']),
#                               course=random.choice(['python','linux']),
#                               status='未报名',
#
#                               )
#         obj_l.append(obj_c)
#     models.Customer.objects.bulk_create(obj_l)

import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NBcrm.settings")
    import django
    django.setup()
    from nbapp import models
    from nbapp import views
    import random
    # l1 = []
    # for i in range(1,101):
    #     obj = models.Customer(
    #         qq = ''.join([str(i) for i in random.choices(range(1,10),k=11)]),
    #         name = 'lihua'+ str(i),
    #         sex = random.choice(['male','female']),
    #         source = random.choice(['qq','referral','website']),
    #         course=random.choice(['LinuxL','PythonFullStack']),
    #
    #     )
    #     l1.append(obj)
    # models.Customer.objects.bulk_create(l1)

