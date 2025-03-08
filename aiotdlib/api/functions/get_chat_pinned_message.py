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
class GetChatPinnedMessage(BaseObject):
    """
    Returns information about a newest pinned message in the chat. Returns a 404 error if the message doesn't exist

    :param chat_id: Identifier of the chat the message belongs to
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatPinnedMessage"] = field(default="getChatPinnedMessage", metadata={"alias": "@type"})
    chat_id: Int53
