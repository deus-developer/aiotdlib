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
class LeaveGroupCall(BaseObject):
    """
    Leaves a group call

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["leaveGroupCall"] = field(default="leaveGroupCall", metadata={"alias": "@type"})
    group_call_id: Int32
