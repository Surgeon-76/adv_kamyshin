from decimal import Decimal
from enum import Enum
from typing import Optional

import ormar

from ..models.ads import ADVT
from settings.db import (
    database,
    metadata
    )


class CountServices(Enum):
    cs_1 = 'за услугу'
    cs_2 = 'за м*2'
    cs_3 = 'за м. погонный'
    cs_4 = 'за м*3'
    cs_5 = 'за 1 шт.'
    cs_6 = 'за 1 метр'
    cs_7 = 'за 1 км.'
    cs_8 = 'за 45 мин.'
    cs_9 = 'за 1 час'
    cs_10 = 'за 1 сутки'
    cs_11 = 'за 1 неделю'
    cs_12 = 'за 1 месяц'


class Service(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    name: str = ormar.String(max_length=200)
    slug: str = ormar.String(max_length=255, nullable=True, index=True)
    price: Decimal = ormar.Decimal(
        precision=10,
        scale=2,
        default=0
    )
    unit_of_dim: str = ormar.String(max_length=100,
                                    choices=list(CountServices))
    advt: Optional[ADVT] = ormar.ForeignKey(ADVT, related_name="service")
