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
class SetUserPersonalProfilePhoto(BaseObject):
    """
    Changes a personal profile photo of a contact user

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param photo: Profile photo to set; pass null to delete the photo; inputChatPhotoPrevious isn't supported in this function, defaults to None
    :type photo: :class:`InputChatPhoto`, optional
    """

    ID: typing.Literal["setUserPersonalProfilePhoto"] = field(
        default="setUserPersonalProfilePhoto", metadata={"alias": "@type"}
    )
    user_id: Int53
    photo: typing.Optional[InputChatPhoto] = field(default=None)
