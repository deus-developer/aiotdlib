# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ReactionType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetStoryReaction(BaseObject):
    """
    Changes chosen reaction on a story that has already been sent

    :param story_sender_chat_id: The identifier of the sender of the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: The identifier of the story
    :type story_id: :class:`Int32`
    :param update_recent_reactions: Pass true if the reaction needs to be added to recent reactions
    :type update_recent_reactions: :class:`Bool`
    :param reaction_type: Type of the reaction to set; pass null to remove the reaction. Custom emoji reactions can be used only by Telegram Premium users. Paid reactions can't be set, defaults to None
    :type reaction_type: :class:`ReactionType`, optional
    """

    ID: typing.Literal["setStoryReaction"] = field(default="setStoryReaction", metadata={"alias": "@type"})
    story_sender_chat_id: Int53
    story_id: Int32
    update_recent_reactions: Bool = field(default=False)
    reaction_type: typing.Optional[ReactionType] = field(default=None)
