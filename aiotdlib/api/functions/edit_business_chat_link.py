# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputBusinessChatLink,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class EditBusinessChatLink(BaseObject):
    """
    Edits a business chat link of the current account. Requires Telegram Business subscription. Returns the edited link

    :param link: The link to edit
    :type link: :class:`String`
    :param link_info: New description of the link
    :type link_info: :class:`InputBusinessChatLink`
    """

    ID: typing.Literal["editBusinessChatLink"] = field(default="editBusinessChatLink", metadata={"alias": "@type"})
    link: String
    link_info: InputBusinessChatLink
