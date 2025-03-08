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
class SetChatTheme(BaseObject):
    """
    Changes the chat theme. Supported only in private and secret chats

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param theme_name: Name of the new chat theme; pass an empty string to return the default theme
    :type theme_name: :class:`String`
    """

    ID: typing.Literal["setChatTheme"] = field(default="setChatTheme", metadata={"alias": "@type"})
    chat_id: Int53
    theme_name: String
