# تابعی به نام 
# is_positive 
# بنویسید که یک عدد دریافت کند و مقدار 
# True
#را برگرداند اگر عدد مثبت یا صفر باشد
#و در غیر این صورت مقدار 
# False 
# را برگرداند.
#ورودی‌ها:
# یک عدد صحیح 
# (int).  
#خروجی‌ها:
# مقدار 
# True 
# اگر مثبت و یا صفر باشد.
# مقدار 
# False
#  اگر منفی باشد.

def is_positive(number):
    if number >= 0 :
        return True
    else :
        return False

print(is_positive(-1))

#version 2
"""
def is_positive(number):
    if number >= 0 :
        return True
    else :
        return False


number = int (input("Enter number:"))

print(is_positive(number))
"""
#version 3
"""
def is_positive(number):
    return number >= 0
"""