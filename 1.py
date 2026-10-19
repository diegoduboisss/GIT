
print("=" * 35)
print("       POLLOS DEL SABOR")
print("=" * 35)
print("1. Pollo asado entero - $12")
print("2. Medio pollo con papas - $7")
print("3. Alitas (10 unidades) - $9")
print("4. Combo familiar - $20")
print("5. Salir")

opcion = input("¿Qué opción deseas? ")

if opcion == "5":
	print("¡Gracias por visitarnos!")
else:
	print("¡Excelente elección!")
	nombre = input("1. ¿A nombre de quién será el pedido? ")
	acompanamiento = input("2. ¿Qué acompañamiento prefieres: papas o ensalada? ")
	entrega = input("3. ¿Prefieres recogerlo o recibirlo a domicilio? ")

	print(f"\nPedido registrado para {nombre}.")
	print(f"Acompañamiento: {acompanamiento}")
	print(f"Modalidad: {entrega}")
	print("¡Gracias por comprar en Pollos del Sabor!")
