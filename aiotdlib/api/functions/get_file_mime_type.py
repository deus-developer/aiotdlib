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
class GetFileMimeType(BaseObject):
    """
    Returns the MIME type of a file, guessed by its extension. Returns an empty string on failure. Can be called synchronously

    :param file_name: The name of the file or path to the file
    :type file_name: :class:`String`
    """

    ID: typing.Literal["getFileMimeType"] = field(default="getFileMimeType", metadata={"alias": "@type"})
    file_name: String
