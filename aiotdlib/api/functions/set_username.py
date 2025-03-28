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
class SetUsername(BaseObject):
    """
    Changes the editable username of the current user

    :param username: The new value of the username. Use an empty string to remove the username. The username can't be completely removed if there is another active or disabled username
    :type username: :class:`String`
    """

    ID: typing.Literal["setUsername"] = field(default="setUsername", metadata={"alias": "@type"})
    username: String
