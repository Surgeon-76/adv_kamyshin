from typing import Optional
import ormar

from .advertisement import ADSAppart
from settings.db import (
    database,
    metadata
    )


class PhotoAPRT(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    photo: str = ormar.String(max_length=255)
    photo_thumb: str = ormar.String(max_length=255)
    advaprt: Optional[ADSAppart] = ormar.ForeignKey(
       ADSAppart
    )
