from typing import Any, Optional


class BstNode:
    def __init__(self, data: Any, left: Optional['BstNode'] = None, right: Optional['BstNode'] = None):
        self.value = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'<BstNode {self.value}>'
