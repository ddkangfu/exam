#coding=utf-8

class TreeNode(object):
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent #用来分析各节点之间的层级关系，无实际用途
        self.left = None
        self.middle = None
        self.right = None

    def __str__(self):
        return '%d[%s]' % (self.value, self.parent if self.parent else 'None')


class TriNaryTree(object):
    def __init__(self):
        self.root = None
     
    def _insert(self, node, parent, value):
        """
        递归在指定节点下插入指定值
        """        
        if node.value < value:
            if node.right:
                self._insert(node.right, node, value)
            else:
                node.right = TreeNode(value, node)
        elif node.value == value:
            if node.middle:
                self._insert(node.middle, node, value)
            else:
                node.middle = TreeNode(value, node)
        else:
            if node.left:
                self._insert(node.left, node, value)
            else:
                node.left = TreeNode(value, node)
    
    def _delete(self, node, value):
        """
        递归删除指定节点下的指定值
        """
        if not node:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.middle:
                node.middle = self._delete(node.middle, value)
            elif node.right and node.left:
                #从右子树里找到最小值作为被删节点的替换值
                min_node = self._find_min_node(node.right)
                node.value = min_node.value
                node.right = self._delete(node.right, min_node.value)
            else:
                if node.right:
                    tmp_node = node.right
                    del node #主动作一下垃圾回收
                    return tmp_node
                else:
                    tmp_node = node.left
                    del node #主动作一下垃圾回收
                    return tmp_node
        return node

    def _find_min_node(self, node):
        """
        查找节点下的最小值
        """
        return self._find_min_node(node.left) if node.left else node

    def _traversal(self, node, print_result):
        """
        遍历三叉树，用于组织显示的数据
        """
        if node:
            print_result.append(node.value)
            #print node
            self._traversal(node.left, print_result)
            self._traversal(node.middle, print_result)
            self._traversal(node.right, print_result)

    def insert(self, value):
        """
        对外接口，用于向三叉树插入指定值的节点
        """
        if self.root:
            self._insert(self.root, None, value)
        else:
            self.root = TreeNode(value)

    def delete(self, value):
        """
        对外接口，用于从三叉树中删除指值定节点
        """
        self._delete(self.root, value)

    def __str__(self):
        print_result = []
        self._traversal(self.root, print_result)
        return print_result.__str__()
