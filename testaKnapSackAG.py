from Problema import Problema
from KnapsackProblem import KnapsackProblem
from GeneticAlgorithm import GeneticAlgorithm

capacidade = 12
peso = [4, 6, 3, 2]
valores = [5, 7, 9, 6]

solucionador = GeneticAlgorithm(tamanhoPopulacao=6, geracoes=4, taxaMutacao=0.2)
pMochila = KnapsackProblem(capacidade, peso, valores)
melhor_solucao, melhor_valor = solucionador.resolve(pMochila, maximize=True)

print("Melhor solução: ", melhor_solucao)
print("Melhor valor: ", melhor_valor)
