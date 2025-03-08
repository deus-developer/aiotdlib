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
class ProcessChatJoinRequest(BaseObject):
    """
    Handles a pending join request in a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param user_id: Identifier of the user that sent the request
    :type user_id: :class:`Int53`
    :param approve: Pass true to approve the request; pass false to decline it
    :type approve: :class:`Bool`
    """

    ID: typing.Literal["processChatJoinRequest"] = field(default="processChatJoinRequest", metadata={"alias": "@type"})
    chat_id: Int53
    user_id: Int53
    approve: Bool = field(default=False)
