from phpton import generate_links
from phpton.web import route


@route("/")
def index():
    print("~main~")


@route("/hello")
def hello_world():
    print("Hello, world!")


if __name__ == '__main__':
    generate_links("public_html/")
