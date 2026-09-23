import random
from Problema import Problema 
from Heuristica import Heuristica
class GeneticAlgorithm(Heuristica):
    def __init__(self, tamanhoPopulacao=50, geracoes=100, taxaMutacao=0.2):
        self.tamanhoPopulacao = tamanhoPopulacao
        self.geracoes = geracoes
        self.taxaMutacao = taxaMutacao
    def _cruzamento(self, pai1, pai2):
        if len(pai1) > 1:
            ponto = random.randint(1, len(pai1) - 1)
            filho1 = pai1[:ponto] + pai2[ponto:]
            filho2 = pai2[:ponto] + pai1[ponto:]
            return filho1, filho2
        return pai1.copy(), pai2.copy()
    def resolve(self, problema: Problema, maximize=True):
        populacao = [problema.geraSolucaoAleatoria() for _ in range(self.tamanhoPopulacao)]
        melhorSolucaoGlobal = None
        valorMelhorGlobal = float('-inf') if maximize else float('inf')
        fitnesses_iniciais = [problema.avalia(ind) for ind in populacao]
        for ind, fit in zip(populacao, fitnesses_iniciais):
            if (maximize and fit > valorMelhorGlobal) or (not maximize and fit < valorMelhorGlobal):
                valorMelhorGlobal = fit
                melhorSolucaoGlobal = ind

        # Ordena a população inicial para a seleção por ranqueamento (melhores primeiro)
        pop_com_fit_inicial = list(zip(populacao, fitnesses_iniciais))
        pop_com_fit_inicial.sort(key=lambda x: x[1], reverse=True if maximize else False)
        populacao = [ind for ind, fit in pop_com_fit_inicial]
        
        fitness_total_anterior = sum(fitnesses_iniciais)
        pesos_selecao = [self.tamanhoPopulacao - i for i in range(self.tamanhoPopulacao)]
        
        for _ in range(self.geracoes):
            filhos = []
            
            # 1. Cruzamento
            # Gera filhos a partir da população atual (com maior peso para os melhores)
            while len(filhos) < self.tamanhoPopulacao:
                pai1 = random.choices(populacao, weights=pesos_selecao, k=1)[0]
                pai2 = random.choices(populacao, weights=pesos_selecao, k=1)[0]
                f1, f2 = self._cruzamento(pai1, pai2)
                filhos.extend([f1, f2])
            
            # Trunca caso o tamanho tenha passado do limite (por adicionar de 2 em 2)
            filhos = filhos[:self.tamanhoPopulacao]

            # 2. Mutação
            for i in range(len(filhos)):
                if random.random() < self.taxaMutacao:
                    vizinhos = problema.geraVizinhos(filhos[i])
                    if vizinhos:
                        filhos[i] = random.choice(vizinhos)

            # 3. Preseleção (Didático) - A solução garante que os filhos sejam válidos
            filhos_preselecionados = []
            for filho in filhos:
                filhos_preselecionados.append(filho)

            # 4. Seleção
            pop_com_fit = [(ind, problema.avalia(ind)) for ind in populacao]
            filhos_com_fit = [(ind, problema.avalia(ind)) for ind in filhos_preselecionados]
            uniao_populacoes = pop_com_fit + filhos_com_fit
            uniao_populacoes.sort(key=lambda x: x[1], reverse=True if maximize else False)
            
            # Seleciona os N melhores para compor a nova população
            nova_populacao_com_fit = uniao_populacoes[:self.tamanhoPopulacao]
            
            melhor_da_geracao_fit = nova_populacao_com_fit[0][1]
            melhor_da_geracao_ind = nova_populacao_com_fit[0][0]
            
            fitness_total_nova = sum(fit for _, fit in nova_populacao_com_fit)
            
            # Sempre avalia e guarda o melhor global, pois break pode ocorrer
            if (maximize and melhor_da_geracao_fit > valorMelhorGlobal) or \
               (not maximize and melhor_da_geracao_fit < valorMelhorGlobal):
                valorMelhorGlobal = melhor_da_geracao_fit
                melhorSolucaoGlobal = melhor_da_geracao_ind
            
            # Condição de parada: se o fitness total da próxima geração não evolui, o sistema deve parar
            if (maximize and fitness_total_nova <= fitness_total_anterior) or \
               (not maximize and fitness_total_nova >= fitness_total_anterior):
                break
                
            # Atualiza para a próxima geração
            populacao = [ind for ind, fit in nova_populacao_com_fit]
            fitness_total_anterior = fitness_total_nova

        return melhorSolucaoGlobal, valorMelhorGlobal
