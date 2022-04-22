import os
from dotenv import load_dotenv
from src.models.config import Env

class Config:
    def __init__(self):
        load_dotenv()
        self.env: Env = Env(
            user_login=os.getenv('USER_LOGIN'),
            password_login=os.getenv('PASSWORD_LOGIN'),
            time_reserve_default=os.getenv('TIME_RESERVE_DEFAULT'),
            time_reserve_custom=os.getenv('TIME_RESERVE_CUSTOM'),
            url=os.getenv('URL')
        )
        self.days = {
                1: 'Segunda-feira',
                2: 'Terça-feira',
                3: 'Quarta-feira',
                4: 'Quinta-Feira',
                5: 'Sexta-feira',
                6: 'Sábado',
                7: 'Domingo'}