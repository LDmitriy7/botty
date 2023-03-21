import warnings

from telegram.ext import Application
from telegram.warnings import PTBUserWarning

from .handlers import HandlerClass, Handlers

warnings.filterwarnings(
    action="ignore",
    message=".* should be built via the `ApplicationBuilder`",
    category=PTBUserWarning,
)


class App:
    def __init__(self, token: str):
        self.raw = Application.builder().token(token).build()

    def _add_handler(self, handler: HandlerClass) -> None:
        self.raw.add_handler(handler.build())

    def run(self, handlers: Handlers) -> None:
        for handler in handlers:
            self._add_handler(handler)
        self.raw.run_polling()
