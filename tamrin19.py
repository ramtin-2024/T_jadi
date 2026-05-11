# در این تمرین، شما باید یک تابع به نام 
# pick_evens(*args)
# بنویسید که یک سری عدد دریافت کند و فقط اعداد زوج را برگرداند.
# وظیفه شما:
# تابعی به نام 
# pick_evens(*args) 
# بنویسید که:تعداد نامحدودی عدد به عنوان ورودی دریافت کند.
# فقط اعداد زوج را در قالب یک لیست برگرداند.
# اگر هیچ عدد زوجی وجود نداشت، لیست خالی [] را برگرداند.


def pick_evens(*args):
    Even_numbers = []
    for number in args :
        if number %2 == 0:
            Even_numbers.append(number)
    return Even_numbers

input_string = input("Please enter numbers with spaces:")
if input_string.strip() == "":
    number = []
else:
    try:
        number = list(map(int, input_string.split()))
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
        number = [] 
print(pick_evens(*number))    