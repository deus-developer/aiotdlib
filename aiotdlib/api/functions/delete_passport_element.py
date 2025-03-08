# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.all import (
    PassportElementType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class DeletePassportElement(BaseObject):
    """
    Deletes a Telegram Passport element

    :param type_: Element type
    :type type_: :class:`PassportElementType`
    """

    ID: typing.Literal["deletePassportElement"] = field(default="deletePassportElement", metadata={"alias": "@type"})
    type_: PassportElementType = field(default=MISSING, metadata={"alias": "type"})
