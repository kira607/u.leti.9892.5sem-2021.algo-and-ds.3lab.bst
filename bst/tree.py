from typing import Iterator, Optional, Type, Any, Generator

from bst.node import BstNode


class _MISSING(object):
    pass


class BST:
    def __init__(self, *args) -> None:
        self.root = None
        for arg in args:
            self.insert(arg)

    def contains(self, value: int) -> bool:
        self.__check_type(value)
        return bool(self.get(value))

    def insert(self, value: int) -> BstNode:
        self.__check_type(value)
        if self.root is None:
            return self._init(value)

        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BstNode(value)
                    return current_node.left
                else:
                    current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = BstNode(value)
                    return current_node.right
                else:
                    current_node = current_node.right
            else:
                return current_node

    def remove(self, value: int) -> None:
        self.__check_type(value)
        node_to_del = self.get(value)
        if not node_to_del:
            return
        if not node_to_del.left and not node_to_del.right:  # no children
            parent_node = self.get_parent(value)
            if parent_node.left == node_to_del:
                parent_node.left = None
            else:
                parent_node.right = None
        elif (not node_to_del.left and node_to_del.right) or (node_to_del.left and not node_to_del.right):  # XOR: one child
            parent_node = self.get_parent(value)
            if node_to_del.left:
                if parent_node.left == node_to_del:
                    parent_node.left = node_to_del.left
                else:
                    parent_node.right = node_to_del.left
            else:  # node_to_del.right
                if parent_node.left == node_to_del:
                    parent_node.left = node_to_del.right
                else:
                    parent_node.right = node_to_del.right
        else:  # 2 children
            max_val = self.get_max_node(node_to_del.left).value
            self.remove(max_val)
            node_to_del.value = max_val

    def get(self, value, default=None) -> Optional[BstNode]:
        self.__check_type(value)
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return current_node
        return default

    def get_parent(self, value, default=None) -> Optional[BstNode]:
        self.__check_type(value)
        current_node = self.root
        parent = None
        while current_node:
            if value < current_node.value:
                parent = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent = current_node
                current_node = current_node.right
            else:
                return parent
        return default

    def dft(self, type: str = 'inorder') -> Generator:
        traversal_types = {
            'inorder': self._inorder,
            'preorder': self._preorder,
            'postorder': self._postorder,
        }
        traversal = traversal_types.get(type)
        if traversal is None:
            raise ValueError(f'type of traversal must be either {tuple(traversal_types.keys())}, not {type}')
        return traversal(self.root)

    def bft(self) -> Generator:
        '''В ширину (BFS)'''
        this_line = [self.root]
        next_line = []
        while this_line:
            node = this_line.pop(0)
            if node:
                next_line.append(node.left)
                next_line.append(node.right)
                yield node.value
            if len(this_line) > 0:
                continue
            else:
                this_line = next_line
                next_line = []

    def _init(self, value) -> BstNode:
        self.root = BstNode(value)
        return self.root

    def _inorder(self, node) -> Generator:
        '''Центрированый (LNR)'''
        if node:
            yield from self._inorder(node.left)
            yield node.value
            yield from self._inorder(node.right)

    def _preorder(self, node) -> Generator:
        '''Прямой (NLR)'''
        if node:
            yield node.value
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def _postorder(self, node) -> Generator:
        '''Обратный (LRN)'''
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.value

    @property
    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node) -> int:
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

    def get_str(self, node: BstNode = _MISSING, indent=0, arrow='--->') -> Generator:
        if node is _MISSING:
            node = self.root
        if not node:
            return
        next_indent = indent + 4 + len(str(node.value))
        yield from self.get_str(node.right, next_indent, '.-->')
        yield f'{indent * " "}{arrow}{node.value}'
        yield from self.get_str(node.left, next_indent, '`-->')

    def __str__(self) -> str:
        return '\n'.join(self.get_str(self.root))

    @staticmethod
    def __check_type(value: Any, t: Type = int) -> None:
        if not isinstance(value, t):
            raise TypeError('BST accepts only an int values')

    @staticmethod
    def get_max_node(node) -> Optional[BstNode]:
        if not node:
            return None
        while node.right:
            node = node.right
        return node
