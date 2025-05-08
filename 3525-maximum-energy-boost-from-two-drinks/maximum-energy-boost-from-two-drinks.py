class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        N = len(energyDrinkA)

        @cache
        def drinkA(index):
            if index >= N:
                return 0
            
            return energyDrinkA[index] + max(drinkA(index + 1), drinkB(index + 2))

        @cache
        def drinkB(index):
            if index >= N:
                return 0

            return energyDrinkB[index] + max(drinkB(index + 1), drinkA(index + 2))

        return max(drinkA(0), drinkB(0))