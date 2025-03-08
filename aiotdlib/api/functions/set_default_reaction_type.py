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
class SetDefaultReactionType(BaseObject):
    """
    Changes type of default reaction for the current user

    :param reaction_type: New type of the default reaction. The paid reaction can't be set as default
    :type reaction_type: :class:`ReactionType`
    """

    ID: typing.Literal["setDefaultReactionType"] = field(default="setDefaultReactionType", metadata={"alias": "@type"})
    reaction_type: ReactionType
