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
class GetFile(BaseObject):
    """
    Returns information about a file; this is an offline request

    :param file_id: Identifier of the file to get
    :type file_id: :class:`Int32`
    """

    ID: typing.Literal["getFile"] = field(default="getFile", metadata={"alias": "@type"})
    file_id: Int32
