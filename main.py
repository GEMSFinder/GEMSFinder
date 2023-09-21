#from kivy.app import App
from kivy.properties import NumericProperty ,  StringProperty
# from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.lang import Builder
#from kivymd.uix.textfield import MDTextField
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
#from kivymd.uix.selectioncontrol import MDSwitch
#from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

class Screens(ScreenManager):
    pass

class reportitemscroll(ScrollView):
    pass
class  HomeScreen(Screen):
    extendSign=StringProperty("C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png")
    extend_check=NumericProperty(1)
    extend_x = NumericProperty(0.225)
    switch = NumericProperty(0)
    def extend(self):

        if  self.extend_check==1:

            self.switch=-1
            self.extendSign="C:\\Users\\97155\\Downloads\\Screenshot_20230904_180649_Word.png"
            self.extend_x=0
            self.extend_check=0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self,categories):
        if categories == 'Electronics':
            self.manager.current = "electronics"
        if categories == 'Stationary':
            self.manager.current = "stationary"
        if categories == 'Books':
            self.manager.current = "books"
        if categories == 'Clothes':
            self.manager.current = "clothes"
        if categories == 'Other':
            self.manager.current = "others"
    def reportitems(self):
        self.manager.current='reportitems'
    def search(self):
        Search = self.ids.searchbar.text

        if Search=="Electronics" or Search=="electronics" or Search=="ipad" or Search=="Ipad" or Search =="IPad"or Search=="Phone"or Search=="Tablet"or Search=="Laptop"or Search=="phone"or Search == "laptop"or Search=="mouse"or Search=="watch"or Search=="huwaei"or Search=="razor"or Search=="apple"or Search=="andriod":
            self.manager.current='electronics'
        if Search=='Stationary'or Search=="stationary"or Search=="pencil"or Search=="pen"or Search=="rubber"or Search=="eraser"or Search=="ruler"or Search=="scale"or Search=="sharpener"or Search=="pages"or Search=="page"or Search=="Pencil"or Search=="Pen"or Search=="Rubber"or Search=="Eraser"or Search=="Ruler"or Search=="Scale"or Search=="Sharpener"or Search=="Pages"or Search=="Page":
            self.manager.current = 'stationary'
        if Search=='Books'or Search=="books"or Search=="grade"or Search=="evs"or Search=="science"or Search=="english"or Search=="textbook"or Search=="notebook"or Search=="math"or Search=="maths"or Search=="cs"or Search=="computer"or Search=="computer science"or Search=="hindi"or Search=="french"or Search=="urdu"or Search=="malayalam"or Search=="biology"or Search=="chemistry"or Search=="physics":
            self.manager.current='books'
        if Search=='sweater'or Search=="shirt"or Search=="pants"or Search=="tie"or Search=="socks"or Search=="clothes" or Search=='Sweater'or Search=="Shirt"or Search=="Pants"or Search=="Tie"or Search=="Socks"or Search=="Clothes":
            self.manager.current='clothes'
        else:
            self.manager.current="notfound"
class Electronics(Screen):
    extendSign = StringProperty("C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png")
    extend_check = NumericProperty(1)
    extend_x = NumericProperty(0.225)
    switch = NumericProperty(0)

    def extend(self):
        if self.extend_check == 1:

            self.switch = -1
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180649_Word.png"
            self.extend_x = 0
            self.extend_check = 0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self,categories):



        if categories == 'Stationary':
            self.manager.current = "stationary"
        if categories == 'Books':
            self.manager.current = "books"
        if categories == 'Clothes':
            self.manager.current = "clothes"
        if categories == 'Other':
            self.manager.current = "others"
    def homebutton(self):

        self.manager.current="homescreen"

        def search(self):
            Search = self.ids.searchbar.text


            if Search == 'Stationary' or Search == "stationary" or Search == "pencil" or Search == "pen" or Search == "rubber" or Search == "eraser" or Search == "ruler" or Search == "scale" or Search == "sharpener" or Search == "pages" or Search == "page" or Search == "Pencil" or Search == "Pen" or Search == "Rubber" or Search == "Eraser" or Search == "Ruler" or Search == "Scale" or Search == "Sharpener" or Search == "Pages" or Search == "Page":
                self.manager.current = 'stationary'
            if Search == 'Books' or Search == "books" or Search == "grade" or Search == "evs" or Search == "science" or Search == "english" or Search == "textbook" or Search == "notebook" or Search == "math" or Search == "maths" or Search == "cs" or Search == "computer" or Search == "computer science" or Search == "hindi" or Search == "french" or Search == "urdu" or Search == "malayalam" or Search == "biology" or Search == "chemistry" or Search == "physics":
                self.manager.current = 'books'
            if Search == 'sweater' or Search == "shirt" or Search == "pants" or Search == "tie" or Search == "socks" or Search == "clothes" or Search == 'Sweater' or Search == "Shirt" or Search == "Pants" or Search == "Tie" or Search == "Socks" or Search == "Clothes":
                self.manager.current = 'clothes'
            else:
                self.manager.current="notfound"
