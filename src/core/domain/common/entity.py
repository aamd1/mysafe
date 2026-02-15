from typing import Generic, TypeVar

T= TypeVar('T')

class Entity(Generic[T]):
    __id: T

    @property
    def id(self) -> T:
        return self.__id

    def __init__(self, entity_id: T):
        self.__id = entity_id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return False
        return self.id == other.id