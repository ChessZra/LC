class Directory:
    def __init__(self, name):
        self.sub_directories = []
        self.max_length = -1
        self.name = name

class Solution:
    def lengthLongestPath(self, input_string: str) -> int:
        input_string = '\n' + input_string
        N = len(input_string)
        stk = [(Directory(''), -1)]     
        index = 0
        while index < N:
            assert(input_string[index] == '\n')
            index += 1

            tabs = 0
            while input_string[index] == '\t':
                tabs += 1
                index += 1

            directory_name = ''
            while index < N and input_string[index] != '\n' and input_string[index] != '\t':
                directory_name += input_string[index]
                index += 1

            # Get current directory
            while tabs <= stk[-1][1]:
                stk.pop()
            
            cur = stk[-1][0]
            if directory_name.find('.') != -1: # it's a file
                cur.max_length = max(cur.max_length, len(directory_name))
            else: # It's a directory
                d = Directory(directory_name)
                cur.sub_directories.append(d)
                stk.append((d, tabs))
        
        res = 0
        def dfs(directory, cur_length):
            nonlocal res

            if directory.max_length != -1:
                res = max(res, 1 + directory.max_length + cur_length)

            for neighbor in directory.sub_directories:
                dfs(neighbor, 1 + len(neighbor.name) + cur_length)

        dfs(stk[0][0], len(stk[0][0].name))

        return res - 1 if res > 0 else 0

