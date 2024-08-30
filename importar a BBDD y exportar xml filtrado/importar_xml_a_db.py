import sqlite3
import xml.etree.ElementTree as ET

# Conexión a la base de datos SQLite (se creará si no existe)
conn = sqlite3.connect('productos.db')
cursor = conn.cursor()

# Crear la tabla de productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    descripcion TEXT,
    precio REAL,
    categoria TEXT,
    stock INTEGER,
    modo_pago TEXT,
    costo_envio REAL
)
''')

# Parsear el archivo XML
tree = ET.parse('catalogo.xml')
root = tree.getroot()

# Insertar los datos en la base de datos
for producto in root.findall('producto'):
    descripcion = producto.find('descripcion').text
    precio = float(producto.find('precio').text)
    categoria = producto.find('categoria').text
    stock = int(producto.find('stock').text)
    modo_pago = producto.find('modo_pago').text
    costo_envio = float(producto.find('costo_envio').text)

    cursor.execute('''
    INSERT INTO productos (descripcion, precio, categoria, stock, modo_pago, costo_envio)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (descripcion, precio, categoria, stock, modo_pago, costo_envio))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos importados exitosamente a la base de datos.")