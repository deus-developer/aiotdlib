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
class CommitPendingPaidMessageReactions(BaseObject):
    """
    Applies all pending paid reactions on a message

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["commitPendingPaidMessageReactions"] = field(
        default="commitPendingPaidMessageReactions", metadata={"alias": "@type"}
    )
    chat_id: Int53
    message_id: Int53
