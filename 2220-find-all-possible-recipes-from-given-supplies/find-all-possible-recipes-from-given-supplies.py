class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                if recipes[i] not in graph:
                    graph[recipes[i]] = []
                graph[recipes[i]].append(ingredients[i][j])

        supplies_lookup = set(supplies)
        recipes_lookup = set(recipes)
        visited = []
        @cache
        def can(node):
            if node in supplies_lookup:
                return True
            
            if node not in recipes_lookup or node in visited:
                return False

            visited.append(node)
            for neighbor in graph.get(node, []):
                if not can(neighbor):
                    return False
            visited.pop()
            return True
        
        res = []
        for rec in recipes:
            visited.clear()
            if can(rec):
                res.append(rec)

        return res
