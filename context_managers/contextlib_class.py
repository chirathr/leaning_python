from contextlib import ContextDecorator


class MakeBody(ContextDecorator):
    def __enter__(self):
        print("<body>")

    def __exit__(self, *args):
        print("</body>")


@MakeBody()
def print_html(content):
    print(content)


print_html("Some random text inside body tag")
