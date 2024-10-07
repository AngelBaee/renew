def my_de(func):
    def def_wrapp():
        print("code before")
        func()
        print("code after")
    return def_wrapp

@my_de
def test_func():
    print("hey nerds I am func")


test_func()    
