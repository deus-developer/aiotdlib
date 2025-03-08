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
class CancelPreliminaryUploadFile(BaseObject):
    """
    Stops the preliminary uploading of a file. Supported only for files uploaded by using preliminaryUploadFile

    :param file_id: Identifier of the file to stop uploading
    :type file_id: :class:`Int32`
    """

    ID: typing.Literal["cancelPreliminaryUploadFile"] = field(
        default="cancelPreliminaryUploadFile", metadata={"alias": "@type"}
    )
    file_id: Int32
