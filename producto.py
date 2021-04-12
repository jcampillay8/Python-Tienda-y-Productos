class Producto:

    def __init__(self,nombre,precio,categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.aumento = False

    def update_price(self, percent_change, is_increased):
        
        self.aumento=is_increased

        if self.aumento==True:
            self.precio = self.precio + (self.precio*percent_change)
            print(self.precio)

    def print_info (self) :
        print("Nombre: "+self.nombre+"\nPrecio: "+str(self.precio)+"\nCategoria: "+self.categoria)


canasta1=Producto("Pan",1000,"masa")

canasta1.update_price(0.2,True)
canasta1.print_info()
