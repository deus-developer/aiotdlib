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
class GetInstalledBackgrounds(BaseObject):
    """
    Returns backgrounds installed by the user

    :param for_dark_theme: Pass true to order returned backgrounds for a dark theme
    :type for_dark_theme: :class:`Bool`
    """

    ID: typing.Literal["getInstalledBackgrounds"] = field(
        default="getInstalledBackgrounds", metadata={"alias": "@type"}
    )
    for_dark_theme: Bool = field(default=False)
