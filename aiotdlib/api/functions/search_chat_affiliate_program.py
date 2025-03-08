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
class SearchChatAffiliateProgram(BaseObject):
    """
    Searches a chat with an affiliate program. Returns the chat if found and the program is active

    :param username: Username of the chat
    :type username: :class:`String`
    :param referrer: The referrer from an internalLinkTypeChatAffiliateProgram link
    :type referrer: :class:`String`
    """

    ID: typing.Literal["searchChatAffiliateProgram"] = field(
        default="searchChatAffiliateProgram", metadata={"alias": "@type"}
    )
    username: String
    referrer: String
