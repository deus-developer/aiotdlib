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
class DeleteProfilePhoto(BaseObject):
    """
    Deletes a profile photo

    :param profile_photo_id: Identifier of the profile photo to delete
    :type profile_photo_id: :class:`Int64`
    """

    ID: typing.Literal["deleteProfilePhoto"] = field(default="deleteProfilePhoto", metadata={"alias": "@type"})
    profile_photo_id: Int64
