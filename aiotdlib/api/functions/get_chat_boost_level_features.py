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
class GetChatBoostLevelFeatures(BaseObject):
    """
    Returns the list of features available on the specific chat boost level; this is an offline request

    :param level: Chat boost level
    :type level: :class:`Int32`
    :param is_channel: Pass true to get the list of features for channels; pass false to get the list of features for supergroups
    :type is_channel: :class:`Bool`
    """

    ID: typing.Literal["getChatBoostLevelFeatures"] = field(
        default="getChatBoostLevelFeatures", metadata={"alias": "@type"}
    )
    level: Int32
    is_channel: Bool = field(default=False)
