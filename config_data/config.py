from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    """Stores configuration for the database."""
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class TgBot:
    """Stores configuration for the Telegram bot."""
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    """Stores the overall configuration."""
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str = 'env/.env') -> Config:
    """
    Load configuration from environment variables.

    Args:
        path (str, optional): Path to the environment file. Defaults to 'env/.env'.

    Returns:
        Config: The loaded configuration.
    """
    env = Env()
    env.read_env(path)

    tg_bot_config = TgBot(
        token=env('BOT_TOKEN'),
        admin_ids=list(map(int, env.list('ADMIN_IDS')))
    )

    db_config = DatabaseConfig(
        database=env('POSTGRES_DB'),
        db_host=env('DB_HOST'),
        db_user=env('POSTGRES_USER'),
        db_password=env('POSTGRES_PASSWORD')
    )

    return Config(tg_bot=tg_bot_config, db=db_config)
