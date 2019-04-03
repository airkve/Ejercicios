# Crear un programa de facturacion, para una empresa que vende desinfectantes
# Campos de entrada:
# Codigo del producto
# Cantidad por litro
# Precio por litro
# Generar 5 facturas:
# Facturacion total
# Cantidad en litros vendidos de 1er producto
# Facturas emitidas de mas de $600

print('{:-^120}'.format('Progama de Facturacion'))

totalSale = 0
totalLiters = 0
sellsOver600 = 0

for i in range(5):
    itemId = input('Ingresa el codigo del producto: ')
    itemQty = int(input('Ingresa la cantidad en litros: '))
    itemPrice = int(input('Ingresa el precio: '))

    totalSale += itemPrice
    if i == 1:
        totalLiters = itemQty
    elif itemPrice > 600:
        sellsOver600 += 1

    print('{:-^120}'.format('Factura'))
    print('{:_<20}{:_^60}{:_>40}'.format('Codigo del producto', 'Cantidad', 'Precio'))
    print('{:<20}{:^60}{:>40}'.format(itemId, itemQty, itemPrice))

print('El total facturado es de: ', totalSale)
print('La cantidad de facturas por mas de $600, son: ', sellsOver600)

