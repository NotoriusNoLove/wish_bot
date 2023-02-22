# место где регаются команды
__all__ = ['register_user_commands', 'start']

# импорт библиотек
from aiogram import F
from aiogram import Router
from aiogram.filters.command import CommandStart
from commands.start import start


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
