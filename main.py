import traceback
import schedule

from src.business.orchestrator import Orchestrator
from src.libs.log import logger
from src.libs.exceptions import ClassError
import time


def main():
    _logger.info("Iniciando execução")
    try:
        orchestrator = Orchestrator()
        orchestrator.orchestrate()
    except ClassError:
        pass
    except Exception as e:
        message = f"Erro inesperado na execução: {e}"
        _logger.error(message)
        _logger.debug(traceback.format_exc())
    _logger.info("Execução finalizada")


def run() -> None:
    schedule.every().day.at("00:00").do(main)
    schedule.run_all()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    _logger = logger(__name__)

    run()
