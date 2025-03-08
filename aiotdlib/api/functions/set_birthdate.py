# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    Birthdate,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetBirthdate(BaseObject):
    """
    Changes the birthdate of the current user

    :param birthdate: The new value of the current user's birthdate; pass null to remove the birthdate, defaults to None
    :type birthdate: :class:`Birthdate`, optional
    """

    ID: typing.Literal["setBirthdate"] = field(default="setBirthdate", metadata={"alias": "@type"})
    birthdate: typing.Optional[Birthdate] = field(default=None)
