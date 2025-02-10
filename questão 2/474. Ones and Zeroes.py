from functools import cache  # Importamos cache para otimizar a recursão com memoização
import math
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Dado um conjunto de strings contendo apenas '0's e '1's, 
        e duas restrições: um limite de '0's (m) e um limite de '1's (n),
        queremos encontrar o maior subconjunto de strings que podemos formar 
        sem ultrapassar esses limites.
        """

        # Criamos uma lista de contagem de zeros e uns para cada string.
        # Assim, para cada string `s`, armazenamos (quantidade de '0's, quantidade de '1's).
        counter = [[s.count("0"), s.count("1")] for s in strs]

        # Função de Programação Dinâmica com Memoização
        @cache  # Memoização automática para evitar cálculos repetidos
        def dp(zeros_restantes: int, uns_restantes: int, idx: int) -> int:
            """
            Parâmetros:
            - zeros_restantes: Quantos '0's ainda podemos usar.
            - uns_restantes: Quantos '1's ainda podemos usar.
            - idx: Índice da string atual em `strs` que estamos analisando.

            Retorna:
            - O tamanho máximo do subconjunto que podemos formar a partir do índice `idx`.
            """

            # Caso base: Se ultrapassarmos os limites de '0's ou '1's, retornamos -∞ 
            # para garantir que essa escolha não seja válida.
            if zeros_restantes < 0 or uns_restantes < 0:
                return -math.inf

            # Caso base: Se já analisamos todas as strings, retornamos 0, pois não há mais o que escolher.
            if idx == len(strs):
                return 0
            
            # Opção 1: Ignorar a string atual e passar para a próxima
            opcao_ignorar = dp(zeros_restantes, uns_restantes, idx + 1)

            # Opção 2: Escolher a string atual (se for possível dentro dos limites)
            zeros_atuais, uns_atuais = counter[idx]  # Pegamos a contagem da string atual
            opcao_escolher = 1 + dp(zeros_restantes - zeros_atuais, uns_restantes - uns_atuais, idx + 1)

            # Retornamos o melhor dos dois casos: pegar ou ignorar a string
            return max(opcao_ignorar, opcao_escolher)

        # Chamamos a função recursiva começando do índice 0 e com `m` zeros e `n` uns disponíveis.
        return dp(m, n, 0)