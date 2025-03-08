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
class GetInternalLinkType(BaseObject):
    """
    Returns information about the type of internal link. Returns a 404 error if the link is not internal. Can be called before authorization

    :param link: The link
    :type link: :class:`String`
    """

    ID: typing.Literal["getInternalLinkType"] = field(default="getInternalLinkType", metadata={"alias": "@type"})
    link: String
