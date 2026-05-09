# در این تمرین، شما باید یک تابع به نام 
# is_greater(a, b) 
# تعریف کنید که بررسی کند آیا عدد a بزرگ‌تر از b است یا خیر.
# وظیفه شما:
# یک تابع به نام 
# is_greater(a, b)
#  تعریف کنید که:
#دو عدد صحیح a و b را به عنوان ورودی دریافت کند.
#بررسی کند که آیا a از b بزرگ‌تر است یا نه.
#مقدار 
# True
# را برگرداند اگر a > b باشد.
#مقدار 
# False 
# را برگرداند اگر a ≤ b باشد.
#مقدار باید برگردانده (return) شود و نه مستقیماً چاپ شود.


def  is_greater(a, b):
    if a > b :
        return True
    elif a <= b :
        return False    

a = int (input("Enter number 1 :"))
b = int (input("Enter number 2 :"))

print(is_greater(a, b))