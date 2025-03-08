# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    LogStream,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetLogStream(BaseObject):
    """
    Sets new log stream for internal logging of TDLib. Can be called synchronously

    :param log_stream: New log stream
    :type log_stream: :class:`LogStream`
    """

    ID: typing.Literal["setLogStream"] = field(default="setLogStream", metadata={"alias": "@type"})
    log_stream: LogStream
