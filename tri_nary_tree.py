#coding=utf-8


class TreeNode(object):
    #print_result = []
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None


class TriNaryTree(object):
    def __init__(self):
        self.root = None

    def _search(self, value):
        pass

    def _insert(self, node, value):
        if node.value < value:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = TreeNode(value)
        elif node.value == value:
            if node.middle:
                self._insert(node.middle, value)
            else:
                node.middle = TreeNode(value)
        else:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = TreeNode(value)
    """
    def _delete(self, node, value):
        if not node:
            return node

        if node.value < value:
            node.right = self._delete(node.right, value)
        elif node.value > value:
            node.left = self._delete(node.left, value)
        else:
            if (not node.right) and (not node.middle) and (not node.middle):
                del node
                return None

            if node.middle:
                node.middle = self._delete(node.middle, value)
            else:
                #if node.right and node.left:
                #    s_node = _find(node.right)
                #    node.value = s_node.value
                #    node.right = delete(node.right, s_node.value)
                #elif node.left:
                #    new_node = node.left
                #    del node
                #    return new_node
                #else:
                #    new_node = node.right
                #    del node
                #    return new_node
                if node.right:
                    left_node = self._find(node.right)
                    node.value = left_node.value
                    node.right = self._delete(node.right, left_node.value)
                else:
                    node = node.left
        return node
    """
    
    def _delete(self, node, value):
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
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right = self._delete(node.right, min_node.value)
            else:
                #node = node.left
                node = node.right if node.right else node.left

        return node

    def _find_min(self, node):
        return _find(node.left) if node.left else node

    def _print(self, node, print_result):
        if node:
            print_result.append(node.value)
            print 'Node=%d' % node.value
            self._print(node.left, print_result)
            self._print(node.middle, print_result)
            self._print(node.right, print_result)

    def insert(self, value):
        if self.root:
            self._insert(self.root, value)
        else:
            self.root = TreeNode(value)

    def delete(self, value):
        self._delete(self.root, value)

    def __str__(self):
        print_result = []
        self._print(self.root, print_result)
        return print_result.__str__()


if __name__ == '__main__':
    t = TriNaryTree()
    a = [5, 4, 9, 5, 7, 2, 2]
    for x in a:
        t.insert(x)
    print t