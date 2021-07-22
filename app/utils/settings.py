from environs import Env
from dataclasses import dataclass


env = Env()
env.read_env()


@dataclass(frozen=True)
class Settings:
    bot_token: str = env("BOT_TOKEN")
