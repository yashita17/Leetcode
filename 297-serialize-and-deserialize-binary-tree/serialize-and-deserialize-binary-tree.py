# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        ans = []
        def dfs(root):
            if not root:
                ans.append("None")
                return
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(ans)
        

    def deserialize(self, data):
        value = data.split(",")
        i = [0]
        def dfs():
            if value[i[0]] == "None":
                i[0] +=1
                return None
            node = TreeNode(int(value[i[0]]))
            i[0] +=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))