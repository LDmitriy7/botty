from abc import ABC, abstractmethod

from telegram import Update, ext

from botty.handlers.handler import Handler
from botty.handlers.types import Context, PTBHandler


class UpdateHandler(Handler, ABC):

    def __init__(self, update: Update, context: Context):
        self.update = update
        self.context = context

    @classmethod
    def build(cls) -> PTBHandler:
        return ext.TypeHandler(Update, cls._handle)

    @classmethod
    async def _handle(cls, update: Update, context: Context) -> None:
        handler = cls(update, context)
        await handler.callback()

    @abstractmethod
    async def callback(self) -> None:
        """Will be called to handle update."""


class UpdateFieldError(AttributeError):
    def __init__(self, update: Update, field: str) -> None:
        self.update = update
        self.field = field

    def __str__(self) -> str:
        return f"No `{self.field}` for `{self.update}`"
