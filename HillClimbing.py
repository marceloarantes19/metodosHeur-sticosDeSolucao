from Problema import Problema 
from Heuristica import Heuristica
class HillClimbing(Heuristica):
    def __init__(self, maximoDeIteracoes=1000):
        self.maximoDeIteracoes = maximoDeIteracoes
    def resolve(self, problema: Problema, maximize=True):
        solucaoAtual = problema.geraSolucaoAleatoria()
        valorSolucaoAtual = problema.avalia(solucaoAtual)
        for _ in range(self.maximoDeIteracoes):
            vizinhos = problema.geraVizinhos(solucaoAtual)
            if not vizinhos:
                break
            melhorVizinho = None
            valorMelhorVizinho = float('-inf') if maximize else float('inf')
            for vizinho in vizinhos:
                valorVizinho = problema.avalia(vizinho)
                if (maximize and valorVizinho > valorMelhorVizinho) or (not maximize and valorVizinho < valorMelhorVizinho):
                    melhorVizinho = vizinho
                    valorMelhorVizinho = valorVizinho
            if (maximize and valorMelhorVizinho <= valorSolucaoAtual) or (not maximize and valorMelhorVizinho >= valorSolucaoAtual):
                break
            solucaoAtual = melhorVizinho
            valorSolucaoAtual = valorMelhorVizinho
        return solucaoAtual, valorSolucaoAtual
