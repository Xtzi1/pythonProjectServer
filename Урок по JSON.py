# Запись в json объекта python:
#
# import json
#
# template = {
#     'firstname': 'Иван',
#     'lastname': 'Иванов',
#     'isAlive': True,
#     'age': 32,
#     'address': {
#         'streetAddress': 'Нейбута 32',
#         'city': 'Владивосток',
#         'state': '',
#         'postalcode': ''
#     },
#     'phoneNumbers': [
#         {
#             'type': 'mob',
#             'number': '123-333-4455'
#         },
#         {
#             'type': 'office',
#             'number': '123 111-4567'
#         }
#     ],
#     'children': [],
#     'spouse': None
# }
#
# with open('to_json_example.json', 'w',  encoding='utf8') as f:
#     json.dump(template, f, ensure_ascii=False, indent=4)
#
# with open('to_json_example.json', encoding='utf8') as f:
#     print(f.read())

# Открываем на чтение json:
#
# import json
#
# with open('to_json_example.json', encoding='utf8') as f:
#     strfile = f.read()
#     templates = json.loads(strfile)
#
# print(templates)
# print(type(templates))

# AGAIN:

import json

template = {
    'firstname': 'Иван',
    'lastname': 'Иванов',
    'isAlive': True,
    'age': 32,
    'address': {
        'streetAddress': 'Нейбута 32',
        'city': 'Владивосток',
        'state': '',
        'postalcode': ''
    },
    'phoneNumbers': [
        {
            'type': 'mob',
            'number': '123-333-4455'
        },
        {
            'type': 'office',
            'number': '123 111-4567'
        }
    ],
    'children': [],
    'spouse': None
}

with open('AGAINJSON.json', 'w', encoding='utf8') as f:
    json.dump(template, f, ensure_ascii=False, indent=4)

with open('AGAINJSON.json', 'r', encoding='utf8') as f:
    print(f.read())

