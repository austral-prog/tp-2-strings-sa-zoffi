def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base=int(input())
    altura=int(input())
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    area=base*altura
    print(f"Area: {area}")
    perimetro=altura*2+base*2
    print(f"Perimetro: {perimetro}")
#rectangle()