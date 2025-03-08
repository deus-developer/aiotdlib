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
class GetPremiumStickers(BaseObject):
    """
    Returns premium stickers from regular sticker sets

    :param limit: The maximum number of stickers to be returned; 0-100
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getPremiumStickers"] = field(default="getPremiumStickers", metadata={"alias": "@type"})
    limit: Int32
