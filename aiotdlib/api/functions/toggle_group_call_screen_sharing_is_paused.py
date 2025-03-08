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
class ToggleGroupCallScreenSharingIsPaused(BaseObject):
    """
    Pauses or unpauses screen sharing in a joined group call

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param is_paused: Pass true to pause screen sharing; pass false to unpause it
    :type is_paused: :class:`Bool`
    """

    ID: typing.Literal["toggleGroupCallScreenSharingIsPaused"] = field(
        default="toggleGroupCallScreenSharingIsPaused", metadata={"alias": "@type"}
    )
    group_call_id: Int32
    is_paused: Bool = field(default=False)
