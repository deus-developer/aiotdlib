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
class SendCallDebugInformation(BaseObject):
    """
    Sends debug information for a call to Telegram servers

    :param call_id: Call identifier
    :type call_id: :class:`Int32`
    :param debug_information: Debug information in application-specific format
    :type debug_information: :class:`String`
    """

    ID: typing.Literal["sendCallDebugInformation"] = field(
        default="sendCallDebugInformation", metadata={"alias": "@type"}
    )
    call_id: Int32
    debug_information: String
