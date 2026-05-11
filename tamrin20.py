# بلندترین ساختمان در افق 
# شما باید یک تابع به نام 
# skyline(*args)
#  بنویسید که ارتفاع تعدادی ساختمان را دریافت کند و بلندترین ارتفاع را برگرداند.
# وظیفه شما:
# تابعی به نام 
# skyline(*args) 
# بنویسید که:تعدادی عدد صحیح (ارتفاع ساختمان‌ها) را به عنوان ورودی دریافت کند.
# بیشترین عدد را از بین آن‌ها پیدا کند و برگرداند.
# اگر هیچ عددی وارد نشد، مقدار 0 را برگرداند.



def skyline(*args):
    if not args:
        return 0
    max_height = args [0]
    for num in args:
        if num > max_height:
            max_height = num 
    return max_height

number = list(map(int,input("Please enter numbers with spaces:").split()))  

print(skyline(*number))
