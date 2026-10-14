# 1. Los datos: la lista inventario con los 5 productos
inventario = [
    {"producto": "tornillo", "stock": 120, "minimo": 50},
    {"producto": "tuerca",   "stock": 30,  "minimo": 40},
    {"producto": "arandela", "stock": 0,   "minimo": 20},
    {"producto": "perno",    "stock": 75,  "minimo": 75},
    {"producto": "clavo",    "stock": 15,  "minimo": 25},
]

# 2. La función estado(stock, minimo)
def estado(stock, minimo):
    if stock == 0:
       return  "AGOTADO"
    elif stock < minimo:
        return "REPONER"
    else:
        return "OK"
# 3. La función contar_a_reponer(inventario)
def contar_a_reponer(inventario):
    rcontador =0
    for inv in inventario:
        if inv["stock"] < inv["minimo"] :
            rcontador =  rcontador + 1
    return rcontador
# 4. La función unidades_faltantes(inventario)
def unidades_faltantes(inventario):
    fcontador =0
    for inv in inventario:
        if inv["stock"] < inv["minimo"] :
            fcontador = fcontador + inv["minimo"] - inv["stock"]
    return fcontador
# 5. El for que muestra una línea por producto
for inv in inventario:
    print(f"{inv['producto']}: {estado(inv['stock'], inv['minimo'])}") 
# 6. El print de "A reponer"
print (f"A reponer: {contar_a_reponer(inventario)}")
# 7. El print de "Unidades faltantes"
print(f"Unidades faltantes: {unidades_faltantes(inventario)}")