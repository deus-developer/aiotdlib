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
class GetChat(BaseObject):
    """
    Returns information about a chat by its identifier; this is an offline request if the current user is not a bot

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChat"] = field(default="getChat", metadata={"alias": "@type"})
    chat_id: Int53
