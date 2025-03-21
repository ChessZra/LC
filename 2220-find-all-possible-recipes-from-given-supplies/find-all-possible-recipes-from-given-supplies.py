class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        N = len(recipes)
        res = []
        supplies_lookup = set(supplies)
        for i in range(N):
            
            for j in range(N):
                valid = True
                for ing in ingredients[j]:
                    if ing not in supplies_lookup:
                        valid = False
                        break
                if valid:
                    res.append(recipes[j])
                    supplies_lookup.add(recipes[j])

        return list(set(res))
