# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    FormattedText,
    LinkPreviewOptions,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetLinkPreview(BaseObject):
    """
    Returns a link preview by the text of a message. Do not call this function too often. Returns a 404 error if the text has no link preview

    :param text: Message text with formatting
    :type text: :class:`FormattedText`
    :param link_preview_options: Options to be used for generation of the link preview; pass null to use default link preview options, defaults to None
    :type link_preview_options: :class:`LinkPreviewOptions`, optional
    """

    ID: typing.Literal["getLinkPreview"] = field(default="getLinkPreview", metadata={"alias": "@type"})
    text: FormattedText
    link_preview_options: typing.Optional[LinkPreviewOptions] = field(default=None)
