# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputChatPhoto,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetChatPhoto(BaseObject):
    """
    Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info member right

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param photo: New chat photo; pass null to delete the chat photo, defaults to None
    :type photo: :class:`InputChatPhoto`, optional
    """

    ID: typing.Literal["setChatPhoto"] = field(default="setChatPhoto", metadata={"alias": "@type"})
    chat_id: Int53
    photo: typing.Optional[InputChatPhoto] = field(default=None)
