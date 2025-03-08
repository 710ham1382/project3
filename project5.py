usernames = []

while True:
    username = input("لطفا نام کاربری را وارد کنید (برای پایان -1 را وارد کنید): ")

    if username == "-1":
        break

    # ذخیره نام کاربری در لیست
    usernames.append(username)

print("نام‌های کاربری وارد شده:")
for username in usernames:
    print(username)