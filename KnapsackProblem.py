from Problema import Problema
import random

class KnapsackProblem(Problema):
    """
    Problema da Mochila (Knapsack Problem).
    Dado um conjunto de itens, cada um com um peso e um valor,
    o objetivo é determinar o número de cada item a incluir em uma coleção
    para que o peso total seja menor ou igual a um determinado limite
    e o valor total seja o maior possível.
    """
    def __init__(self, capacidade, peso, valores):
        self.capacidade = capacidade
        self.peso = peso
        self.valores = valores
        self.n = len(peso)

    def avalia(self, solucao):
        """
        Avalia o valor total da mochila.
        Se o peso exceder a capacidade, o valor será penalizado com -infinito
        (inviabilizando a solução).
        """
        peso_total = sum(self.peso[i] for i in range(self.n) if solucao[i] == 1)
        valor_total = sum(self.valores[i] for i in range(self.n) if solucao[i] == 1)
        
        if peso_total > self.capacidade:
            return -float('inf') # Penalidade máxima para soluções inválidas
        
        return valor_total

    def geraSolucaoAleatoria(self):
        """Gera uma representação binária aleatória dos itens na mochila."""
        return [random.choice([0, 1]) for _ in range(self.n)]

    def geraVizinhos(self, solucao):
        """Gera vizinhos invertendo a decisão de inclusão de um item."""
        vizinhos = []
        for i in range(self.n):
            vizinho = list(solucao)
            vizinho[i] = 1 - vizinho[i]
            vizinhos.append(vizinho)
        return vizinhos
