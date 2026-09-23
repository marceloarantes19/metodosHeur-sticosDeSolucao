from abc import ABC, abstractmethod
class Problema(ABC):
    """
    Classe abstrata base para problemas de otimização.
    Define os métodos obrigatórios que qualquer problema deve implementar
    para poder ser resolvido por heurísticas e metaheurísticas.
    """

    @abstractmethod
    def avalia(self, solucao):
        """Avalia a qualidade (fitness) de uma solução."""
        pass

    @abstractmethod
    def geraSolucaoAleatoria(self):
        """Gera uma solução aleatória válida para o problema."""
        pass

    @abstractmethod
    def geraVizinhos(self, solucao):
        """Gera vizinhos para uma dada solução (usado em busca local)."""
        pass


