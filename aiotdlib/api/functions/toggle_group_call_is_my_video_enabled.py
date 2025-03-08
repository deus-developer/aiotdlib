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
class ToggleGroupCallIsMyVideoEnabled(BaseObject):
    """
    Toggles whether current user's video is enabled

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param is_my_video_enabled: Pass true if the current user's video is enabled
    :type is_my_video_enabled: :class:`Bool`
    """

    ID: typing.Literal["toggleGroupCallIsMyVideoEnabled"] = field(
        default="toggleGroupCallIsMyVideoEnabled", metadata={"alias": "@type"}
    )
    group_call_id: Int32
    is_my_video_enabled: Bool = field(default=False)
