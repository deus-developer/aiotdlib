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
class GetAllPassportElements(BaseObject):
    """
    Returns all available Telegram Passport elements

    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    """

    ID: typing.Literal["getAllPassportElements"] = field(default="getAllPassportElements", metadata={"alias": "@type"})
    password: String
