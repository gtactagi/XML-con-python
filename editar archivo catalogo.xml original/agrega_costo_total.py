import xml.etree.ElementTree as ET

# Cargar y parsear el archivo XML modificado
tree = ET.parse('catalogo_modificado.xml')
root = tree.getroot()

# Iterar sobre todos los productos para agregar el campo costo_total
for producto in root.findall('producto'):
    precio = float(producto.find('precio').text)
    costo_envio = float(producto.find('costo_envio').text)
    costo_total = precio + costo_envio
    
    # Crear el nuevo elemento costo_total
    costo_total_elem = ET.SubElement(producto, 'costo_total')
    costo_total_elem.text = str(costo_total)

# Guardar el archivo XML con el nuevo campo
tree.write('catalogo_con_costo_total.xml', encoding='utf-8', xml_declaration=True)

print("Campo costo_total agregado y guardado en catalogo_con_costo_total.xml")