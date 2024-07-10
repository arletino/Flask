
from flask import Flask, render_template, url_for
from random import randint

class Template_page:
    top_menu_list = ['Главная', 'Одежда', 'Обувь', 'Куртки' ]
    title: str = 'Test template page'
    footer: str = 'Footer template page'
    path: str = ['root', 'clothes', 'shoes', 'jacket']
    top_menu: dict[str, str] = []
    _isinstance= None
    
    def __init__(self) -> None:
        self.title = self.title
        self.footer = self.footer
        self.path = self.path
        self.top_menu_list = self.top_menu_list
        self.top_menu = [{'name': item, 'url':url_for(url)} for item, url in zip(self.top_menu_list, self.path) ]

    
    
    
    def __call__(self, *args,  **kwargs) :
        return self.__dict__
    
    # def __new__(cls):
    #     if cls._isinstance is None:
    #         cls._isinstance = super().__new__(cls)
    #         cls.top_menu_list.append()
        
    
class Index_page(Template_page):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'This is start page - index.html'
        # self.top_menu_list = ['Одежда', 'Обувь', 'Куртки']


class Clothes_page(Index_page):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'This is start page - clothes.html'
        # self.path = 'clothes.html'

class Shoes_page(Index_page):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'This is start page - Shoes.html'
        # self.path = 'clothes.html' 

class Jacket_page(Index_page):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'This is start page - jacket.html'
        # self.path = 'clothes.html'       

app = Flask(__name__)

@app.route('/')
def root():
    index = Index_page()
    return render_template('index.html', root_page = index())

@app.route('/clothes')
def clothes():
    index = Clothes_page()
    clothes = [{'name': 'name' + str(i), 'description':f'lorem', 'price':10*randint(i, i*3)} for i in range(3)]
    return render_template('clothes.html', root_page = index(), clothes = clothes)

@app.route('/jacket')
def jacket():
    index = Jacket_page()
    clothes = [{'name': 'name' + str(i), 'description':f'lorem', 'price':10*randint(i, i*3)} for i in range(3)]
    return render_template('jacket.html', root_page = index(), clothes = clothes)

@app.route('/shoes')
def shoes():
    index = Shoes_page()
    clothes = [{'name': 'name' + str(i), 'description':f'lorem', 'price':10*randint(i, i*3)} for i in range(3)]
    return render_template('shoes.html', root_page = index(), clothes = clothes)

if __name__ == '__main__':
   
   app.run(debug=True) 