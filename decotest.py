def my_deco(func):
    def func_wrapper():
        print("code before")
        func()
        print("code after")
    return func_wrapper

def func_test():
    print("Hey, I am func test")

test = my_deco(func_test)
test()       