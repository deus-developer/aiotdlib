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
class GetStoryAvailableReactions(BaseObject):
    """
    Returns reactions, which can be chosen for a story

    :param row_size: Number of reaction per row, 5-25
    :type row_size: :class:`Int32`
    """

    ID: typing.Literal["getStoryAvailableReactions"] = field(
        default="getStoryAvailableReactions", metadata={"alias": "@type"}
    )
    row_size: Int32
