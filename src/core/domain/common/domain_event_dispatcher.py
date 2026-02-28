from src.core.domain.common.domain_event import DomainEvent
from src.core.domain.common.domain_event_handler import DomainEventHandler


class DomainEventDispatcher:
    __handlers: dict[type[DomainEvent], list[DomainEventHandler[DomainEvent]]]=[]
    def dispatch(self, domain_events: list[DomainEvent]):
        for event in domain_events:
            self._dispatch_event(event)

    def _dispatch_event(self, domain_event: DomainEvent) -> None:
        raise NotImplementedError("Subclasses must implement dispatch_event method")

    def register(self, handler: DomainEventHandler[DomainEvent]):
        self.__handlers[]

