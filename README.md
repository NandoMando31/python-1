# Inventory Stock Checker

A Python script that checks stock levels against minimum thresholds and flags which products need restocking.

## What problem does it solve?

In a warehouse, products that fall below their minimum stock level can cause delays and lost sales. This script reviews a list of products, labels each one as `OK`, `REPONER` (restock) or `AGOTADO` (out of stock), and summarizes how many products need attention and how many units are missing.

## How it works

Each product is a dictionary with a name, its current stock and its minimum stock. The script uses three functions:

- `estado(stock, minimo)`: takes the current stock and the minimum of one product and returns its status: `"AGOTADO"` if the stock is 0, `"REPONER"` if it is below the minimum, and `"OK"` otherwise.
- `contar_a_reponer(inventario)`: takes the full inventory and returns how many products are below their minimum stock (out-of-stock products included).
- `unidades_faltantes(inventario)`: takes the full inventory and returns the total number of units needed to bring every low-stock product back up to its minimum.

## How to run it

```
python inventory.py
```

Requires Python 3. No external libraries are needed.

## Example output

```
tornillo: OK
tuerca: REPONER
arandela: AGOTADO
perno: OK
clavo: REPONER
A reponer: 3
Unidades faltantes: 40