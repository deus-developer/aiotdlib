# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    MessageSender,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetVideoChatDefaultParticipant(BaseObject):
    """
    Changes default participant identifier, on whose behalf a video chat in the chat will be joined

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param default_participant_id: Default group call participant identifier to join the video chats
    :type default_participant_id: :class:`MessageSender`
    """

    ID: typing.Literal["setVideoChatDefaultParticipant"] = field(
        default="setVideoChatDefaultParticipant", metadata={"alias": "@type"}
    )
    chat_id: Int53
    default_participant_id: MessageSender
