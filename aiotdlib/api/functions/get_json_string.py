# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    JsonValue,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetJsonString(BaseObject):
    """
    Converts a JsonValue object to corresponding JSON-serialized string. Can be called synchronously

    :param json_value: The JsonValue object
    :type json_value: :class:`JsonValue`
    """

    ID: typing.Literal["getJsonString"] = field(default="getJsonString", metadata={"alias": "@type"})
    json_value: JsonValue
