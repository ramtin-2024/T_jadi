# یک فروشگاه تخفیف‌های ویژه‌ای برای مشتریان در نظر گرفته است. قوانین تخفیف به شرح زیر است:

# اگر مبلغ خرید بیشتر از ۵۰۰۰۰ تومان باشد، تخفیف ۲۰٪ اعمال می‌شود.
# اگر مبلغ خرید بین ۲۰۰۰۰ تا ۵۰۰۰۰ تومان باشد، تخفیف ۱۰٪ اعمال می‌شود.
# اگر مبلغ خرید کمتر از ۲۰۰۰۰ تومان باشد، تخفیفی اعمال نمی‌شود.

# برنامه‌ای بنویسید که مبلغ خرید را از کاربر دریافت کند و مقدار مبلغ نهایی را نمایش دهد.



Purchase_Amount = int(input("Enter Purchase Amount please"))

if Purchase_Amount >50000 :
    discount = Purchase_Amount * 0.20
    total_payment = Purchase_Amount - discount 
    print('shoma shamel takhfif "20%" shode ed ')
    print(f"mablaq qubel pardakht:{total_payment}")

elif 20000 <  Purchase_Amount <= 50000 :
    discount = Purchase_Amount * 0.10
    total_payment = Purchase_Amount - discount 
    print('shoma shamel takhfif "10%" shode ed')
    print(f"mablaq qubel pardakht:{total_payment}")

else :
    total_payment = Purchase_Amount
    print("shoma shamel takhfif nashode ed ")
    print(f"mablaq qubel pardakht:{total_payment}")
        
