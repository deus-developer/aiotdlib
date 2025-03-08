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
class GetDeepLinkInfo(BaseObject):
    """
    Returns information about a tg:// deep link. Use "tg://need_update_for_some_feature" or "tg:some_unsupported_feature" for testing. Returns a 404 error for unknown links. Can be called before authorization

    :param link: The link
    :type link: :class:`String`
    """

    ID: typing.Literal["getDeepLinkInfo"] = field(default="getDeepLinkInfo", metadata={"alias": "@type"})
    link: String
