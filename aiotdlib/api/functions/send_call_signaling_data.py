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
class SendCallSignalingData(BaseObject):
    """
    Sends call signaling data

    :param call_id: Call identifier
    :type call_id: :class:`Int32`
    :param data: The data
    :type data: :class:`Bytes`
    """

    ID: typing.Literal["sendCallSignalingData"] = field(default="sendCallSignalingData", metadata={"alias": "@type"})
    call_id: Int32
    data: Bytes
