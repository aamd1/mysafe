import uuid
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


    @property
    def first_name(self) -> str:
        return self.__first_name
    @property
    def last_name(self) -> str:
        return self.__last_name
    @property
    def is_active(self) -> bool:
        return self.__is_active
    @property
    def last_logged_in_at(self) -> datetime | None:
        return self.__last_logged_in_at

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @property
    def updated_at(self) -> datetime | None:
        return self.__updated_at

    @property
    def password(self) -> str | None:
        return self.__password

    @property
    def email(self) -> str:
        return self.__email

    @property
    def email_verified(self) -> bool:
        return self.__email_verified

    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name
    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @is_active.setter
    def is_active(self, is_active: bool):
        self.__is_active = is_active

    @last_logged_in_at.setter
    def last_logged_in_at(self, last_logged_in_at: datetime):
        self.__last_logged_in_at = last_logged_in_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        self.__created_at = created_at
    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        self.__updated_at = updated_at

    @email.setter
    def email(self, email: str):
        self.__email = email

    @email_verified.setter
    def email_verified(self, email_verified: bool):
        self.__email_verified = email_verified

    @password.setter
    def password(self, password: str):
        self.__password = password

    def __init__(self,first_name: str, last_name: str, email: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__is_active = False
        self.__last_logged_in_at = None
        self.__created_at = datetime.now()
        self.__updated_at = None
        self.__password = None
        self.__email_verified = False
        self.is_active = False
        super().__init__(uuid.uuid4())

    def activate(self, email: str):
        if self.__email_verified:
            self.__is_active = True

        else:
            raise Exception("Email not verified")

    @staticmethod
    def create(first_name: str, last_name: str, email: str) -> 'User':
        user = User(first_name, last_name, email);
        return user

