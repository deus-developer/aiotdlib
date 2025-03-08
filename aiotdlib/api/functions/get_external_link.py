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
class GetExternalLink(BaseObject):
    """
    Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed

    :param link: The HTTP link
    :type link: :class:`String`
    :param allow_write_access: Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages
    :type allow_write_access: :class:`Bool`
    """

    ID: typing.Literal["getExternalLink"] = field(default="getExternalLink", metadata={"alias": "@type"})
    link: String
    allow_write_access: Bool = field(default=False)
