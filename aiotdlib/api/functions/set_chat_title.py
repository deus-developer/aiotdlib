# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetChatTitle(BaseObject):
    """
    Changes the chat title. Supported only for basic groups, supergroups and channels. Requires can_change_info member right

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param title: New title of the chat; 1-128 characters
    :type title: :class:`String`
    """

    ID: typing.Literal["setChatTitle"] = field(default="setChatTitle", metadata={"alias": "@type"})
    chat_id: Int53
    title: String = field(default=MISSING, metadata={"min_length": 1, "max_length": 128})
