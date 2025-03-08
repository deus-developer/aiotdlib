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
class GetSuggestedFileName(BaseObject):
    """
    Returns suggested name for saving a file in a given directory

    :param file_id: Identifier of the file
    :type file_id: :class:`Int32`
    :param directory: Directory in which the file is expected to be saved
    :type directory: :class:`String`
    """

    ID: typing.Literal["getSuggestedFileName"] = field(default="getSuggestedFileName", metadata={"alias": "@type"})
    file_id: Int32
    directory: String
