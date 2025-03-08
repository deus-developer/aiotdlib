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
class GetGiftUpgradePreview(BaseObject):
    """
    Returns examples of possible upgraded gifts for a regular gift

    :param gift_id: Identifier of the gift
    :type gift_id: :class:`Int64`
    """

    ID: typing.Literal["getGiftUpgradePreview"] = field(default="getGiftUpgradePreview", metadata={"alias": "@type"})
    gift_id: Int64
