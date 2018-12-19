from DecoratorsPackage.html_dec.underline import underline
from DecoratorsPackage.html_dec.bold import bold
from DecoratorsPackage.html_dec.italic import italic
from DecoratorsPackage.delay import delay
from DecoratorsPackage.raises import raises

if __name__ == "__main__":
    print('Message from main application!')

    @underline
    @bold
    @italic
    def my_fun():
        return 'Hello World'


    print(my_fun())
