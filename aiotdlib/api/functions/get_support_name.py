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
class GetSupportName(BaseObject):
    """
    Returns localized name of the Telegram support user; for Telegram support only
    """

    ID: typing.Literal["getSupportName"] = field(default="getSupportName", metadata={"alias": "@type"})
