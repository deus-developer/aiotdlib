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
class EndGroupCallScreenSharing(BaseObject):
    """
    Ends screen sharing in a joined group call

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["endGroupCallScreenSharing"] = field(
        default="endGroupCallScreenSharing", metadata={"alias": "@type"}
    )
    group_call_id: Int32
