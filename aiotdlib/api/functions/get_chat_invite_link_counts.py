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
class GetChatInviteLinkCounts(BaseObject):
    """
    Returns the list of chat administrators with number of their invite links. Requires owner privileges in the chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatInviteLinkCounts"] = field(
        default="getChatInviteLinkCounts", metadata={"alias": "@type"}
    )
    chat_id: Int53
