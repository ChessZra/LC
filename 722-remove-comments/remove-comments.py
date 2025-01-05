class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # Third submission code:

        # Turn source into a string
        source_code = ""
        N = len(source)
        for i in range(N):
            source_code += source[i]
            if i != N - 1:
                source_code += '\n'
        
        # print("Source code")
        # print(source_code)

        # Parse it
        res = ""
        N = len(source_code)
        i = 0
        while i < N:
            if i + 1 < N and source_code[i:i+2] in ['//', '/*']:
            
                if source_code[i:i+2] == '//': # Single line comment
                    j = i + 2
                    while j < N and source_code[j] != '\n':
                        j += 1
                    if j < N and source_code[j] == '\n' and (i > 0 and source_code[i - 1] == '\n' or i == 0):
                        j += 1
                    i = j
                elif source_code[i:i+2] == '/*': # Mutli line comment
                    j = i + 2
                    while j < N - 1 and source_code[j:j+2] != '*/':
                        j += 1
                    j += 2
                    if j < N and source_code[j] == '\n' and (i > 0 and source_code[i - 1] == '\n' or i == 0):
                        j += 1
                    i = j
                continue
            
            res += source_code[i]
            i += 1
        
        # print("res code")
        # print(res)

        answer = res.split("\n")
        removed_blank = []
        for ans in answer:
            if len(ans) == 0: continue
            removed_blank.append(ans)

        return removed_blank   