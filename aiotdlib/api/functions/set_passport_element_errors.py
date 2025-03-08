# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputPassportElementError,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetPassportElementErrors(BaseObject):
    """
    Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param errors: The errors
    :type errors: :class:`Vector[InputPassportElementError]`
    """

    ID: typing.Literal["setPassportElementErrors"] = field(
        default="setPassportElementErrors", metadata={"alias": "@type"}
    )
    user_id: Int53
    errors: Vector[InputPassportElementError]
