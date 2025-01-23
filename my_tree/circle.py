from typing import Literal

from .node import Node


class Circle(Node):
    node_type: Literal["circle"] = "circle"
    radius: float
