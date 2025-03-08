# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputFile,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SendCallLog(BaseObject):
    """
    Sends log file for a call to Telegram servers

    :param call_id: Call identifier
    :type call_id: :class:`Int32`
    :param log_file: Call log file. Only inputFileLocal and inputFileGenerated are supported
    :type log_file: :class:`InputFile`
    """

    ID: typing.Literal["sendCallLog"] = field(default="sendCallLog", metadata={"alias": "@type"})
    call_id: Int32
    log_file: InputFile
