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
class GetBasicGroupFullInfo(BaseObject):
    """
    Returns full information about a basic group by its identifier

    :param basic_group_id: Basic group identifier
    :type basic_group_id: :class:`Int53`
    """

    ID: typing.Literal["getBasicGroupFullInfo"] = field(default="getBasicGroupFullInfo", metadata={"alias": "@type"})
    basic_group_id: Int53
