from typing import Optional
import ormar

from buysell_advertisement.ads.models.ads import ADVT
from settings.db import (
    database,
    metadata
    )


class PhotoADVT(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    photo: str = ormar.String(max_length=255)
    photo_thumb: str = ormar.String(max_length=255)
    adv: Optional[ADVT] = ormar.ForeignKey(ADVT, related_name="photo_galery")
