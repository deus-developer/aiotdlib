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
class SetSupergroupStickerSet(BaseObject):
    """
    Changes the sticker set of a supergroup; requires can_change_info administrator right

    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`Int53`
    :param sticker_set_id: New value of the supergroup sticker set identifier. Use 0 to remove the supergroup sticker set
    :type sticker_set_id: :class:`Int64`
    """

    ID: typing.Literal["setSupergroupStickerSet"] = field(
        default="setSupergroupStickerSet", metadata={"alias": "@type"}
    )
    supergroup_id: Int53
    sticker_set_id: Int64
