# یک دیکشنری به نام fruit_prices بسازید که شامل قیمت‌های میوه‌ها باشد.
#  قیمت‌ها به شرح زیر است:
# apple: 1500
# banana: 1000
# orange: 1200
# سپس کدی بنویسید که قیمت 
# banana را تغییر داده و به 1100 تغییر دهد و 
# apple 
# را به طور کلی حذف کند. در آخر این دیکشنری را چاپ کنید.

# درست کردن دیکشنری 
fruit_prices ={
     "apple": 1500, 
     "banana": 1000,
     "orange": 1200
}
# تغییری کلید خاصی از یک دیکشنری  
fruit_prices ["banana"]=1100
print(fruit_prices)
#حذف یک کیلید از یک دیکشنری با استفاده از 
# del
del fruit_prices ["apple"]
print(fruit_prices)