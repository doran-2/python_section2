import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def function1():
        print("function1 has been called.")

    def function2(self):
        print(id(self))
        print("function2 has been called.")

f = SelfTest()

#print(dir(f))
print(id(f))

f.function2()
SelfTest.function1()
