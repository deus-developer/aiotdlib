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
class SetSavedMessagesTagLabel(BaseObject):
    """
    Changes label of a Saved Messages tag; for Telegram Premium users only

    :param tag: The tag which label will be changed
    :type tag: :class:`ReactionType`
    :param label: New label for the tag; 0-12 characters
    :type label: :class:`String`
    """

    ID: typing.Literal["setSavedMessagesTagLabel"] = field(
        default="setSavedMessagesTagLabel", metadata={"alias": "@type"}
    )
    tag: ReactionType
    label: String = field(default="", metadata={"max_length": 12})
