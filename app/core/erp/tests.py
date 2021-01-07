from config.wsgi import *
from core.erp.models import *
import random

#show data
# query = Category.objects.all()
# print(query)

#save data
# t = Category(name='Azucares').save()
# t.name = 'Frutas'
# t.save()

#edition data
# try:
#     t = Type.objects.get(id=3)
#     t.name = 'Oficionista'
#     t.save()
# except Exception as e:
#     print(e)

#delete data
# t = Type.objects.get(pk=6)
# t.delete()

#obj = Type.objects.filter(name__startswith='A')
#obj = Type.objects.filter(name__startswith='A')
# obj = Type.objects.filter(name__in=['Administrador','Federal']).count()
# obj = Employee.objects.filter(type_id=1)
# for i in Type.objects.filter(name__endswith='e')[:1]:
#     print(i)

# data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
#         'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
#         'Grasas, aceite y mantequilla']
#
# for i in data:
#     cat = Category(name=i)
#     cat.save()
#     print('Guardado registro N°{}'.format(cat.id))

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
           'u','v','w','x','y','z']

for i in range(1, 100):
    name = ''.join(random.choices(letters, k=5))
    while Category.objects.filter(name=name).exists():
        name = ''.join(random.choices(letters, k=5))
    Category(name=name).save()
    print('Guardado registro {}'.format(i))