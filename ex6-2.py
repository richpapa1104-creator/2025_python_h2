username = "admin"
password = "20111104"
is_active = True

if username == "admin" and password =="20111104" and is_active:
    print("登入成功!")
elif not is_active:
    print("帳號已被停用")
else:
    print("使用者名稱或密碼錯誤")
