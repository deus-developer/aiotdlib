# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputBusinessStartPage,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetBusinessStartPage(BaseObject):
    """
    Changes the business start page of the current user. Requires Telegram Business subscription

    :param start_page: The new start page of the business; pass null to remove custom start page, defaults to None
    :type start_page: :class:`InputBusinessStartPage`, optional
    """

    ID: typing.Literal["setBusinessStartPage"] = field(default="setBusinessStartPage", metadata={"alias": "@type"})
    start_page: typing.Optional[InputBusinessStartPage] = field(default=None)
