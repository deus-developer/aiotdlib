# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputMessageContent,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class AddQuickReplyShortcutMessage(BaseObject):
    """
    Adds a message to a quick reply shortcut. If shortcut doesn't exist and there are less than getOption("quick_reply_shortcut_count_max") shortcuts, then a new shortcut is created. The shortcut must not contain more than getOption("quick_reply_shortcut_message_count_max") messages after adding the new message. Returns the added message

    :param shortcut_name: Name of the target shortcut
    :type shortcut_name: :class:`String`
    :param input_message_content: The content of the message to be added; inputMessagePoll, inputMessageForwarded and inputMessageLocation with live_period aren't supported
    :type input_message_content: :class:`InputMessageContent`
    :param reply_to_message_id: Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none
    :type reply_to_message_id: :class:`Int53`
    """

    ID: typing.Literal["addQuickReplyShortcutMessage"] = field(
        default="addQuickReplyShortcutMessage", metadata={"alias": "@type"}
    )
    shortcut_name: String
    input_message_content: InputMessageContent
    reply_to_message_id: Int53 = field(default=0)
