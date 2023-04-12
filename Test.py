import pkg_resources

# nome do módulo que você quer verificar a versão
nome_modulo = "psutil"

try:
    # obter a distribuição (que contém informações sobre o módulo)
    distribuicao = pkg_resources.get_distribution(nome_modulo)
    # imprimir a versão
    print(f"A versão do módulo {nome_modulo} é {distribuicao.version}")
except pkg_resources.DistributionNotFound:
    print(f"O módulo {nome_modulo} não está instalado.")
