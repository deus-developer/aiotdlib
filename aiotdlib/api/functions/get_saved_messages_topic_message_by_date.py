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
class GetSavedMessagesTopicMessageByDate(BaseObject):
    """
    Returns the last message sent in a Saved Messages topic no later than the specified date

    :param saved_messages_topic_id: Identifier of Saved Messages topic which message will be returned
    :type saved_messages_topic_id: :class:`Int53`
    :param date: Point in time (Unix timestamp) relative to which to search for messages
    :type date: :class:`Int32`
    """

    ID: typing.Literal["getSavedMessagesTopicMessageByDate"] = field(
        default="getSavedMessagesTopicMessageByDate", metadata={"alias": "@type"}
    )
    saved_messages_topic_id: Int53
    date: Int32
