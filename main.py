# ValueError: malformed node or string in Python

import ast

a_str = '''{
    "first": "bobby",
    "last": "hadz"
}'''

result = ast.literal_eval(a_str)


print(result)  # 👉️ {'first': 'bobby', 'last': 'hadz'}
print(type(result))  # 👉️ <class 'dict'>