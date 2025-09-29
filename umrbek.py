import datetime
# Foydalanuvchidan tug‘ilgan yilini olish
birth_year = int(input("Tug‘ilgan yilingizni kiriting: "))
# Hozirgi yilni olish
current_year = datetime.date.today().year
# Yoshni hisoblash
age = current_year - birth_year
print(f"Siz {age} yoshdasiz.")


import datetime
date_input = input("Sanani kiriting (YYYY-MM-DD): ")
date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")
week_day = date_obj.strftime("%A") # Hafta kunini olish
print(f"{date_input} - {week_day} kuni bo‘lgan.")
