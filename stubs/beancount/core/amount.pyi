# pylint: disable=all
# flake8: noqa
import datetime
from typing import Any
from typing import Dict
from typing import NamedTuple
from typing import Optional

from beancount.core.number import Decimal

class _Amount(NamedTuple):
    number: Optional[Decimal]
    currency: str

CURRENCY_RE: str

class Amount(_Amount):
    valid_types_number: Any = ...
    valid_types_currency: Any = ...
    def __new__(cls, number: Optional[Decimal], currency: str): ...
    def to_string(self, dformat: Any = ...): ...
    def __bool__(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def __neg__(self): ...
    @staticmethod
    def from_string(string: str): ...

# def sortkey(amount: Any): ...
# def mul(amount: Any, number: Any): ...
# def div(amount: Any, number: Any): ...
# def add(amount1: Any, amount2: Any): ...
# def sub(amount1: Any, amount2: Any): ...
# def abs(amount: Any): ...
#
# A: Any
#
# from_string: Any
# NULL_AMOUNT: Any
