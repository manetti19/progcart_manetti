
import matplotlib.pyplot as plt
def plotar_grafico_barras(dados, titulo="Grafico de Barras",
xlabel="Categorias", ylabel="Valores",
rotacao_labels=0, salvar_em="plot.png"):


    # Separando chaves e valores
    labels = list(dados.keys())
    valores = list(dados.values())
    # Plot
    plt.figure() # Inicializa ´area de desenho.
    plt.bar(labels, valores) # Gr´afico de barras.
    plt.xlabel(xlabel) # Descri¸c~ao do eixo x.
    plt.ylabel(ylabel) # Descri¸c~ao do eixo y.
    plt.title(titulo) #T´ıtulo do plot.
    plt.xticks(rotation=rotacao_labels) # Textos do eixo X.
    plt.tight_layout() # Reduz espa¸cos
    plt.savefig(salvar_em) # Salva o gr´afico em um arquivo.
    plt.show() # Abre a janela interativa.
    return

dados = {
"Aprendizado profundo": 10,
"GNSS": 9,
"Sensoriamento remoto": 6,
"Fotogrametria": 5,
"SIG": 7,
"Programacao desktop": 7,
"Programacao web backend": 8,
"Programacao web frontend": 5,
"Producao cartografica": 6,
"Batimetria": 2
}


plotar_grafico_barras(dados, titulo="Habilidades do Mauricio",
xlabel="Habilidades", ylabel="Pontuacao",
rotacao_labels=90, salvar_em="plot.png")

