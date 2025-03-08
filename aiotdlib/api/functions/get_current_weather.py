# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    Location,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetCurrentWeather(BaseObject):
    """
    Returns the current weather in the given location

    :param location: The location
    :type location: :class:`Location`
    """

    ID: typing.Literal["getCurrentWeather"] = field(default="getCurrentWeather", metadata={"alias": "@type"})
    location: Location
