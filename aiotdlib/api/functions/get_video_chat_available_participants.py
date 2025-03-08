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
class GetVideoChatAvailableParticipants(BaseObject):
    """
    Returns the list of participant identifiers, on whose behalf a video chat in the chat can be joined

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getVideoChatAvailableParticipants"] = field(
        default="getVideoChatAvailableParticipants", metadata={"alias": "@type"}
    )
    chat_id: Int53
