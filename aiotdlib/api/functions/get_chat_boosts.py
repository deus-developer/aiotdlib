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
class GetChatBoosts(BaseObject):
    """
    Returns the list of boosts applied to a chat; requires administrator rights in the chat

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of boosts to be returned; up to 100. For optimal performance, the number of returned boosts can be smaller than the specified limit
    :type limit: :class:`Int32`
    :param only_gift_codes: Pass true to receive only boosts received from gift codes and giveaways created by the chat
    :type only_gift_codes: :class:`Bool`
    """

    ID: typing.Literal["getChatBoosts"] = field(default="getChatBoosts", metadata={"alias": "@type"})
    chat_id: Int53
    offset: String
    limit: Int32
    only_gift_codes: Bool = field(default=False)
