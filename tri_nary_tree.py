#coding=utf-8


class TreeNode(object):
    #print_result = []
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.middle = None
        self.right = None

    def __str__(self):
        return '%d[%s]' % (self.value, self.parent if self.parent else 'None')

class TriNaryTree(object):
    def __init__(self):
        self.root = None

    def _search(self, node, value):
        result = None
        if node:
            if node.value == value:
                return node
            
            if node.left:
                result = self._search(node.left, value)

            if node.right:
                result = self._search(node.right, value)
        return result
     
    def _insert(self, node, parent, value):
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
    """
    def _delete(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            print node
            if node.middle:
                #tmp_middle_node = node.middle
                #while tmp_middle_node:
                #    tmp_middle_node2 = tmp_middle_node.middle
                #    del tmp_middle_node
                #    tmp_middle_node = tmp_middle_node2
                    #node = node.middle
                #self._delete_middle(node)
                node.middle = self._delete(node.middle, value)
            elif node.right and node.left:
                min_node = self._find_min_node(node.right)
                node.value = min_node.value
                node.right = self._delete(node.right, min_node.value)
            else:
                #node = node.left
                #node = node.right if node.right else node.left
                if node.right:
                    node = node.right
                    #elif node.left:
                else:
                    node = node.left
                #else:
                #    node = node.parent
                #else:
                #    parent = node.parent
                #    del node
                #    return parent
        return node
    """
    def _delete(self, node, value):
        if not node:
            return None

        if node.value == value:
            if (not node.left) and (not node.middle) and (not node.right):
                del node
                return None

            if node.middle:
                node.middle = self._delete(node.middle, value)
            else:
                if not node.left:
                    right_child = node.right
                    del node
                    return right_child
                elif not node.right:
                    left_child = node.left
                    del node
                    return left_child
                else:
                    delete_node = self._find_min_node(node.right)
                    node.value = delete_node.value
                    node.right = self._delete(node.right, delete_node.value)
        elif node.value > value:
            node.left = self._delete(node.left, value)
        else:
            node.right = self._delete(node.right, value)

        return node


    def _delete_middle(self, node):
        middle_node = self._delete_middle(node.middle)
        if not middle_node:
            del node
        return middle_node
    
    """
    def _delete(self, node, value):
        if node:
            tmp_node = _search(self.root, value)
            if tmp_node:
                if tmp_node.middle:
                    while tmp_node.middle:
                        tmp_node = tmp_node.middle
                    _adjust_parent_barnch(tmp_node.parent, tmp_node, None)
                else:
                    replace_node = None
                    if tmp_node.left:
                        replace_node = self._find_max_node(tmp_node.left)
                        if replace_node:
                            replace_node_left = replace_node.left
                            replace_node_parent = replace_node.parent

                            if replace_node != tmp_node.left:
                                if replace_node.value == tmp_node.left.value:
                                    replace_node.middle = tmp_node.left
                                else:
                                    replace_node.left = tmp_node.left
                            replace_node.right = tmp_node.right
                            replace_node.parent = tmp_node.parent

                            if tmp_node.parent:
                                _adjust_parent_barnch(tmp_node.parent, tmp_node, replace_node)

                            _adjust_branch_parent(tmp_node, replace_node)

                            _adjust_parent_barnch(replace_node_parent, replace_node, replace_node_left)
                    elif tmp_node.right:
                        replace_node = self._find_min_node(tmp_node.right)
                        if replace_node:
                            replace_node_right = replace_node.right
                            replace_node_parent = replace_node.parent

                            if replace_node != tmp_node.right:
                                if replace_node.value == tmp_node.right:
                                    replace_node.middle = tmp_node.right
                                else:
                                    replace_node.right = tmp_node.right
                            replace_node.left = tmp_node.left
                            replace_node.parent = tmp_node.parent
                            if tmp_node.parent:
                                _adjust_parent_barnch(tmp_node.parent, tmp_node, replace_node)
                            _adjust_branch_parent(tmp_node, replace_node)
                            _adjust_parent_barnch(replace_node_parent, replace_node, replace_node_right)
                    else:
                        _adjust_parent_barnch(tmp_node.parent, tmp_node, None)

                    if (node == tmp_node):
                        node = replace_node
    """
    

    def _find_min_node(self, node):
        return self._find_min_node(node.left) if node.left else node

    def _find_max_node(self, node):
        return self._find_min_node(node.left) if node.left else node

    def _print(self, node, print_result):
        if node:
            print_result.append(node.value)
            print 'Node=%d, Parent=%s' % (node.value, node.parent.value if node.parent else 'None')
            self._print(node.left, print_result)
            self._print(node.middle, print_result)
            self._print(node.right, print_result)


    def insert(self, value):
        if self.root:
            self._insert(self.root, None, value)
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
    print '[5, 4, 9, 5, 7, 2, 2] insert:'
    print t

    #t1 = t._search(t.root, 9)
    #print t1
    
    t.delete(5)
    print '4 delted:'
    print t

    t.delete(5)
    print t