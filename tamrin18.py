# در این تمرین، شما باید یک تابع به نام 
# sum_numbers(*args)
#  تعریف کنید که بتواند هر تعداد عدد را دریافت کرده و مجموع آن‌ها را برگرداند.
# وظیفه شما:
# یک تابع به نام 
# sum_numbers(*args) 
# بنویسید که:تعداد نامحدودی از اعداد را به عنوان ورودی دریافت کند.
# مجموع این اعداد را محاسبه کرده و برگرداند 
# (return).
# اگر هیچ عددی ارسال نشود، مقدار 0 را برگرداند.


def sum_numbers(*args) :
    total = 0
    for i in args :
        total += i
    return total
    


number = list (map (int,input("Please enter numbers with spaces:").split()) )
if number == []  :
    print(0)
else:
    print(sum_numbers(*number)) 
