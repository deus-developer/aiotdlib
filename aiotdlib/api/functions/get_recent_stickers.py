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
class GetRecentStickers(BaseObject):
    """
    Returns a list of recently used stickers

    :param is_attached: Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers
    :type is_attached: :class:`Bool`
    """

    ID: typing.Literal["getRecentStickers"] = field(default="getRecentStickers", metadata={"alias": "@type"})
    is_attached: Bool = field(default=False)
