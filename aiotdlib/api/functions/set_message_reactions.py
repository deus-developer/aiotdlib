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
class SetMessageReactions(BaseObject):
    """
    Sets reactions on a message; for bots only

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param reaction_types: Types of the reaction to set; pass an empty list to remove the reactions
    :type reaction_types: :class:`Vector[ReactionType]`
    :param is_big: Pass true if the reactions are added with a big animation
    :type is_big: :class:`Bool`
    """

    ID: typing.Literal["setMessageReactions"] = field(default="setMessageReactions", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
    reaction_types: Vector[ReactionType]
    is_big: Bool = field(default=False)
