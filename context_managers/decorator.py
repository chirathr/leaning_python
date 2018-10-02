from contextlib import contextmanager

@contextmanager
def simple_context_manager(name):
    # code for __enter__()
    print (name)
    yield
    # code for __exit__()
    print(name)


with simple_context_manager("Hi") as context_manager:
    print("Hello")

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    yield file
    file.close()


with open_file("abc.txt", 'w+') as file:
    file.write("Hello")
