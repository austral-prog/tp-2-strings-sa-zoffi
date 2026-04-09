def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto=float(input())
    print(gasto)
    print("Dinero recibido")
    dinero_recibido=int(input())
    print(dinero_recibido)
    print()
    vuelto=dinero_recibido-gasto
    vuelto_pesos=int(dinero_recibido-gasto)
    print("Vuelto")
    print()
    print("Pesos:")
    print(vuelto_pesos)
    print("Centavos:")
    vuelto_centavos=int(round((vuelto-vuelto_pesos)*100))
    print(vuelto_centavos)

