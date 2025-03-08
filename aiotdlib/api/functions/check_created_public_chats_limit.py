# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.all import (
    PublicChatType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class CheckCreatedPublicChatsLimit(BaseObject):
    """
    Checks whether the maximum number of owned public chats has been reached. Returns corresponding error if the limit was reached. The limit can be increased with Telegram Premium

    :param type_: Type of the public chats, for which to check the limit
    :type type_: :class:`PublicChatType`
    """

    ID: typing.Literal["checkCreatedPublicChatsLimit"] = field(
        default="checkCreatedPublicChatsLimit", metadata={"alias": "@type"}
    )
    type_: PublicChatType = field(default=MISSING, metadata={"alias": "type"})
