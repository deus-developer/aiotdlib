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
class GetApplicationDownloadLink(BaseObject):
    """
    Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram
    """

    ID: typing.Literal["getApplicationDownloadLink"] = field(
        default="getApplicationDownloadLink", metadata={"alias": "@type"}
    )
