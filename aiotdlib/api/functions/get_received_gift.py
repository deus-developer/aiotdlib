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
class GetReceivedGift(BaseObject):
    """
    Returns information about a received gift

    :param received_gift_id: Identifier of the gift
    :type received_gift_id: :class:`String`
    """

    ID: typing.Literal["getReceivedGift"] = field(default="getReceivedGift", metadata={"alias": "@type"})
    received_gift_id: String
