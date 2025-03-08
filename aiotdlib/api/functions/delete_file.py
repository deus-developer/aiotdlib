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
class DeleteFile(BaseObject):
    """
    Deletes a file from the TDLib file cache

    :param file_id: Identifier of the file to delete
    :type file_id: :class:`Int32`
    """

    ID: typing.Literal["deleteFile"] = field(default="deleteFile", metadata={"alias": "@type"})
    file_id: Int32
