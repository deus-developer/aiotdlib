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
class ChangeStickerSet(BaseObject):
    """
    Installs/uninstalls or activates/archives a sticker set

    :param set_id: Identifier of the sticker set
    :type set_id: :class:`Int64`
    :param is_installed: The new value of is_installed
    :type is_installed: :class:`Bool`
    :param is_archived: The new value of is_archived. A sticker set can't be installed and archived simultaneously
    :type is_archived: :class:`Bool`
    """

    ID: typing.Literal["changeStickerSet"] = field(default="changeStickerSet", metadata={"alias": "@type"})
    set_id: Int64
    is_installed: Bool
    is_archived: Bool
