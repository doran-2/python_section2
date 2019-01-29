import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __del__(self):
        print("delete!")   

    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("=====================")
        print("Name: ",self.name)
        print("Phone: ",self.phone)

user1 = UserInfo("Do","010-2517-9429")
user2 = UserInfo("Park","010-4427-4529")

print(id(user1))
print(id(user2))

#user1.set_info("Do","010-2517-9429")
#user2.set_info("Park","010-4427-4529")

user1.print_info()
user2.print_info()


print(user1.__dict__)
print(user2.__dict__)

print(user1.name, ',', user1.phone)
print(user2.name, ',', user2.phone)
