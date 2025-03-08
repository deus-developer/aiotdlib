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
class GetBasicGroup(BaseObject):
    """
    Returns information about a basic group by its identifier. This is an offline request if the current user is not a bot

    :param basic_group_id: Basic group identifier
    :type basic_group_id: :class:`Int53`
    """

    ID: typing.Literal["getBasicGroup"] = field(default="getBasicGroup", metadata={"alias": "@type"})
    basic_group_id: Int53
