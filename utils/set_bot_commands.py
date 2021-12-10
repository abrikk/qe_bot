from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

from loader import bot


async def set_default_commands(dp):
    usercommands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Справка по использованию бота"),
        BotCommand(command="quadratic_equation", description="Решить квадратное уравнение"),
        BotCommand(command="test", description="Начать тестирование")
    ]
    await bot.set_my_commands(usercommands, scope=BotCommandScopeDefault())

    admin_commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Справка по использованию бота"),
        BotCommand(command="quadratic_equation", description="Решить квадратное уравнение"),
        BotCommand(command="test", description="Начать тестирование"),
        BotCommand(command="show_state", description="Показать текущее состояние"),
        BotCommand(command="add_admin", description="Добавить админа"),
        BotCommand(command="remove_admin", description="Удалить админа"),
        BotCommand(command="statistics", description="Посмотреть статистику бота.")
    ]
    await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=569356638))

