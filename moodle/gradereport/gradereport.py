from moodle import BaseMoodle
from moodle.utils.decorator import lazy
from . import BaseUser


class Gradereport(BaseMoodle):
    @property  # type: ignore
    @lazy
    def user(self) -> BaseUser:
        return BaseUser(self.moodle)
