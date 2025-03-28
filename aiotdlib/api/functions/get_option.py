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
class GetOption(BaseObject):
    """
    Returns the value of an option by its name. (Check the list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization. Can be called synchronously for options "version" and "commit_hash"

    :param name: The name of the option
    :type name: :class:`String`
    """

    ID: typing.Literal["getOption"] = field(default="getOption", metadata={"alias": "@type"})
    name: String
