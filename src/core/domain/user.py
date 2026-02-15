from datetime import datetime

from src.core.domain.common.aggregate_root import AggregateRoot


class User(AggregateRoot[str]):
    __first_name: str
    __last_name: str
    __is_active: bool
    __last_logged_in_at: datetime | None
    __created_at: datetime
    __updated_at: datetime | None
    __password: str | None
    __email: str
    __email_verified: bool

    def __init__(self,user_id: str, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__is_active = False
        self.__last_logged_in_at = None
        self.__created_at = datetime.now()
        super().__init__(user_id)

    def activate(self, email: str):
        if self.__email_verified:
            self.__is_active = True

        else:
            raise Exception("Email not verified")

