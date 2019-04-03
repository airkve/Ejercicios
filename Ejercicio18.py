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

item1Pric = 0.6
item2Pric = 3
item3Pric = 1.25

totalSale = 0
totalLiters = 0
sellsOver600 = 0

for i in range(5):
    itemId = input('Selecciona algunos de nuestros productos:\na) Jabon liquido\nb) Suavizante\nc) Desinfectante ')
    itemQty = int(input('Ingresa la cantidad en litros: '))

    if itemId.lower() == 'a':
        totalInvoice = item1Pric * itemQty
        if totalInvoice > 600:
            sellsOver600 += 1
        totalSale += totalInvoice
        item = 'Jabon Liquido'
    elif itemId.lower() == 'b':
        totalInvoice = item2Pric * itemQty
        if totalInvoice > 600:
            sellsOver600 += 1
        totalSale += totalInvoice
        item = 'Suavizante'
    elif itemId.lower() == 'c':
        totalInvoice = item3Pric * itemQty
        if totalInvoice > 600:
            sellsOver600 += 1
        totalSale += totalInvoice
        item = 'Desinfectante'
    
    print('{:-^120}'.format('Factura'))
    print('{:_<20}{:_^60}{:_>40}'.format('Codigo del producto', 'Cantidad', 'Precio'))
    print('{:<20}{:^60}{:>40}'.format(item, itemQty, totalInvoice))

print('El total facturado es de: $', totalSale)
print('La cantidad de facturas por mas de $600, son: ', sellsOver600)

