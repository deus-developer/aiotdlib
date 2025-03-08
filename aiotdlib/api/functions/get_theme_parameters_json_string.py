# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ThemeParameters,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetThemeParametersJsonString(BaseObject):
    """
    Converts a themeParameters object to corresponding JSON-serialized string. Can be called synchronously

    :param theme: Theme parameters to convert to JSON
    :type theme: :class:`ThemeParameters`
    """

    ID: typing.Literal["getThemeParametersJsonString"] = field(
        default="getThemeParametersJsonString", metadata={"alias": "@type"}
    )
    theme: ThemeParameters
