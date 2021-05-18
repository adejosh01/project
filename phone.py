print("INFINIX")
Password = (input("Enter your password: "))
if Password!=1234:
    print("Wrong password, try agian later...")
class Phone:
    """ A member tells about the function and how my device works"""
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
    def power_on(self):
        print("Loading...")
    # it require a password before you can access the phone
    def power_down(self):
        print("Phone is shutting down")

My_phone = Phone("Infinix", "Black", "2")
My_phone.power_on()
print("The name of this device is " + My_phone.name)
print("The color of this device is " + My_phone.color)
print("The size of this device is " + My_phone.size)
My_phone.power_down()

f = open("demo", "w")
print(f.write("New file is open"))
f.close()

f = open("demo", "r")
print(f.read())
f.close()

f = open("demo", "a")
print(f.write(" Wow"))
f.close()

f = open("demo", "r")
print(f.read())
f.close()