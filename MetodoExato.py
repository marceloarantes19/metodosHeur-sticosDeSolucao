from Problema import Problema
from Heuristica import Heuristica
import itertools
class MetodoExato(Heuristica):
    """
    Método Exato (Força Bruta/Enumeração).
    Gera todas as combinações possíveis para o problema
    e avalia cada uma para encontrar a solução ótima global.
    """
    def __init__(self, tipo='produto', elementos=None):
        if elementos is None:
            elementos = [0, 1]
        self.tipo = tipo
        self.elementos = elementos

    def resolve(self, problema: Problema, maximize=True):
        solucao_base = problema.geraSolucaoAleatoria()
        is_dict = isinstance(solucao_base, dict)
        
        if is_dict:
            keys = list(solucao_base.keys())
            values = list(solucao_base.values())
        else:
            values = solucao_base
            
        n = len(values)
        
        if self.tipo == 'produto':
            gerador = itertools.product(self.elementos, repeat=n)
        elif self.tipo == 'permutacao':
            gerador = itertools.permutations(values)
        else:
            raise ValueError(f"Tipo de enumeração '{self.tipo}' não suportado.")
            
        melhor_solucao = None
        melhor_valor = float('-inf') if maximize else float('inf')
        
        for combinacao in gerador:
            if is_dict:
                solucao_atual = dict(zip(keys, combinacao))
            else:
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
