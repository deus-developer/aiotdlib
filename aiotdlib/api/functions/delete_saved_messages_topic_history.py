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
class DeleteSavedMessagesTopicHistory(BaseObject):
    """
    Deletes all messages in a Saved Messages topic

    :param saved_messages_topic_id: Identifier of Saved Messages topic which messages will be deleted
    :type saved_messages_topic_id: :class:`Int53`
    """

    ID: typing.Literal["deleteSavedMessagesTopicHistory"] = field(
        default="deleteSavedMessagesTopicHistory", metadata={"alias": "@type"}
    )
    saved_messages_topic_id: Int53
