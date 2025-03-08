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
class GetPassportElement(BaseObject):
    """
    Returns one of the available Telegram Passport elements

    :param type_: Telegram Passport element type
    :type type_: :class:`PassportElementType`
    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    """

    ID: typing.Literal["getPassportElement"] = field(default="getPassportElement", metadata={"alias": "@type"})
    type_: PassportElementType = field(default=MISSING, metadata={"alias": "type"})
    password: String
