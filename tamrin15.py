# در این تمرین، شما باید یک تابع بنویسید که دو عدد صحیح را دریافت کند و مجموع مربع‌های آن‌ها را محاسبه کند.
# وظیفه شما:
# تابعی به نام 
# sum_of_squares 
# بنویسید که دو عدد صحیح دریافت کند و مقدار مجموع مربع‌های آن دو عدد را برگرداند.
# فرمول محاسبه:
# sum_of_squares(a,b)=a**2+b**2


def sum_of_squares(X,Y):
    result = X ** 2 + Y ** 2
    return result

X = int (input("Enter number 1 :"))
Y = int (input("Enter number 2 :"))

print(sum_of_squares(X,Y))
