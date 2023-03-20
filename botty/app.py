import warnings

from handler import Handler
from telegram.ext import Application
from telegram.warnings import PTBUserWarning

warnings.filterwarnings(
    action="ignore",
    message=".* should be built via the `ApplicationBuilder`",
    category=PTBUserWarning,
)

HandlerClass = type[Handler]


class App:
    def __init__(self, token: str) -> None:
        self.raw = Application.builder().token(token).build()

    def _add_handler(self, handler: HandlerClass) -> None:
        self.raw.add_handler(handler.build())

    def run(self, handlers: list[HandlerClass]) -> None:
        for handler in handlers:
            self._add_handler(handler)
        self.raw.run_polling()
