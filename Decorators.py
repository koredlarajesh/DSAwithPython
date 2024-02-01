def test():
    return 4+5
print(test())

#===========================================

def test():
    print("start of the function")
    print(4+4)
    print("end of the function")
test()
#================================================

def deco(func):
    def inner_deco():
        print("start of the function")
        func()
        print("end of the function")
    return inner_deco

@deco
def test1():
    print(4+5)

test1()

# ==========================================================


import time
def timer_test(func):
    def timer_test_inner():
        start=time.time()
        func()
        end=time.time()
        print(end-start)
    return timer_test_inner
@timer_test
def test_time():
    print( 5+4 )
test_time()

