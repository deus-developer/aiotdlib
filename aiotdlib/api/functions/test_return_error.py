# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    Error,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class TestReturnError(BaseObject):
    """
    Returns the specified error and ensures that the Error object is used; for testing only. Can be called synchronously

    :param error: The error to be returned
    :type error: :class:`Error`
    """

    ID: typing.Literal["testReturnError"] = field(default="testReturnError", metadata={"alias": "@type"})
    error: Error
