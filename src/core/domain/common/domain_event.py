from datetime import datetime


class DomainEvent:
    __occurred_on: datetime

    @property
    def occurred_on(self) -> datetime:
        return self.__occurred_on
    def __init__(self):
        self.__occurred_on = datetime.now()
