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
class GetChatSponsoredMessages(BaseObject):
    """
    Returns sponsored messages to be shown in a chat; for channel chats and chats with bots only

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatSponsoredMessages"] = field(
        default="getChatSponsoredMessages", metadata={"alias": "@type"}
    )
    chat_id: Int53
