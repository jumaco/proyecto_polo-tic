from app.models import Category, Product

'''products = Product.objects.all()
categories = Category.objects.all()'''


def monto(request):
    total = 0.0
    if request.user.is_authenticated:
        if 'carrito' in request.session:
            for key, value in request.session['carrito'].items():
                total = total + (float(value['precio']))
    return {'monto': total}


def cantidad_pruductos(request):
    total = 0.0
    if request.user.is_authenticated:
        if 'carrito' in request.session:
            for key, value in request.session['carrito'].items():
                total = total + (float(value["cantidad"]))
    return {"cantidad_pruductos": total}

'''
def categories_list(request):
    categories = Category.objects.all()
    return {"categories": categories}
'''