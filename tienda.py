from producto import Producto
class Tienda:

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_producto=[]

    def add_product (self, new_product) :
        self.lista_producto.append(new_product)

    def sell_product (self, id) :
        self.sell=self.lista_producto[id]
        self.lista_producto.remove(self.sell)

    def inflation(self, percent_increase) : 
        pass

    def display_info(self):
        print(self.lista_producto)


producto1 = Tienda("Leche")
producto1 = Tienda("Pan")

producto1.add_product("leche")
producto1.add_product("pan")
producto1.display_info()
producto1.sell_product(0)
producto1.display_info()