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
class GetFileDownloadedPrefixSize(BaseObject):
    """
    Returns file downloaded prefix size from a given offset, in bytes

    :param file_id: Identifier of the file
    :type file_id: :class:`Int32`
    :param offset: Offset from which downloaded prefix size needs to be calculated
    :type offset: :class:`Int53`
    """

    ID: typing.Literal["getFileDownloadedPrefixSize"] = field(
        default="getFileDownloadedPrefixSize", metadata={"alias": "@type"}
    )
    file_id: Int32
    offset: Int53
