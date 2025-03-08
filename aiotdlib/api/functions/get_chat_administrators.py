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
class GetChatAdministrators(BaseObject):
    """
    Returns a list of administrators of the chat with their custom titles

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatAdministrators"] = field(default="getChatAdministrators", metadata={"alias": "@type"})
    chat_id: Int53
