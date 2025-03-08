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
class GetChatBoostLinkInfo(BaseObject):
    """
    Returns information about a link to boost a chat. Can be called for any internal link of the type internalLinkTypeChatBoost

    :param url: The link to boost a chat
    :type url: :class:`String`
    """

    ID: typing.Literal["getChatBoostLinkInfo"] = field(default="getChatBoostLinkInfo", metadata={"alias": "@type"})
    url: String
