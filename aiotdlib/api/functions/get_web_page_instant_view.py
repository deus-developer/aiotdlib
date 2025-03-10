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
class GetWebPageInstantView(BaseObject):
    """
    Returns an instant view version of a web page if available. Returns a 404 error if the web page has no instant view page

    :param url: The web page URL
    :type url: :class:`String`
    :param force_full: Pass true to get full instant view for the web page
    :type force_full: :class:`Bool`
    """

    ID: typing.Literal["getWebPageInstantView"] = field(default="getWebPageInstantView", metadata={"alias": "@type"})
    url: String
    force_full: Bool = field(default=False)
