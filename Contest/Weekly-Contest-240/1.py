class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0 for _ in range(101)]
        for (birth, death) in logs:
            for i in range(birth-1950, death-1950):
                population[i] += 1
        print(population)
        return population.index(max(population))+1950
