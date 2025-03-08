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
class RemoveBusinessConnectedBotFromChat(BaseObject):
    """
    Removes the connected business bot from a specific chat by adding the chat to businessRecipients.excluded_chat_ids

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["removeBusinessConnectedBotFromChat"] = field(
        default="removeBusinessConnectedBotFromChat", metadata={"alias": "@type"}
    )
    chat_id: Int53
