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
class GetStickerSetName(BaseObject):
    """
    Returns name of a sticker set by its identifier

    :param set_id: Identifier of the sticker set
    :type set_id: :class:`Int64`
    """

    ID: typing.Literal["getStickerSetName"] = field(default="getStickerSetName", metadata={"alias": "@type"})
    set_id: Int64