class Stationary(Screen):
    extendSign = StringProperty("C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png")
    extend_check = NumericProperty(1)
    extend_x = NumericProperty(0.225)
    switch = NumericProperty(0)

    def extend(self):
        if self.extend_check == 1:

            self.switch = -1
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180649_Word.png"
            self.extend_x = 0
            self.extend_check = 0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self,categories):
        if categories == 'Electronics':
            self.manager.current = "electronics"
        if categories == 'Books':
            self.manager.current = "books"
        if categories == 'Clothes':
            self.manager.current = "clothes"
        if categories == 'Other':
            self.manager.current = "others"

    def homebutton(self):
        self.manager.current="homescreen"
    def search(self):
        Search = self.ids.searchbar.text

        if Search == "Electronics" or Search == "electronics" or Search == "ipad" or Search == "Ipad" or Search == "IPad" or Search == "Phone" or Search == "Tablet" or Search == "Laptop" or Search == "phone" or Search == "laptop" or Search == "mouse" or Search == "watch" or Search == "huwaei" or Search == "razor" or Search == "apple" or Search == "andriod":
            self.manager.current = 'electronics'
        if Search=='Books'or Search=="books"or Search=="grade"or Search=="evs"or Search=="science"or Search=="english"or Search=="textbook"or Search=="notebook"or Search=="math"or Search=="maths"or Search=="cs"or Search=="computer"or Search=="computer science"or Search=="hindi"or Search=="french"or Search=="urdu"or Search=="malayalam"or Search=="biology"or Search=="chemistry"or Search=="physics":
            self.manager.current='books'
        if Search=='sweater'or Search=="shirt"or Search=="pants"or Search=="tie"or Search=="socks"or Search=="clothes" or Search=='Sweater'or Search=="Shirt"or Search=="Pants"or Search=="Tie"or Search=="Socks"or Search=="Clothes":
            self.manager.current='clothes'

class Clothes(Screen):
    extendSign = StringProperty("C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png")
    extend_check = NumericProperty(1)
    extend_x = NumericProperty(0.225)
    switch = NumericProperty(0)

    def extend(self):
        if self.extend_check == 1:

            self.switch = -1
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180649_Word.png"
            self.extend_x = 0
            self.extend_check = 0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self,categories):
        if categories == 'Electronics':
            self.manager.current = "electronics"
        if categories == 'Stationary':
            self.manager.current = "stationary"
        if categories == 'Books':
            self.manager.current = "books"
        if categories == 'Other':
            self.manager.current = "others"
    def homebutton(self):
        self.manager.current="homescreen"
    def search(self):
        Search = self.ids.searchbar.text

        if Search=="Electronics" or Search=="electronics" or Search=="ipad" or Search=="Ipad" or Search =="IPad"or Search=="Phone"or Search=="Tablet"or Search=="Laptop"or Search=="phone"or Search == "laptop"or Search=="mouse"or Search=="watch"or Search=="huwaei"or Search=="razor"or Search=="apple"or Search=="andriod":
            self.manager.current='electronics'
        if Search == 'Stationary' or Search == "stationary" or Search == "pencil" or Search == "pen" or Search == "rubber" or Search == "eraser" or Search == "ruler" or Search == "scale" or Search == "sharpener" or Search == "pages" or Search == "page" or Search == "Pencil" or Search == "Pen" or Search == "Rubber" or Search == "Eraser" or Search == "Ruler" or Search == "Scale" or Search == "Sharpener" or Search == "Pages" or Search == "Page":
            self.manager.current = 'stationary'

        if Search=='Books'or Search=="books"or Search=="grade"or Search=="evs"or Search=="science"or Search=="english"or Search=="textbook"or Search=="notebook"or Search=="math"or Search=="maths"or Search=="cs"or Search=="computer"or Search=="computer science"or Search=="hindi"or Search=="french"or Search=="urdu"or Search=="malayalam"or Search=="biology"or Search=="chemistry"or Search=="physics":
            self.manager.current='books'


