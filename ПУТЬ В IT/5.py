'''
• Проверять, содержит ли пароль хотя бы один символ из chars.
• Убедиться, что длина пароля не менее 8 символов.
'''

def check_password(password,chars='$%!?@#'): return len(password)>=8 and any(char in password for char in chars )

print(check_password('@Lolita1899'))
print(check_password('Lolita1899'))
print(check_password('Путь_в_IT','_'))
print(check_password('Путь_в_IT','!#$%^)([]'))

