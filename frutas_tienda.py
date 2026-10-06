carrito = {}
producto_frutas = {"manzanas": 15, "cambures": 20, "naranjas": 15, "peras": 20, "uvas": 25}
preguntas = ["agregar producto", "ver carrito", "finalizar compra"]


def numero_entero_positivo(mensaje):
    while True:
        respuesta = input(mensaje)
        if respuesta.isdigit() and int(respuesta) > 0:
            return int(respuesta)
        print("debe ingresar un numero positivo")


def pregunta_sn(texto):
    while True:
        respuesta = input(f"{texto}? (si/no): ").lower()
        if respuesta == 'si' or respuesta == 'no':
            return respuesta
        else:
            print("respuesta invalida (debe responder si o no)")


def agregar_producto(carrito):
    while True:
        producto_comprar = input("que le gustaria agregar al carrito?: ").lower()
        if producto_comprar not in producto_frutas:
            print(f"disculpa, pero no tenemos {producto_comprar} en stock")
        else:
            cantidad_producto = numero_entero_positivo(f"cuantas {producto_comprar} desea llevar?: ")
            carrito[producto_comprar] = carrito.get(producto_comprar, 0) + cantidad_producto
            respuesta2 = pregunta_sn("desea agregar otro producto")
            if respuesta2 != "si":
                break


def ver_carrito(carrito):
    while True:
        if not carrito:
            print("no tienes nada en el carrito")
            break
        else:
            print("en el carrito tienes:")
            for producto, cantidad in carrito.items():
                print(f"{producto}: {cantidad}")
            pregunta_delete = input("quisieras quitar algun producto? (si/no): ")
            if pregunta_delete != "si":
                break
            else:
                respuesta_delete = "si"
                while respuesta_delete == "si":
                    producto_delete = input("que quisiera quitar del carrito?: ").lower()
                    if producto_delete not in carrito:
                        print(f"no tienes {producto_delete} en el carrito")
                        continue
                    else:
                        cantidad_delete = numero_entero_positivo(f"cuantas {producto_delete} quisiera quitar?: ")
                        if cantidad_delete >= carrito[producto_delete]:
                            del carrito[producto_delete]
                            print(f"{producto_delete} ha sido eliminado del carrito")
                        else:
                            carrito[producto_delete] -= cantidad_delete
                            print(f"sacaste {cantidad_delete} {producto_delete} del carrito")
                        respuesta_delete = pregunta_sn("desea quitar algo mas")
                        if respuesta_delete == "si":
                            continue
                        else:
                            break


def finalizar_compra(carrito):
    factura_total = 0
    for producto, cantidad in carrito.items():
        subtotal = producto_frutas[producto] * cantidad
        factura_total += subtotal
        print(f"{producto}: {cantidad} X {producto_frutas[producto]} = {subtotal}")
    print(f"el total seria de {factura_total}Bs")
    if factura_total >= 100:
        descuento = factura_total * 0.1
        print(f"su total seria de {factura_total}, pero como su compra supera los 100bs, le aplicaremos un 10% de descuento ({descuento}bs), con lo cual le quedaria en {factura_total * 0.9}bs")


while True:
    print("que quieres hacer?: ")
    for n, opciones in enumerate(preguntas, start=1):
        print(f"{n}. {opciones}")
    resp = input()
    match resp:
        case "1":
            agregar_producto(carrito)
        case "2":
            ver_carrito(carrito)
        case "3":
            finalizar_compra(carrito)
            break
        case _:
            print("esa opcion no es valida")
