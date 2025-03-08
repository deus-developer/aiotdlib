# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class ViewTrendingStickerSets(BaseObject):
    """
    Informs the server that some trending sticker sets have been viewed by the user

    :param sticker_set_ids: Identifiers of viewed trending sticker sets
    :type sticker_set_ids: :class:`Vector[Int64]`
    """

    ID: typing.Literal["viewTrendingStickerSets"] = field(
        default="viewTrendingStickerSets", metadata={"alias": "@type"}
    )
    sticker_set_ids: Vector[Int64]
