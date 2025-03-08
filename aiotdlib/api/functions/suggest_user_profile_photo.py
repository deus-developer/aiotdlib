# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputChatPhoto,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SuggestUserProfilePhoto(BaseObject):
    """
    Suggests a profile photo to another regular user with common messages

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param photo: Profile photo to suggest; inputChatPhotoPrevious isn't supported in this function
    :type photo: :class:`InputChatPhoto`
    """

    ID: typing.Literal["suggestUserProfilePhoto"] = field(
        default="suggestUserProfilePhoto", metadata={"alias": "@type"}
    )
    user_id: Int53
    photo: InputChatPhoto
