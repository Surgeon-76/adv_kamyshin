from enum import Enum
from typing import Optional

import ormar

from settings.db import (
    database,
    metadata
    )


class TransactionVar(Enum):
    tv_1 = 'продать'
    tv_2 = 'сдать'


class TypeOfHousing(Enum):
    th_1 = 'коммерческая'
    th_2 = 'жилая'


"""
    transaction: Optional[str]  Тип сделки(TransactionVar)
    type_housing: Optional[str] Тип жилья(TypeOfHousing)
    daily: bool                 Посуточно или нет
"""


class Categorie(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    transaction: Optional[str] = ormar.String(max_length=8,
                                              choices=list(TransactionVar))
    type_housing: Optional[str] = ormar.String(max_length=20,
                                               choices=list(TypeOfHousing))
    daily: bool = ormar.Boolean(default=False)
