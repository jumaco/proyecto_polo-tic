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
