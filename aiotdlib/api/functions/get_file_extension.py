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
class GetFileExtension(BaseObject):
    """
    Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. Can be called synchronously

    :param mime_type: The MIME type of the file
    :type mime_type: :class:`String`
    """

    ID: typing.Literal["getFileExtension"] = field(default="getFileExtension", metadata={"alias": "@type"})
    mime_type: String
