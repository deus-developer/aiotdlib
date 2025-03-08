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
class GetPushReceiverId(BaseObject):
    """
    Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification. Can be called synchronously

    :param payload: JSON-encoded push notification payload
    :type payload: :class:`String`
    """

    ID: typing.Literal["getPushReceiverId"] = field(default="getPushReceiverId", metadata={"alias": "@type"})
    payload: String
