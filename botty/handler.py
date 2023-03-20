from abc import abstractmethod

from telegram import CallbackQuery, Message, Update, ext

Context = ext.ContextTypes.DEFAULT_TYPE


class HandlerFieldError(AttributeError):
    def __init__(self, update: Update, field: str) -> None:
        self.update = update
        self.field = field

    def __str__(self) -> str:
        return f"No `{self.field}` for `{self.update}`"


class Handler:
    on_command: str

    def __init__(self, update: Update, context: Context) -> None:
        self.update = update
        self.context = context

    @abstractmethod
    async def callback(self) -> None:
        """Will be called on trigger."""

    @property
    def message(self) -> Message:
        value = self.update.effective_message
        if value is None:
            raise HandlerFieldError(self.update, "message")
        return value

    @property
    def query(self) -> CallbackQuery:
        value = self.update.callback_query
        if value is None:
            raise HandlerFieldError(self.update, "query")
        return value

    @classmethod
    async def handle(cls, update: Update, context: Context) -> None:
        handler = cls(update, context)
        await handler.callback()

    @classmethod
    def build(cls) -> ext.CommandHandler[Context]:
        return ext.CommandHandler(cls.on_command, cls.handle)

    async def reply(self, text: str) -> Message:
        return await self.message.reply_text(text)
