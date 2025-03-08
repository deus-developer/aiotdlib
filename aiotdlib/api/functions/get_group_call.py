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
class GetGroupCall(BaseObject):
    """
    Returns information about a group call

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["getGroupCall"] = field(default="getGroupCall", metadata={"alias": "@type"})
    group_call_id: Int32
