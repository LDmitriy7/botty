from abc import ABC

from telegram import CallbackQuery

from .update import UpdateFieldError, UpdateHandler


class QueryHandler(UpdateHandler, ABC):
    async def answer(self, text: str, *, show_alert: bool = False) -> bool:
        return await self.query.answer(text, show_alert)

    @property
    def query(self) -> CallbackQuery:
        value = self.update.callback_query
        if value is None:
            raise UpdateFieldError(self.update, "query")
        return value
