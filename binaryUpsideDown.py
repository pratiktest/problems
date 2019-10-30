class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Solution:
    def upsideDown(self, root, roots_left, roots_right):
        if not root:
            return None
        if not roots_left:
            return root
        right = roots_left.right
        left = roots_left.left

        ## flip algorithm simple but we loose roots_left.right so we store above
        roots_left.right = root
        roots_left.left = roots_right

        return self.upsideDown(roots_left, left, right)




if __name__ == '__main__':
    print("hello")
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t2.left = t4
    t1.right = t3
    t2.right = t5
    """
    Input: [1,2,3,4,5]

            1
           / \
          2   3
         / \
        4   5
    """
    s = Solution()
    right = t1.right
    t1.right = None
    root = s.upsideDown(t1, t2, right)
    print(root.val)

