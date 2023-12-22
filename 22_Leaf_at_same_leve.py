class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
  
    def check(self, root):
        if root is None:
            return True
        q=[(root,0)]
        first_level = None
        while q:
            curr, level = q.pop(0)
            if not curr.left and not curr.right:
                if first_level is None:
                    first_level = level
                else:
                    if first_level!=level:
                        return False
            if curr.left: q.append((curr.left, level + 1))
            if curr.right: q.append((curr.right, level + 1))
        return True
