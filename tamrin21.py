# شرح مسئله:
# یک باغ‌وحش قصد دارد یک سیستم مدیریت حیوانات ایجاد کند. شما باید با استفاده از برنامه‌نویسی شی‌گرا 
# (OOP) 
# در پایتون، این سیستم را طراحی کنید.
# ۱. مقدمه بر شی‌گرایی (OOP Introduction)
# وظیفه شما:
# یک کلاس به نام Animal تعریف کنید که ویژگی‌های زیر را داشته باشد:
#     name (نام حیوان)
#     species (گونه حیوان)
#     age (سن حیوان)
#     sound (صدای حیوان)
# سپس یک نمونه از این کلاس برای یک "شیر" ایجاد کرده و مشخصات آن را چاپ کنید.
# ۲. ویژگی‌ها و کلاس‌ها 
# (Attributes and Class Keyword)
# وظیفه شما:
# متد 
# make_sound() 
# را به کلاس 
# Animal
#  اضافه کنید که صدای حیوان را چاپ کند.
# ۳. ویژگی‌های کلاس و متدها 
# (Class Object Attributes and Methods)
# وظیفه شما:
# یک ویژگی کلاس 
# (zoo_name) 
# اضافه کنید که نام باغ‌وحش را مشخص کند. همچنین، یک متد 
# info()
#  تعریف کنید که مشخصات حیوان را چاپ کند.
# ۴. ارث‌بری و چندریختی 
# (Inheritance and Polymorphism)
# وظیفه شما:
# یک کلاس جدید به نام Bird از Animal بسازید که یک ویژگی جدید 
# wing_span
#  (اندازه بال) داشته باشد.
# همچنین متد 
# make_sound() 
# را بازنویسی کنید تا صدای پرندگان متفاوت باشد.
# ۵. متدهای جادویی 
# (Magic/Dunder Methods)
# وظیفه شما:
# متد 
# __str__ 
# را در کلاس 
# Animal 
# پیاده‌سازی کنید تا وقتی شیء را چاپ می‌کنید، مشخصات حیوان نمایش داده شود.


class Animal:
    zoo_name = "Mamdali"
    def __init__(self,name,species,age,sound):
        self.name = name 
        self.species = species
        self.age = age
        self.sound = sound

    def  make_sound(self):
        print(f"sound:{self.sound}")     

    def info (self):
        print(f"name:{self.name} , species:{self.species} , age:{self.age} ") 

    def __str__ (self):
        return f"name:{self.name} , species:{self.species} , age:{self.age} , sound:{self.sound} "


class Bird(Animal):
    def __init__(self,name,species,age,sound,wing_span):
        super().__init__(name,species,age,sound)
        self.wing_span = wing_span
    
    def  make_sound(self):
        print(f"Bird_sound:{self.sound}")

   

l = Animal("lion", "iran" , 5 , "woooooaaaa")
B = Bird("eagle", "U.S.A" , 3 , "qiiiiiizh",12)
print(l)
print(B)
