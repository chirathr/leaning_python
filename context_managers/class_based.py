class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, *args):
        self.file.close()


with OpenFile('abc.txt', 'w+') as file:
    file.write("Hello")

with OpenFile('abc.txt', 'r+') as file:
    print(file.readline())
