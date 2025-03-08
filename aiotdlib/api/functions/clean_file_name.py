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
class CleanFileName(BaseObject):
    """
    Removes potentially dangerous characters from the name of a file. Returns an empty string on failure. Can be called synchronously

    :param file_name: File name or path to the file
    :type file_name: :class:`String`
    """

    ID: typing.Literal["cleanFileName"] = field(default="cleanFileName", metadata={"alias": "@type"})
    file_name: String
