from typing import TypeVar

from src.core.domain.common.domain_event import DomainEvent
from src.core.domain.common.entity import Entity

T = TypeVar('T')
class AggregateRoot(Entity[T]):
    __domain_events: list[DomainEvent] = []

    def __init__(self, entity_id: T):
        super().__init__(entity_id)
    @property
    def domain_events(self) -> list[DomainEvent]:
        return self.__domain_events


    def raise_domain_event(self, domain_event: DomainEvent):
        self.__domain_events.append(domain_event)

    def clear_domain_events(self):
        self.__domain_events.clear()