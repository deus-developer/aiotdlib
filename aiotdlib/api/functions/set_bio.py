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
class SetBio(BaseObject):
    """
    Changes the bio of the current user

    :param bio: The new value of the user bio; 0-getOption("bio_length_max") characters without line feeds
    :type bio: :class:`String`
    """

    ID: typing.Literal["setBio"] = field(default="setBio", metadata={"alias": "@type"})
    bio: String
