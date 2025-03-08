# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.all import (
    BackgroundType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetBackgroundUrl(BaseObject):
    """
    Constructs a persistent HTTP URL for a background

    :param name: Background name
    :type name: :class:`String`
    :param type_: Background type; backgroundTypeChatTheme isn't supported
    :type type_: :class:`BackgroundType`
    """

    ID: typing.Literal["getBackgroundUrl"] = field(default="getBackgroundUrl", metadata={"alias": "@type"})
    name: String
    type_: BackgroundType = field(default=MISSING, metadata={"alias": "type"})
