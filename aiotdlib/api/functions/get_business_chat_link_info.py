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
class GetBusinessChatLinkInfo(BaseObject):
    """
    Returns information about a business chat link

    :param link_name: Name of the link
    :type link_name: :class:`String`
    """

    ID: typing.Literal["getBusinessChatLinkInfo"] = field(
        default="getBusinessChatLinkInfo", metadata={"alias": "@type"}
    )
    link_name: String
