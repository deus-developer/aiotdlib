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
class BlockMessageSenderFromReplies(BaseObject):
    """
    Blocks an original sender of a message in the Replies chat

    :param message_id: The identifier of an incoming message in the Replies chat
    :type message_id: :class:`Int53`
    :param delete_message: Pass true to delete the message
    :type delete_message: :class:`Bool`
    :param delete_all_messages: Pass true to delete all messages from the same sender
    :type delete_all_messages: :class:`Bool`
    :param report_spam: Pass true to report the sender to the Telegram moderators
    :type report_spam: :class:`Bool`
    """

    ID: typing.Literal["blockMessageSenderFromReplies"] = field(
        default="blockMessageSenderFromReplies", metadata={"alias": "@type"}
    )
    message_id: Int53
    delete_message: Bool = field(default=False)
    delete_all_messages: Bool = field(default=False)
    report_spam: Bool = field(default=False)