class Books(Screen):
    extendSign = StringProperty("C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png")
    extend_check = NumericProperty(1)
    extend_x = NumericProperty(0.225)
    switch = NumericProperty(0)

    def extend(self):
        if self.extend_check == 1:

            self.switch = -1
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180649_Word.png"
            self.extend_x = 0
            self.extend_check = 0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self,categories):

        if categories == 'Electronics':
            self.manager.current = "electronics"
        if categories == 'Stationary':
            self.manager.current = "stationary"
        if categories == 'Books':
            self.manager.current = "clothes"
        if categories == 'Other':
            self.manager.current = "others"

    def homebutton(self):
        self.manager.current="homescreen"
    def search(self):
        Search = self.ids.searchbar.text

        if Search=="Electronics" or Search=="electronics" or Search=="ipad" or Search=="Ipad" or Search =="IPad"or Search=="Phone"or Search=="Tablet"or Search=="Laptop"or Search=="phone"or Search == "laptop"or Search=="mouse"or Search=="watch"or Search=="huwaei"or Search=="razor"or Search=="apple"or Search=="andriod":
            self.manager.current='electronics'
        if Search=='Stationary'or Search=="stationary"or Search=="pencil"or Search=="pen"or Search=="rubber"or Search=="eraser"or Search=="ruler"or Search=="scale"or Search=="sharpener"or Search=="pages"or Search=="page"or Search=="Pencil"or Search=="Pen"or Search=="Rubber"or Search=="Eraser"or Search=="Ruler"or Search=="Scale"or Search=="Sharpener"or Search=="Pages"or Search=="Page":
            self.manager.current = 'stationary'
        if Search=='sweater'or Search=="shirt"or Search=="pants"or Search=="tie"or Search=="socks"or Search=="clothes" or Search=='Sweater'or Search=="Shirt"or Search=="Pants"or Search=="Tie"or Search=="Socks"or Search=="Clothes":
            self.manager.current='clothes'
class Others(Screen):
    extendSign = StringProperty("C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png")
    extend_check = NumericProperty(1)
    extend_x = NumericProperty(0.225)
    switch = NumericProperty(0)

    def extend(self):
        if self.extend_check == 1:

            self.switch = -1
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180649_Word.png"
            self.extend_x = 0
            self.extend_check = 0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self,categories):

        if categories == 'Electronics':
            self.manager.current = "electronics"
        if categories == 'Stationary':
            self.manager.current = "stationary"
        if categories == 'Books':
            self.manager.current = "books"
        if categories == 'Clothes':
            self.manager.current = "clothes"


    def homebutton(self):
        self.manager.current="homescreen"

class Test(StackLayout):
    pass

class TopMenu(BoxLayout):
    pass

class HomeFound(GridLayout):
    pass

class LoginScreen(Screen):
    check = NumericProperty(0)
    #light=BooleanProperty(False)
    error=StringProperty("")
    def login(self):
        username=self.ids.username.text
        password=self.ids.password.text



        if password == "q" and username == "q":
            self.error=""

            self.check = 0

            self.manager.current = "homescreen"
        else:
            self.check = "1"


    def reset(self):
        self.check=0


    def reseto(self):
        self.check=0
        username = self.ids.username.text
        password = self.ids.password.text

        if password == "pass123" and username == "kanishkk":
            self.error = ""

            self.check = 0

        else:
            self.check = 1
            self.manager.current="homescreen"

class LoginArea(FloatLayout):
    pass

