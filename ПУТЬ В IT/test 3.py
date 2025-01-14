symbol = '1234567890qwertyuiopasdfghjklzxcvbnm_'


def email(adres):
    flag = False
    if adres.count("@") == adres.count('.') == 1:
        login, server = adres.split("@")
        flag = all(i in symbol for i in login.lower()) and all(i in (symbol + '.') for i in server.lower())
    return "ДА" if flag == True else "НЕТ"


print(email("example@[object Object]"))
print((email('example@mail.com')))
print((email('example@123.com')))
print((email('example@!mail.com')))
print(email('https://vk.com/informatika_gia'))


