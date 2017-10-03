# 深度优先和广度优先
#### 深度优先（递归算法实现）
**深度优先过程：**
```Python
def depth_tree(tree_node):
    if tree_node is not None:
        print(tree_node._data)
        if tree_node._left is not None:
            return depth_tree(tree_node._left)
        if tree_node._right is not None:
            return depth_tree(tree_node_right)
```
要设置跳出，不能栈太深，否则会栈溢出

#### 广度优先（队列算法实现）
**广度优先过程：**
```Python
def level_queue(root):
    if root is None:
        return
    my_queue = [ ]
    node =root
    my_queue.append(node)
    while my_queue:
        node = my_queue.pop(0)
        print(node.elem)
        if node.lchild is not None:
            my_queue.append(node.lchild)
        if node.rchild is not None:
            my_queue.append(node.rchild)
```