class ReportItems(Screen):
    extendSign = StringProperty("C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png")
    extend_check = NumericProperty(1)
    extend_x = NumericProperty(0.225)
    switch = NumericProperty(0)

    def extend(self):

        if self.extend_check == 1:

            self.switch = -1
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180649_Word.png"
            self.extend_x = 0
            self.extend_check = 0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self, categories):
        if categories == 'Electronics':
            self.manager.current = "electronics"
        if categories == 'Stationary':
            self.manager.current = "stationary"
        if categories == 'Books':
            self.manager.current = "books"
        if categories == 'Clothes':
            self.manager.current = "clothes"
        if categories == 'Other':
            self.manager.current = "others"

    def reportitems(self):
        self.manager.current = 'reportitems'

    def search(self):
        Search = self.ids.searchbar.text

        if Search == "Electronics" or Search == "electronics" or Search == "ipad" or Search == "Ipad" or Search == "IPad" or Search == "Phone" or Search == "Tablet" or Search == "Laptop" or Search == "phone" or Search == "laptop" or Search == "mouse" or Search == "watch" or Search == "huwaei" or Search == "razor" or Search == "apple" or Search == "andriod":
            self.manager.current = 'electronics'
        if Search == 'Stationary' or Search == "stationary" or Search == "pencil" or Search == "pen" or Search == "rubber" or Search == "eraser" or Search == "ruler" or Search == "scale" or Search == "sharpener" or Search == "pages" or Search == "page" or Search == "Pencil" or Search == "Pen" or Search == "Rubber" or Search == "Eraser" or Search == "Ruler" or Search == "Scale" or Search == "Sharpener" or Search == "Pages" or Search == "Page":
            self.manager.current = 'stationary'
        if Search == 'Books' or Search == "books" or Search == "grade" or Search == "evs" or Search == "science" or Search == "english" or Search == "textbook" or Search == "notebook" or Search == "math" or Search == "maths" or Search == "cs" or Search == "computer" or Search == "computer science" or Search == "hindi" or Search == "french" or Search == "urdu" or Search == "malayalam" or Search == "biology" or Search == "chemistry" or Search == "physics":
            self.manager.current = 'books'
        if Search == 'sweater' or Search == "shirt" or Search == "pants" or Search == "tie" or Search == "socks" or Search == "clothes" or Search == 'Sweater' or Search == "Shirt" or Search == "Pants" or Search == "Tie" or Search == "Socks" or Search == "Clothes":
            self.manager.current = 'clothes'
        else:
            self.manager.current = "notfound"
    def photo(self):
        self.manager.current="photo"
class FoundItemDescription(Screen):
    i=StringProperty("Request for claim")
    extendSign = StringProperty("C:\\Users\\USER\\Pictures\\Game Sprites\\de extend.png")
    extend_check = NumericProperty(1)
    extend_x = NumericProperty(0.165)
    switch = NumericProperty(0)

    def extend(self):

        if self.extend_check == 1:

            self.switch = -1
            self.extendSign = "C:\\Users\\USER\\Pictures\\Game Sprites\\extend.png"
            self.extend_x = 0
            self.extend_check = 0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\USER\\Pictures\\Game Sprites\\de extend.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self, categories):
        if categories == 'Electronics':
            self.manager.current = "electronics"
        if categories == 'Stationary':
            self.manager.current = "stationary"
        if categories == 'Books':
            self.manager.current = "books"
        if categories == 'Clothes':
            self.manager.current = "clothes"
        if categories == 'Other':
            self.manager.current = "others"

    def reportitems(self):
        self.manager.current = 'reportitems'

    def search(self):
        Search = self.ids.searchbar.text

        if Search == "Electronics" or Search == "electronics"  or Search == "Phone" or Search == "Tablet" or Search == "Laptop" or Search == "phone" or Search == "laptop" or Search == "mouse" or Search == "watch" or Search == "huwaei" or Search == "razor" or Search == "apple" or Search == "andriod":
            self.manager.current = 'electronics'
        if Search == 'Stationary' or Search == "stationary" or Search == "pencil" or Search == "pen" or Search == "rubber" or Search == "eraser" or Search == "ruler" or Search == "scale" or Search == "sharpener" or Search == "pages" or Search == "page" or Search == "Pencil" or Search == "Pen" or Search == "Rubber" or Search == "Eraser" or Search == "Ruler" or Search == "Scale" or Search == "Sharpener" or Search == "Pages" or Search == "Page":
            self.manager.current = 'stationary'
        if Search == 'Books' or Search == "books" or Search == "grade" or Search == "evs" or Search == "science" or Search == "english" or Search == "textbook" or Search == "notebook" or Search == "math" or Search == "maths" or Search == "cs" or Search == "computer" or Search == "computer science" or Search == "hindi" or Search == "french" or Search == "urdu" or Search == "malayalam" or Search == "biology" or Search == "chemistry" or Search == "physics":
            self.manager.current = 'books'
        if Search == 'sweater' or Search == "shirt" or Search == "pants" or Search == "tie" or Search == "socks" or Search == "clothes" or Search == 'Sweater' or Search == "Shirt" or Search == "Pants" or Search == "Tie" or Search == "Socks" or Search == "Clothes":
            self.manager.current = 'clothes'
        else:
            self.manager.current = "notfound"

    def claimitem(self):
        self.manager.current="proof"







    def homebutton(self):
        self.manager.current = "homescreen"

