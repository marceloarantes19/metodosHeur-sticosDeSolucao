from abc import ABC, abstractmethod
from Problema import Problema
class Heuristica(ABC):
    """
    Classe abstrata base para Heurísticas/Metaheurísticas.
    """
    @abstractmethod
    def resolve(self, Problema: Problema):
        """Aplica a heurística ao problema para encontrar uma solução."""
        pass

# Teste de Commit
# teste 2
