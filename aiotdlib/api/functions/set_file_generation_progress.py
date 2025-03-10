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
class SetFileGenerationProgress(BaseObject):
    """
    Informs TDLib on a file generation progress

    :param generation_id: The identifier of the generation process
    :type generation_id: :class:`Int64`
    :param local_prefix_size: The number of bytes already generated
    :type local_prefix_size: :class:`Int53`
    :param expected_size: Expected size of the generated file, in bytes; 0 if unknown, defaults to None
    :type expected_size: :class:`Int53`, optional
    """

    ID: typing.Literal["setFileGenerationProgress"] = field(
        default="setFileGenerationProgress", metadata={"alias": "@type"}
    )
    generation_id: Int64
    local_prefix_size: Int53
    expected_size: typing.Optional[Int53] = field(default=0)
