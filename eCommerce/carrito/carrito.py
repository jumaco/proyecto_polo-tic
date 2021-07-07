class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, product):
        if str(product.id) not in self.carrito.keys():
            self.carrito[product.id] = {
                "producto_id": product.id,
                "nombre": product.name,
                "precio": product.price,
                "imagen": product.image.url,
                "cantidad": 1
            }
        else:
            for key, value in self.carrito.items():
                if key == str(product.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"])+product.price
                    break
        self.salvar()

    def salvar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def remover(self, product):
        product_id = str(product.id)
        if product_id in self.carrito:
            del self.carrito[product_id]
            self.salvar()

    def restar(self, product):
        for key, value in self.carrito.items():
            if key == str(product.id):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"] = float(value["precio"]) - product.price
                if value["cantidad"] < 1:
                    self.remover(product)
                else:
                    self.salvar()
                break

    def vaciar(self):
        self.session["carrito"] = {}
        self.session.modified = True