class SweaterDescription(Screen):
    i = StringProperty("Request for claim")
    extendSign = StringProperty("C:\\Users\\USER\\Pictures\\Game Sprites\\de extend.png")
    extend_check = NumericProperty(1)
    extend_x = NumericProperty(0.225)
    switch = NumericProperty(0)

    def extend(self):

        if self.extend_check == 1:

            self.switch = -1
            self.extendSign = "C:\\Users\\USER\\Pictures\\Game Sprites\\extend.png"
            self.extend_x = 0
            self.extend_check = 0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\USER\\Pictures\\Game Sprites\\de extend.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self, categories):
        if categories == 'Electronics':
            self.manager.current = "electronics"
        if categories == 'Stationary':
            self.manager.current = "stationary"
        if categories == 'Books':
            self.manager.current = "books"
        if categories == 'Clothes':
            self.manager.current = "clothes"
        if categories == 'Other':
            self.manager.current = "others"

    def reportitems(self):
        self.manager.current = 'reportitems'

    def search(self):
        Search = self.ids.searchbar.text

        if Search == "Electronics" or Search == "electronics" or Search == "ipad" or Search == "Ipad" or Search == "IPad" or Search == "Phone" or Search == "Tablet" or Search == "Laptop" or Search == "phone" or Search == "laptop" or Search == "mouse" or Search == "watch" or Search == "huwaei" or Search == "razor" or Search == "apple" or Search == "andriod":
            self.manager.current = 'electronics'
        if Search == 'Stationary' or Search == "stationary" or Search == "pencil" or Search == "pen" or Search == "rubber" or Search == "eraser" or Search == "ruler" or Search == "scale" or Search == "sharpener" or Search == "pages" or Search == "page" or Search == "Pencil" or Search == "Pen" or Search == "Rubber" or Search == "Eraser" or Search == "Ruler" or Search == "Scale" or Search == "Sharpener" or Search == "Pages" or Search == "Page":
            self.manager.current = 'stationary'
        if Search == 'Books' or Search == "books" or Search == "grade" or Search == "evs" or Search == "science" or Search == "english" or Search == "textbook" or Search == "notebook" or Search == "math" or Search == "maths" or Search == "cs" or Search == "computer" or Search == "computer science" or Search == "hindi" or Search == "french" or Search == "urdu" or Search == "malayalam" or Search == "biology" or Search == "chemistry" or Search == "physics":
            self.manager.current = 'books'
        if Search == 'sweater' or Search == "shirt" or Search == "pants" or Search == "tie" or Search == "socks" or Search == "clothes" or Search == 'Sweater' or Search == "Shirt" or Search == "Pants" or Search == "Tie" or Search == "Socks" or Search == "Clothes":
            self.manager.current = 'clothes'
        else:
            self.manager.current = "notfound"

    def claimitem(self):
        self.manager.current="proof"


    def homebutton(self):
        self.manager.current = "homescreen"

    class Proof(Screen):
        i = StringProperty("Sumbit")
        extendSign = StringProperty("C:\\Users\\USER\\Pictures\\Game Sprites\\de extend.png")
        extend_check = NumericProperty(1)
        extend_x = NumericProperty(0.225)
        switch = NumericProperty(0)

        def extend(self):

            if self.extend_check == 1:

                self.switch = -1
                self.extendSign = "C:\\Users\\USER\\Pictures\\Game Sprites\\extend.png"
                self.extend_x = 0
                self.extend_check = 0
                print("done")


            elif self.extend_check == 0:
                self.switch = 0
                self.extendSign = "C:\\Users\\USER\\Pictures\\Game Sprites\\de extend.png"
                self.extend_x = 0.165
                self.extend_check = 1

        def FoundCategories(self, categories):
            if categories == 'Electronics':
                self.manager.current = "electronics"
            if categories == 'Stationary':
                self.manager.current = "stationary"
            if categories == 'Books':
                self.manager.current = "books"
            if categories == 'Clothes':
                self.manager.current = "clothes"
            if categories == 'Other':
                self.manager.current = "others"

        def reportitems(self):
            self.manager.current = 'reportitems'

        def search(self):
            Search = self.ids.searchbar.text

            if Search == "Electronics" or Search == "electronics" or Search == "ipad" or Search == "Ipad" or Search == "IPad" or Search == "Phone" or Search == "Tablet" or Search == "Laptop" or Search == "phone" or Search == "laptop" or Search == "mouse" or Search == "watch" or Search == "huwaei" or Search == "razor" or Search == "apple" or Search == "andriod":
                self.manager.current = 'electronics'
            if Search == 'Stationary' or Search == "stationary" or Search == "pencil" or Search == "pen" or Search == "rubber" or Search == "eraser" or Search == "ruler" or Search == "scale" or Search == "sharpener" or Search == "pages" or Search == "page" or Search == "Pencil" or Search == "Pen" or Search == "Rubber" or Search == "Eraser" or Search == "Ruler" or Search == "Scale" or Search == "Sharpener" or Search == "Pages" or Search == "Page":
                self.manager.current = 'stationary'
            if Search == 'Books' or Search == "books" or Search == "grade" or Search == "evs" or Search == "science" or Search == "english" or Search == "textbook" or Search == "notebook" or Search == "math" or Search == "maths" or Search == "cs" or Search == "computer" or Search == "computer science" or Search == "hindi" or Search == "french" or Search == "urdu" or Search == "malayalam" or Search == "biology" or Search == "chemistry" or Search == "physics":
                self.manager.current = 'books'
            if Search == 'sweater' or Search == "shirt" or Search == "pants" or Search == "tie" or Search == "socks" or Search == "clothes" or Search == 'Sweater' or Search == "Shirt" or Search == "Pants" or Search == "Tie" or Search == "Socks" or Search == "Clothes":
                self.manager.current = 'clothes'
            else:
                self.manager.current = "notfound"

        def claim(self):
            self.i = "Requst Filed"

        def hh(self):
            Photo = self.ids.photoproof.selection
            try:
                self.ids.photodisplayproof.source = Photo[0]
            except:
                pass

        def homebutton(self):
            self.manager.current = "homescreen"


