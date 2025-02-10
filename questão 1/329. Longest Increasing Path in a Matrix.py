from typing import List

class Solution:
    
    def solve(self, i: int, j: int, matrix: List[List[int]], m: int, n: int, dp: List[List[int]]) -> int:
        """
        Função recursiva com memoização para encontrar o maior caminho crescente a partir da posição (i, j).

        Parâmetros:
        - i, j: Coordenadas atuais na matriz.
        - matrix: A matriz de entrada.
        - m, n: Dimensões da matriz.
        - dp: Matriz de memoização que armazena o maior caminho crescente a partir de cada célula.

        Retorna:
        - O comprimento do maior caminho crescente a partir da posição (i, j).
        """

        # Se já calculamos a solução para essa posição, retornamos o valor armazenado
        if dp[i][j] != -1:
            return dp[i][j]

        # Inicializamos a resposta como 0, pois vamos tentar expandir o caminho
        maior_caminho = 0

        # Direções possíveis: cima, direita, baixo, esquerda
        direcoes = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for di, dj in direcoes:
            novo_i, novo_j = i + di, j + dj  # Calculamos a nova posição

            # Verificamos se a nova posição está dentro dos limites da matriz e se há um valor crescente
            if 0 <= novo_i < m and 0 <= novo_j < n and matrix[novo_i][novo_j] > matrix[i][j]:
                # Chamamos recursivamente para expandir o caminho e atualizamos o maior valor encontrado
                maior_caminho = max(maior_caminho, self.solve(novo_i, novo_j, matrix, m, n, dp))

        # Armazena o resultado na matriz dp, adicionando 1 porque contamos a célula atual no caminho
        dp[i][j] = maior_caminho + 1
        return dp[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Encontra o maior caminho crescente em uma matriz.

        Parâmetros:
        - matrix: Matriz de inteiros onde buscamos o caminho crescente.

        Retorna:
        - O comprimento do maior caminho crescente possível.
        """

        if not matrix or not matrix[0]:  # Caso de matriz vazia
            return 0

        m, n = len(matrix), len(matrix[0])  # Dimensões da matriz
        
        # Criamos uma matriz `dp` para armazenar os resultados já calculados (-1 indica não calculado)
        dp = [[-1] * n for _ in range(m)]

        # Variável para armazenar o maior caminho encontrado
        maior_caminho_total = 0

        # Percorremos todas as células da matriz para encontrar o maior caminho possível a partir de cada ponto
        for i in range(m):
            for j in range(n):
                maior_caminho_total = max(maior_caminho_total, self.solve(i, j, matrix, m, n, dp))

        return maior_caminho_total
