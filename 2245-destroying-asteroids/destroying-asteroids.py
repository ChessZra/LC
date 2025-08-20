class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in range(len(asteroids)):
            if asteroids[i] > mass:
                return False
            mass += asteroids[i]
        return True