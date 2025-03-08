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
class ReadAllChatMentions(BaseObject):
    """
    Marks all mentions in a chat as read

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["readAllChatMentions"] = field(default="readAllChatMentions", metadata={"alias": "@type"})
    chat_id: Int53
