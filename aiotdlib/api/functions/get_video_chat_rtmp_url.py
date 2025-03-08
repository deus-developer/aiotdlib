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
class GetVideoChatRtmpUrl(BaseObject):
    """
    Returns RTMP URL for streaming to the chat; requires can_manage_video_chats administrator right

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getVideoChatRtmpUrl"] = field(default="getVideoChatRtmpUrl", metadata={"alias": "@type"})
    chat_id: Int53
