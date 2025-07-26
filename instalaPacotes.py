# Importa biblioteca pip
import pip

# Função para importar ou instalar os pacotes
def import_or_install(package_import, package_name):
    try:
        __import__(package_import)
    except ImportError:
        pip.main(['install', package_name])

# Dicionário com o nome do pacote que deve ser importado / instalado
# {package_import:package_name}
pacotes = {
    'pymysql':'pymysql',
    'python-dotenv':'python-dotenv',
    'pandas':'pandas'
}

for pacote in pacotes.items():
    import_or_install(pacote[0],pacote[1])
