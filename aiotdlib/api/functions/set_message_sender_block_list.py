# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BlockList,
    MessageSender,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetMessageSenderBlockList(BaseObject):
    """
    Changes the block list of a message sender. Currently, only users and supergroup chats can be blocked

    :param sender_id: Identifier of a message sender to block/unblock
    :type sender_id: :class:`MessageSender`
    :param block_list: New block list for the message sender; pass null to unblock the message sender, defaults to None
    :type block_list: :class:`BlockList`, optional
    """

    ID: typing.Literal["setMessageSenderBlockList"] = field(
        default="setMessageSenderBlockList", metadata={"alias": "@type"}
    )
    sender_id: MessageSender
    block_list: typing.Optional[BlockList] = field(default=None)