class Photo(Screen):
    extendSign = StringProperty("C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png")
    extend_check = NumericProperty(1)
    extend_x = NumericProperty(0.225)
    switch = NumericProperty(0)

    def extend(self):

        if self.extend_check == 1:

            self.switch = -1
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180649_Word.png"
            self.extend_x = 0
            self.extend_check = 0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self, categories):
        if categories == 'Electronics':
            self.manager.current = "electronics"
        if categories == 'Stationary':
            self.manager.current = "stationary"
        if categories == 'Books':
            self.manager.current = "books"
        if categories == 'Clothes':
            self.manager.current = "clothes"
        if categories == 'Other':
            self.manager.current = "others"

    def reportitems(self):
        self.manager.current = 'reportitems'

    def search(self):
        Search = self.ids.searchbar.text

        if Search == "Electronics" or Search == "electronics" or Search == "ipad" or Search == "Ipad" or Search == "IPad" or Search == "Phone" or Search == "Tablet" or Search == "Laptop" or Search == "phone" or Search == "laptop" or Search == "mouse" or Search == "watch" or Search == "huwaei" or Search == "razor" or Search == "apple" or Search == "andriod":
            self.manager.current = 'electronics'
        if Search == 'Stationary' or Search == "stationary" or Search == "pencil" or Search == "pen" or Search == "rubber" or Search == "eraser" or Search == "ruler" or Search == "scale" or Search == "sharpener" or Search == "pages" or Search == "page" or Search == "Pencil" or Search == "Pen" or Search == "Rubber" or Search == "Eraser" or Search == "Ruler" or Search == "Scale" or Search == "Sharpener" or Search == "Pages" or Search == "Page":
            self.manager.current = 'stationary'
        if Search == 'Books' or Search == "books" or Search == "grade" or Search == "evs" or Search == "science" or Search == "english" or Search == "textbook" or Search == "notebook" or Search == "math" or Search == "maths" or Search == "cs" or Search == "computer" or Search == "computer science" or Search == "hindi" or Search == "french" or Search == "urdu" or Search == "malayalam" or Search == "biology" or Search == "chemistry" or Search == "physics":
            self.manager.current = 'books'
        if Search == 'sweater' or Search == "shirt" or Search == "pants" or Search == "tie" or Search == "socks" or Search == "clothes" or Search == 'Sweater' or Search == "Shirt" or Search == "Pants" or Search == "Tie" or Search == "Socks" or Search == "Clothes":
            self.manager.current = 'clothes'
        else:
            self.manager.current = "notfound"


