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
class SendCustomRequest(BaseObject):
    """
    Sends a custom request; for bots only

    :param method: The method name
    :type method: :class:`String`
    :param parameters: JSON-serialized method parameters
    :type parameters: :class:`String`
    """

    ID: typing.Literal["sendCustomRequest"] = field(default="sendCustomRequest", metadata={"alias": "@type"})
    method: String
    parameters: String
