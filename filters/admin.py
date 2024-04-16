from aiogram.filters import BaseFilter
from aiogram.types import Message

from config_data.config import load_config


class IsAdmin(BaseFilter):
    """
    Filter to check if the user is an admin based on their user ID.
    """

    def __init__(self) -> None:
        """
        Initialize the IsAdmin filter.
        """
        self.admin_ids = load_config().tg_bot.admin_ids

    async def __call__(self, message: Message) -> bool:
        """
        Check if the user is an admin.
        """
        return message.from_user.id in self.admin_ids
