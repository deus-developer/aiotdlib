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
class RemoveChatActionBar(BaseObject):
    """
    Removes a chat action bar without any other action

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["removeChatActionBar"] = field(default="removeChatActionBar", metadata={"alias": "@type"})
    chat_id: Int53
