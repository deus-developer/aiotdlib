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
class ToggleUsernameIsActive(BaseObject):
    """
    Changes active state for a username of the current user. The editable username can't be disabled. May return an error with a message "USERNAMES_ACTIVE_TOO_MUCH" if the maximum number of active usernames has been reached

    :param username: The username to change
    :type username: :class:`String`
    :param is_active: Pass true to activate the username; pass false to disable it
    :type is_active: :class:`Bool`
    """

    ID: typing.Literal["toggleUsernameIsActive"] = field(default="toggleUsernameIsActive", metadata={"alias": "@type"})
    username: String
    is_active: Bool = field(default=False)
