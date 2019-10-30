class Solution(object):

    def rec(self, board, word, i, j, level, m):
        """
        If I reach the end of the word level will be equal to length of the word
        now I have to check if the last letter is equal to the recusrion level's i and j
        if it is not then just return false ...
        If it is i.e the word is the last word and is equal to the board[i][j] we have found the word ...return true
        """
        if level == len(word) - 1:
            if board[i][j] == word[level]:
                return True
            else:
                return False
        # only recurse if the current letter word[level] is equal to (i,j) on board.. i.e go in to next level
        # only if letter metches. If letter does not match this recursion will return false
        if board[i][j] == word[level]:
            m[(i,j)] = True
            left = False
            right = False
            top = False
            bottom = False
            # only recurse if i and j are in bounds and are not visited
            if self.inBounds(i, j - 1, board) and not m.get((i, j - 1)):
                left = self.rec(board, word, i, j-1, level+1, m)
            if self.inBounds(i, j + 1, board) and not m.get((i, j + 1)):
                right = self.rec(board, word, i, j+1, level+1, m)
            if self.inBounds(i + 1, j, board) and not m.get((i + 1, j)):
                top = self.rec(board, word, i+1, j, level+1, m)
            if self.inBounds(i - 1, j, board) and not m.get((i - 1, j)):
                bottom = self.rec(board, word, i-1, j, level+1, m)
            return left or right or top or bottom

        return False



    def existsRec(self, board, word):
        l = []
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == word[0]:
                    # append word[0] tuple to the list (i,j)
                    l.append((i, j))

        for pair in l:
            i = pair[0]
            j = pair[1]
            m = {}
            exist = self.rec(board, word, i, j, 0, m)
            print(exist)

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        """
        get the first element in the word in the board. There can be multiple starting points
        All these become roots. Append these tuples (i,j) in a list
        below list will contain two tuples (two roots) corresponding to the two starting points of BFS search
        """
        l = []
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == word[0]:
                    # append word[0] tuple to the list (i,j)
                    l.append((i, j))

        print(l)
        pair = l[0]
        m = {pair: True}
        print(m)
        tuple = (0,0)
        print(m.get(tuple))

        """
        To perform BFS initialize a queue
        """
        q = []
        # loop through the list of roots
        for k in range(0, len(l)):
            # get first root
            root = l[k]
            # append in q
            q.append(root)
            # visited map
            m = {}
            level = 0
            # if level of the BFS tree is same as length of the word we have found the word
            found = False
            while q:
                # we will push each level into the Q hence get the size of Q
                size = len(q)
                print(q)
                # we have found the word
                if level >= len(word):
                    found = True
                    break
                # from n=0 to size of Q remove from Q and push the next level
                for n in range(0,size):
                    node = q.pop(0)
                    m[node] = True
                    i = node[0]
                    j = node[1]
                    if word[level] != board[i][j]:
                        continue
                    if self.inBounds(i,j-1, board) and not m.get((i, j - 1)):
                        q.append((i, j - 1))
                    if self.inBounds(i,j+1, board) and not m.get((i, j + 1)):
                        q.append((i, j + 1))
                    if self.inBounds(i+1,j, board) and not m.get((i + 1, j)):
                        q.append((i+1, j))
                    if self.inBounds(i-1,j, board) and not m.get((i-1, j)):
                        q.append((i-1, j))
                print(level)
                level = level+1

            if found:
                print("true")
            else:
                print("false")



    def inBounds(self, i, j , board):
        leni = len(board)
        lenj = len(board[0])
        if i>=0 and j>=0 and i<leni and j<lenj:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    #sol.exist(board, word)
    sol.existsRec(board, word)