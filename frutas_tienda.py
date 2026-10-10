import json
from datetime import datetime
import os
if os.path.exists("catalogo.json"):
    with open("catalogo.json", "r", encoding="utf-8") as f:
        catalogo = json.load(f)
else:
    catalogo = {"manzanas": 15, "cambures": 20, "naranjas": 15, "peras": 10, "uvas": 25}


carrito = {}
preguntas = ["agregar producto", "ver carrito", "finalizar compra"]


def numero_entero_positivo(mensaje):
    while True:
        respuesta = input(mensaje)
        if respuesta.isdigit() and int(respuesta) > 0:
            return int(respuesta)
        print("debe ingresar un numero positivo")


def agregar_producto(carrito):
    while True:
        producto_comprar = input("que le gustaria agregar al carrito?: ").lower()
        if producto_comprar not in catalogo:
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
            pregunta_delete = pregunta_sn("quisieras quitar algun producto")
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
                        if respuesta_delete =="si":
                            continue
                        else:
                            break


def pregunta_sn(texto):
    while True:
        respuesta = input(f"{texto}? (si/no): ").lower()
        if respuesta=='si' or respuesta=='no':
            return respuesta
        else:
            print("respuesta invalida (debe responder si o no)")


def finalizar_compra(carrito):
    datos_factura = [f"[{datetime.now():%Y-%m-%d %H:%M}]"]

    if not carrito:
        print("No lleva nada en el carrito")
        if pregunta_sn("Le gustaria volver y meter algo al carrito") == "si":
            return False      
        datos_factura.append("No hay nada que facturar")
    else:
        factura_total = 0
        for producto, cantidad in carrito.items():
            subtotal = catalogo[producto] * cantidad
            factura_total += subtotal
            datos_factura.append(f"- {producto}: {cantidad} x {catalogo[producto]} = {subtotal}Bs")
            print(f"{producto}: {cantidad} X {catalogo[producto]} = {subtotal}Bs")

        print(f"El total sería de {factura_total}Bs")
        if factura_total >= 100:
            descuento = factura_total * 0.1
            total_final = factura_total * 0.9
            print(f"Descuento del 10% ({descuento}Bs). Total: {total_final}Bs")
            datos_factura.append(f"Serían {factura_total}Bs menos el descuento de {descuento}Bs: total {total_final}Bs")
        else:
            datos_factura.append(f"Su total sería de: {factura_total}Bs")

    with open("facturas.txt", "a", encoding="utf-8") as f:   
        f.write("\n".join(datos_factura) + "\n\n")

    return True     

        

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
            if finalizar_compra(carrito):
                break
        case _:
            print("Esa opción no es válida")