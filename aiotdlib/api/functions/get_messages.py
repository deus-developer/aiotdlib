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
class GetMessages(BaseObject):
    """
    Returns information about messages. If a message is not found, returns null on the corresponding position of the result

    :param chat_id: Identifier of the chat the messages belong to
    :type chat_id: :class:`Int53`
    :param message_ids: Identifiers of the messages to get
    :type message_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["getMessages"] = field(default="getMessages", metadata={"alias": "@type"})
    chat_id: Int53
    message_ids: Vector[Int53]
