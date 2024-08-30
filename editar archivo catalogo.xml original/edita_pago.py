import xml.etree.ElementTree as ET

# Cargar y parsear el archivo XML
tree = ET.parse('catalogo.xml')
root = tree.getroot()

# Iterar sobre todos los productos para cambiar la etiqueta
for producto in root.findall('producto'):
    modo_pago_elem = producto.find('modo_pago')
    if modo_pago_elem is not None:
        modo_pago_elem.tag = 'pago_por'

# Guardar el archivo XML modificado
tree.write('catalogo_modificado.xml', encoding='utf-8', xml_declaration=True)

print("Etiqueta cambiada de modo_pago a pago_por y guardada en catalogo_modificado.xml")