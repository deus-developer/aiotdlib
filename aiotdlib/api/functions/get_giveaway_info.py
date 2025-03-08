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
class GetGiveawayInfo(BaseObject):
    """
    Returns information about a giveaway

    :param chat_id: Identifier of the channel chat which started the giveaway
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the giveaway or a giveaway winners message in the chat
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["getGiveawayInfo"] = field(default="getGiveawayInfo", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
