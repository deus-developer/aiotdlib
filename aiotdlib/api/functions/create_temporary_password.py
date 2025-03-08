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
class CreateTemporaryPassword(BaseObject):
    """
    Creates a new temporary password for processing payments

    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    :param valid_for: Time during which the temporary password will be valid, in seconds; must be between 60 and 86400
    :type valid_for: :class:`Int32`
    """

    ID: typing.Literal["createTemporaryPassword"] = field(
        default="createTemporaryPassword", metadata={"alias": "@type"}
    )
    password: String
    valid_for: Int32
