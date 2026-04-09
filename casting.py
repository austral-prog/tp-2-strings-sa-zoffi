def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio=int(input())
    descuento=float(input())
    cantidad=int(input())
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    pdescuento=precio-descuento
    print(f"Precio con descuento: {pdescuento}")
    total=cantidad*(precio-descuento)
    print(f"Total: {total}")
#casting()