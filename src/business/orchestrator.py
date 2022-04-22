import traceback
from src.libs.exceptions import ClassError
from src.business.webdrive import WebBrowser
from src.libs.log import logger


class Orchestrator:
    def __init__(self):
        self._logger = logger(__name__)
        self.webbrowser = WebBrowser()

    def orchestrate(self) -> any:
        try:

            isdayreserve = self.webbrowser.calculate_day_reserve()
            if not isdayreserve:
                return True
            try:
                self.webbrowser.weblogin()
                self._logger.info("Acessando Reservas")
                self.webbrowser.accessreservation()
                self.webbrowser.selectgym()

            except ClassError as e:
                print(str(e))

            except Exception as e:
                message = f"Erro inesperado ao orquestrar execução, erro: {e}"
                self._logger.error(message)
                self._logger.debug(traceback.format_exc())

        except Exception as e:
            message = f"Erro inesperado ao iniciar orquestração da execução: {e}"
            self._logger.error(message)
            self._logger.debug(traceback.format_exc())
