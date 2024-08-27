import xml.etree.ElementTree as ET

# Caminho absoluto que você quer substituir
old_path = "/home/marlon/projeto_engenharia_2/SIGApoio/proj_SIGApoio"
new_path = "proj_SIGApoio/"

# Carrega o arquivo XML
tree = ET.parse('coverage.xml')
root = tree.getroot()

# Substitui o caminho nas tags <source>
for source in root.findall(".//sources/source"):
    if source.text:
        source.text = source.text.replace(old_path, new_path)

# Salva o arquivo XML modificado
tree.write('coverage.xml')