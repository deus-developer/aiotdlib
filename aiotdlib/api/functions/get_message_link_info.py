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
class GetMessageLinkInfo(BaseObject):
    """
    Returns information about a public or private message link. Can be called for any internal link of the type internalLinkTypeMessage

    :param url: The message link
    :type url: :class:`String`
    """

    ID: typing.Literal["getMessageLinkInfo"] = field(default="getMessageLinkInfo", metadata={"alias": "@type"})
    url: String
