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
class ReplaceVideoChatRtmpUrl(BaseObject):
    """
    Replaces the current RTMP URL for streaming to the chat; requires owner privileges

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["replaceVideoChatRtmpUrl"] = field(
        default="replaceVideoChatRtmpUrl", metadata={"alias": "@type"}
    )
    chat_id: Int53
