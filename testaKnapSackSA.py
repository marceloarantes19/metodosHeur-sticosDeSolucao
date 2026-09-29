from Problema import Problema
from KnapsackProblem import KnapsackProblem
from SimulatedAnnealing import SimulatedAnnealing
peso = [5, 8, 10, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25]
valores = [11, 17, 21, 25, 29, 31, 35, 37, 39, 41, 43, 45, 47, 49, 50]
capacidade = 127

solucionador = SimulatedAnnealing(temperaturaInicial=5000, taxaResfriamento=0.98\
                                , maximoDeIteracoes=1000)
pMochila = KnapsackProblem(capacidade, peso, valores)
melhor_solucao, melhor_valor = solucionador.resolve(pMochila, maximize=True)

print("Melhor solução: ", melhor_solucao)
print("Melhor valor: ", melhor_valor)

