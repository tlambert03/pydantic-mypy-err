from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .circle import Circle

    # note, if square were defined after Node in THIS file, mypy is happy.
    from .square import Square


class _MyBase(BaseModel):
    """Base class for all evented pydantic-style models."""

    # Note: without this additional base with extra="forbid" mypy is happy.
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")


AnyNode = Annotated["Circle | Square", Field(discriminator="node_type")]


class Node(_MyBase):
    name: str | None = Field(default=None, description="Name of the node.")
    parent: AnyNode | None = None
