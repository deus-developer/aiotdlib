# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetJsonValue(BaseObject):
    """
    Converts a JSON-serialized string to corresponding JsonValue object. Can be called synchronously

    :param json_: The JSON-serialized string
    :type json_: :class:`String`
    """

    ID: typing.Literal["getJsonValue"] = field(default="getJsonValue", metadata={"alias": "@type"})
    json_: String = field(default=MISSING, metadata={"alias": "json"})
