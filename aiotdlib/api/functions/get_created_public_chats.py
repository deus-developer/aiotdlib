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
class GetCreatedPublicChats(BaseObject):
    """
    Returns a list of public chats of the specified type, owned by the user

    :param type_: Type of the public chats to return
    :type type_: :class:`PublicChatType`
    """

    ID: typing.Literal["getCreatedPublicChats"] = field(default="getCreatedPublicChats", metadata={"alias": "@type"})
    type_: PublicChatType = field(default=MISSING, metadata={"alias": "type"})
