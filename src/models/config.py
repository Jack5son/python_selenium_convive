from pydantic import BaseModel


class Env(BaseModel):
    user_login: str
    password_login: str
    time_reserve_default: str
    time_reserve_custom: str
    url: str
