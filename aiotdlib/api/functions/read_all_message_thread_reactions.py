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
class ReadAllMessageThreadReactions(BaseObject):
    """
    Marks all reactions in a forum topic as read

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier in which reactions are marked as read
    :type message_thread_id: :class:`Int53`
    """

    ID: typing.Literal["readAllMessageThreadReactions"] = field(
        default="readAllMessageThreadReactions", metadata={"alias": "@type"}
    )
    chat_id: Int53
    message_thread_id: Int53
