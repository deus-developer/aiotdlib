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
class SetPinnedSavedMessagesTopics(BaseObject):
    """
    Changes the order of pinned Saved Messages topics

    :param saved_messages_topic_ids: Identifiers of the new pinned Saved Messages topics
    :type saved_messages_topic_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["setPinnedSavedMessagesTopics"] = field(
        default="setPinnedSavedMessagesTopics", metadata={"alias": "@type"}
    )
    saved_messages_topic_ids: Vector[Int53]
