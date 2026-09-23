from Problema import Problema
from Heuristica import Heuristica
import itertools
class MetodoExato(Heuristica):
    """
    Método Exato (Força Bruta/Enumeração).
    Gera todas as combinações binárias possíveis para o problema
    e avalia cada uma para encontrar a solução ótima global.
    """
    def resolve(self, problema: Problema, maximize=True):
        # Descobre o tamanho (n) do problema gerando uma solução aleatória
        solucao_base = problema.geraSolucaoAleatoria()
        n = len(solucao_base)
        
        melhor_solucao = None
        melhor_valor = float('-inf') if maximize else float('inf')
        
        # itertools.product([0, 1], repeat=n) gera todas as 2^n combinações binárias possíveis
        for combinacao in itertools.product([0, 1], repeat=n):
            solucao_atual = list(combinacao)
            valor_atual = problema.avalia(solucao_atual)
            
            if maximize:
                if valor_atual > melhor_valor:
                    melhor_valor = valor_atual
                    melhor_solucao = solucao_atual
            else:
                if valor_atual < melhor_valor:
                    melhor_valor = valor_atual
                    melhor_solucao = solucao_atual
                    
        return melhor_solucao, melhor_valor
