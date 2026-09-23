import math
import random
from Problema import Problema 
from Heuristica import Heuristica
class SimulatedAnnealing(Heuristica):
    def __init__(self, temperaturaInicial=1000.0, taxaResfriamento=0.95 \
                                                , maximoDeIteracoes=1000):
        self.temperaturaInicial = temperaturaInicial
        self.taxaResfriamento = taxaResfriamento
        self.maximoDeIteracoes = maximoDeIteracoes
        self.agenda = []
        temp = self.temperaturaInicial
        for _ in range(self.maximoDeIteracoes):
            self.agenda.append(temp)
            temp *= self.taxaResfriamento
        
    def gera_vizinho_distancia(self, solucao, temperatura):
        n = len(solucao)
        distancia = max(1, int((temperatura / self.temperaturaInicial) * n))
        vizinho = list(solucao)
        num_para_mudar = random.randint(1, min(distancia, n))
        indices_para_mudar = random.sample(range(n), num_para_mudar)
        for i in indices_para_mudar:
            vizinho[i] = 1 - vizinho[i]
        return vizinho
        
    def resolve(self, problema: Problema, maximize=True):
        solucaoAtual = problema.geraSolucaoAleatoria()
        valorSolucaoAtual = problema.avalia(solucaoAtual)
        melhorSolucao = solucaoAtual
        valorMelhorSolucao = valorSolucaoAtual
        for temperatura in self.agenda:
            vizinho = self.gera_vizinho_distancia(solucaoAtual, temperatura)
            valorVizinho = problema.avalia(vizinho)
            delta = (valorVizinho - valorSolucaoAtual) if maximize else \
                    (valorSolucaoAtual - valorVizinho)
            if delta > 0:
                solucaoAtual = vizinho
                valorSolucaoAtual = valorVizinho
                if (maximize and valorSolucaoAtual > valorMelhorSolucao) or \
                   (not maximize and valorSolucaoAtual < valorMelhorSolucao):
                    melhorSolucao = solucaoAtual
                    valorMelhorSolucao = valorSolucaoAtual
            else:
                probabilidadeAceitacao = math.exp(delta / temperatura)
                if random.random() < probabilidadeAceitacao:
                    solucaoAtual = vizinho
                    valorSolucaoAtual = valorVizinho
        return melhorSolucao, valorMelhorSolucao
