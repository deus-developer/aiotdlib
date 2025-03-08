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
class RemoveSavedAnimation(BaseObject):
    """
    Removes an animation from the list of saved animations

    :param animation: Animation file to be removed
    :type animation: :class:`InputFile`
    """

    ID: typing.Literal["removeSavedAnimation"] = field(default="removeSavedAnimation", metadata={"alias": "@type"})
    animation: InputFile
