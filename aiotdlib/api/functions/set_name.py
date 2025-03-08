# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetName(BaseObject):
    """
    Changes the first and last name of the current user

    :param first_name: The new value of the first name for the current user; 1-64 characters
    :type first_name: :class:`String`
    :param last_name: The new value of the optional last name for the current user; 0-64 characters
    :type last_name: :class:`String`
    """

    ID: typing.Literal["setName"] = field(default="setName", metadata={"alias": "@type"})
    first_name: String = field(default=MISSING, metadata={"min_length": 1, "max_length": 64})
    last_name: String = field(default="", metadata={"max_length": 64})
