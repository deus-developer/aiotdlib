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
class GetMessageProperties(BaseObject):
    """
    Returns properties of a message; this is an offline request

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["getMessageProperties"] = field(default="getMessageProperties", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
