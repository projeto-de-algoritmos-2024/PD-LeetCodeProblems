class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])

        # Inicializa um array DP 1D onde min_cost[col] representa o custo mínimo
        # para alcançar a coluna 'col' na linha atual
        min_cost = [0] * num_cols
        min_cost[0] = grid[0][0]  # Ponto de partida

        # Inicializa a primeira linha do array DP
        for col in range(1, num_cols):
            # Só pode mover para a direita na primeira linha
            min_cost[col] = min_cost[col - 1] + grid[0][col]

        # Itera através de cada linha começando da segunda linha
        for row in range(1, num_rows):
            # Atualiza a primeira coluna para a linha atual (só pode vir de cima)
            min_cost[0] += grid[row][0]
            for col in range(1, num_cols):
                # Escolhe o custo mínimo entre vir da esquerda ou de cima
                min_cost[col] = grid[row][col] + min(min_cost[col], min_cost[col - 1])

        # O último elemento em min_cost terá o custo mínimo do caminho para alcançar o canto inferior direito
        return min_cost[-1]