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
class GetChatBoostFeatures(BaseObject):
    """
    Returns the list of features available for different chat boost levels; this is an offline request

    :param is_channel: Pass true to get the list of features for channels; pass false to get the list of features for supergroups
    :type is_channel: :class:`Bool`
    """

    ID: typing.Literal["getChatBoostFeatures"] = field(default="getChatBoostFeatures", metadata={"alias": "@type"})
    is_channel: Bool = field(default=False)
