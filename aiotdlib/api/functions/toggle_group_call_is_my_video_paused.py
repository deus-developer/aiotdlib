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
class ToggleGroupCallIsMyVideoPaused(BaseObject):
    """
    Toggles whether current user's video is paused

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param is_my_video_paused: Pass true if the current user's video is paused
    :type is_my_video_paused: :class:`Bool`
    """

    ID: typing.Literal["toggleGroupCallIsMyVideoPaused"] = field(
        default="toggleGroupCallIsMyVideoPaused", metadata={"alias": "@type"}
    )
    group_call_id: Int32
    is_my_video_paused: Bool = field(default=False)