class NotFound(Screen):
    extendSign = StringProperty("C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png")
    extend_check = NumericProperty(1)
    extend_x = NumericProperty(0.225)
    switch = NumericProperty(0)

    def extend(self):

        if self.extend_check == 1:

            self.switch = -1
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180649_Word.png"
            self.extend_x = 0
            self.extend_check = 0
            print("done")


        elif self.extend_check == 0:
            self.switch = 0
            self.extendSign = "C:\\Users\\97155\\Downloads\\Screenshot_20230904_180435_Word.png"
            self.extend_x = 0.165
            self.extend_check = 1

    def FoundCategories(self, categories):
        if categories == 'Electronics':
            self.manager.current = "electronics"
        if categories == 'Stationary':
            self.manager.current = "stationary"
        if categories == 'Books':
            self.manager.current = "books"
        if categories == 'Clothes':
            self.manager.current = "clothes"
        if categories == 'Other':
            self.manager.current = "others"

    def reportitems(self):
        self.manager.current = 'reportitems'

    def search(self):
        Search = self.ids.searchbar.text

        if Search == "Electronics" or Search == "electronics" or Search == "ipad" or Search == "Ipad" or Search == "IPad" or Search == "Phone" or Search == "Tablet" or Search == "Laptop" or Search == "phone" or Search == "laptop" or Search == "mouse" or Search == "watch" or Search == "huwaei" or Search == "razor" or Search == "apple" or Search == "andriod":
            self.manager.current = 'electronics'
        if Search == 'Stationary' or Search == "stationary" or Search == "pencil" or Search == "pen" or Search == "rubber" or Search == "eraser" or Search == "ruler" or Search == "scale" or Search == "sharpener" or Search == "pages" or Search == "page" or Search == "Pencil" or Search == "Pen" or Search == "Rubber" or Search == "Eraser" or Search == "Ruler" or Search == "Scale" or Search == "Sharpener" or Search == "Pages" or Search == "Page":
            self.manager.current = 'stationary'
        if Search == 'Books' or Search == "books" or Search == "grade" or Search == "evs" or Search == "science" or Search == "english" or Search == "textbook" or Search == "notebook" or Search == "math" or Search == "maths" or Search == "cs" or Search == "computer" or Search == "computer science" or Search == "hindi" or Search == "french" or Search == "urdu" or Search == "malayalam" or Search == "biology" or Search == "chemistry" or Search == "physics":
            self.manager.current = 'books'
        if Search == 'sweater' or Search == "shirt" or Search == "pants" or Search == "tie" or Search == "socks" or Search == "clothes" or Search == 'Sweater' or Search == "Shirt" or Search == "Pants" or Search == "Tie" or Search == "Socks" or Search == "Clothes":
            self.manager.current = 'clothes'

#kv=Builder.load_file('gemsfinder.kv')

class GEMSFinderApp(MDApp):
    def build(self):

        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('gemsfinder.kv')







GEMSFinderApp().run()