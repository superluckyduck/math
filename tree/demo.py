from collections import deque
from typing import Optional
class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val: int = val                # 节点值
        self.left: Optional[TreeNode] = None  # 左子节点引用
        self.right: Optional[TreeNode] = None # 右子节点引用
def list_to_tree_dfs(arr: list[int], i: int) -> Optional[TreeNode]:
    """将列表反序列化为二叉树：递归"""
    # 如果索引超出数组长度，或者对应的元素为 None ，则返回 None
    if i < 0 or i >= len(arr) or arr[i] is None:
        return None
    # 构建当前节点
    root = TreeNode(arr[i])
    # 递归构建左右子树
    root.left = list_to_tree_dfs(arr, 2 * i + 1)
    root.right = list_to_tree_dfs(arr, 2 * i + 2)
    return root

def list_to_tree(arr: list[int]) -> Optional[TreeNode]:
    """将列表反序列化为二叉树"""
    return list_to_tree_dfs(arr, 0)


def level_order(root: Optional[TreeNode]) -> list[int]:
    """层序遍历"""
    # 初始化队列，加入根节点
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node: TreeNode = queue.popleft()  # 队列出队
        res.append(node.val)  # 保存节点值
        if node.left is not None:
            queue.append(node.left)  # 左子节点入队
        if node.right is not None:
            queue.append(node.right)  # 右子节点入队
    return res
def pre_order(root: TreeNode | None):
    """前序遍历"""
    if root is None:
        return
    # 访问优先级：根节点 -> 左子树 -> 右子树
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)

def in_order(root: TreeNode | None):
    """中序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 根节点 -> 右子树
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)

def post_order(root: TreeNode | None):
    """后序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 右子树 -> 根节点
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)

"""Driver Code"""
if __name__ == "__main__":
    # 初始化二叉树
    # 这里借助了一个从数组直接生成二叉树的函数
    root = list_to_tree(arr=[1, 2, 3, 4, 5, 6, 7])
    # 层序遍历
    res = level_order(root)
    print("\n层序遍历的节点打印序列 = ", res)
    res.clear()
    pre_order(root)
    print("\n前序遍历的节点打印序列 = ", res)