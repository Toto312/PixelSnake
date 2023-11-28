class CallableClass:
    def __init__(self):
        self.my_list = [1, 2, 3]

    def __call__(self):
        return self.my_list

callable_instance = CallableClass()

result = callable_instance()

print(type(result))  # This will print <class 'list'>
