from typing import Literal

from .node import Node


class Square(Node):
    node_type: Literal["square"] = "square"
    side: float
