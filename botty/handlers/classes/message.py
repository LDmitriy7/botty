from abc import ABC
from typing import cast

from telegram import Message, ext

from botty.handlers.types import PTBHandler, ReplyMarkup

from .update import UpdateFieldError, UpdateHandler


class MessageHandler(UpdateHandler, ABC):
    filters: ext.filters.BaseFilter = ext.filters.UpdateType.MESSAGE

    @classmethod
    def build(cls) -> PTBHandler:
        return ext.MessageHandler(cls.filters, cls._handle)

    async def reply(self, text: str, markup: ReplyMarkup | None = None) -> Message:
        markup = cast(ReplyMarkup, markup)  # fix PTB error
        return await self.message.reply_text(text, reply_markup=markup)

    @property
    def message(self) -> Message:
        value = self.update.message
        if value is None:
            raise UpdateFieldError(self.update, "message")
        return value
