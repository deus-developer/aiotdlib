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
class SearchBackground(BaseObject):
    """
    Searches for a background by its name

    :param name: The name of the background
    :type name: :class:`String`
    """

    ID: typing.Literal["searchBackground"] = field(default="searchBackground", metadata={"alias": "@type"})
    name: String
