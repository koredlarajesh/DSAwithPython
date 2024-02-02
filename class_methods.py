class idrbt:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def staff_details(self):
        print(self.name,self.email)
obj_idrbt=idrbt("rajesh","raj@gmail.com")
print(obj_idrbt.name)
obj_idrbt.staff_details()

#========================================================================

class idrbt:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    @classmethod
    def details(cls,name,email):
        return cls(name,email)

    def staff_details(self):
        print(self.name,self.email)

obj_idrbt=idrbt("rajesh","raj@gmail.com")
print(obj_idrbt.name)
obj_idrbt.staff_details()
st1=idrbt.details("ravi","ravi@gmail.com")
print(st1.name)
print(st1.email)
st1.staff_details()


#idrbt1 is a class, and you('re trying to access the name '
#('attribute directly on the class. However, the name attribute is an instance '
#'attribute, not a class attribute. To access it, you need to create an instance of the class first. ))
class idrbt1:
    def __init__(self,name,email):
        self.name=name
        self.email=email
print(idrbt1.name)

class idrbt2:
    mobile_number=93939939393
    def __init__(self,name,email):
        self.name=name
        self.email=email
    @classmethod
    def change_mobile_no(cls,mobile):
        idrbt2.mobile_number=mobile
    @classmethod
    def staff_details(cls,name,email):
        return cls(name,email)
obj_1=idrbt2.staff_details("ramya","ramya@gmail.com")
print(obj_1.name)
print(obj_1.email)
print(obj_1.mobile_number)
obj_1.change_mobile_no(9092678039)
print(obj_1.mobile_number)


