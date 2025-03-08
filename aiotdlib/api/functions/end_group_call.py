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
class EndGroupCall(BaseObject):
    """
    Ends a group call. Requires groupCall.can_be_managed

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["endGroupCall"] = field(default="endGroupCall", metadata={"alias": "@type"})
    group_call_id: Int32
