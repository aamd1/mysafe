from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.core.domain.common.domain_event import DomainEvent

TDomainEvent = TypeVar('TDomainEvent', bound=DomainEvent)

class DomainEventHandler(ABC, Generic[TDomainEvent]):
    @abstractmethod
    def handle(self, domain_event: TDomainEvent) -> None:
        raise NotImplementedError("Subclasses must implement handle method")