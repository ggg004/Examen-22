# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido:Gaspar Gómez
# Curso:2do 2da
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.



# =========================
# ETAPA 1 - INICIO
# =========================

nombre_cliente=input("Digame su nombre ")
dinero_disponible=int(input("¿Cuanto dinero tiene disponible?"))
print("Kiosco Escolar")
print(f"Bienvenido {nombre_cliente}")
print(f"Tiene {dinero_disponible} pesos en total.")
dinero_gastado=0
cantidad_productos=0
cantidad_aguas=0
cantidad_alfajores=0
cantidad_tostados=0
nombres_productos=["Alfajores","Aguas","Tostados"]
precios=["700$","900$", "2200$"]

# =========================
# ETAPA 2 - COMPRAS
# =========================

print("Menú: 1.ALFAJORES:700, 2.AGUAS:900, 3.TOSTADOS:2200")
producto=int(input("Seleccione una opción"))
if producto==1:
    producto_elegido=nombres_productos[0]
    precio_producto=precios[0]
    print(producto_elegido)
    print(precio_producto)
    if dinero_disponible>700:
        dinero_gastado=dinero_gastado+700
        dinero_disponible=dinero_disponible-700
        cantidad_productos=cantidad_productos+1
        cantidad_alfajores=cantidad_alfajores+1
        print("Producto seleccionado: Alfajor")
        print("Precio: $700")
        print("Compra realizada correctamente.")
        print("Saldo restante"),dinero_disponible
    else:
        print("Saldo insuficiente para realizar esta compra.")
elif producto==2:
    producto_elegido=nombres_productos
    precio_producto=precios[1]
    print(producto_elegido)
    print(precio_producto)
    if dinero_disponible>900:
        dinero_gastado=dinero_gastado+900
        dinero_disponible=dinero_disponible-900
        cantidad_productos=cantidad_productos+1
        cantidad_aguas=cantidad_aguas+1
        print("Producto seleccionado: Agua")
        print("Precio: $900")
        print("Compra realizada correctamente.")
        print("Saldo restante"),dinero_disponible
    else:
        print("Saldo insuficiente para realizar esta compra.")
else :
    producto_elegido=nombres_productos[2]
    precio_producto=precios[2]
    print(producto_elegido)
    print(precio_producto)
    if dinero_disponible>2200:
        dinero_gastado=dinero_gastado+2200
        dinero_disponible=dinero_disponible-2200
        cantidad_productos=cantidad_productos+1
        cantidad_tostados=cantidad_tostados+1
        print("Producto seleccionado: Tostado")
        print("Precio: $2200")
        print("Compra realizada correctamente.")
        print("Saldo restante"),dinero_disponible
    else:
        print("Saldo insuficiente para realizar esta compra.")


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.
