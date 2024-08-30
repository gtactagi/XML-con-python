import sqlite3
import xml.etree.ElementTree as ET

# Conexión a la base de datos
conn = sqlite3.connect('productos.db')
cursor = conn.cursor()

# Filtrar productos por ejemplo, por rango de precio
precio_min = 50.0
precio_max = 500.0
cursor.execute('SELECT * FROM productos WHERE precio BETWEEN ? AND ?', (precio_min, precio_max))
productos = cursor.fetchall()

# Crear el elemento raíz para el nuevo archivo XML
root = ET.Element('catalogo_filtrado')

# Añadir productos al XML
for producto in productos:
    prod_elem = ET.SubElement(root, 'producto')
    ET.SubElement(prod_elem, 'descripcion').text = str(producto[1])
    ET.SubElement(prod_elem, 'precio').text = str(producto[2])
    ET.SubElement(prod_elem, 'categoria').text = str(producto[3])
    ET.SubElement(prod_elem, 'stock').text = str(producto[4])
    ET.SubElement(prod_elem, 'modo_pago').text = str(producto[5])
    ET.SubElement(prod_elem, 'costo_envio').text = str(producto[6])

# Escribir el árbol XML a un archivo
tree = ET.ElementTree(root)
tree.write('catalogo_filtrado.xml', encoding='utf-8', xml_declaration=True)

conn.close()

print("Datos exportados exitosamente a catalogo_filtrado.xml")
