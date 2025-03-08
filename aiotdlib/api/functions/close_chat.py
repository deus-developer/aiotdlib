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
class CloseChat(BaseObject):
    """
    Informs TDLib that the chat is closed by the user. Many useful activities depend on the chat being opened or closed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["closeChat"] = field(default="closeChat", metadata={"alias": "@type"})
    chat_id: Int53
