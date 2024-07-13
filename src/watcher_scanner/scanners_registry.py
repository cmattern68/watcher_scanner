import logging
from typing import Dict, List, Optional

from src.watcher_scanner.lib.exception import (
    ScannersLoadingException,
    ScannersNotFoundException,
)
from src.watcher_scanner.lib.logger import LogContextModel, log_context_var
from src.watcher_scanner.scanners import WindowsADScanner  # pylint: disable=C0301
from src.watcher_scanner.scanners.scanner import Scanner
from src.watcher_scanner.schema import ScannerEnum

SCANNERS_BOOK = {ScannerEnum.WINDOWS_AD_SCANNER: WindowsADScanner}


class ScannersRegistry:
    """
    Scanner Registry Manager
    """

    _scanners: Dict[ScannerEnum, Scanner] = {}

    def load(self, scanners: Optional[List[ScannerEnum]]):
        """
        Method called to load Scanner from #ToDefine# folder
        """

        if scanners is not None:
            for scanner in scanners:
                requested_scanner = SCANNERS_BOOK.get(scanner, None)
                if requested_scanner is not None:
                    self._scanners[scanner] = requested_scanner()
                else:
                    logging.error(f"{scanner} scanner type is not registered")

            log_context_var.set(
                LogContextModel(
                    loaded_scanners=" - ".join(self._scanners.keys()),
                )
            )
        logging.debug("All scanners have been successfuly loaded")
        if len(self._scanners) == 0:
            logging.error("Unable to load any scanners")
            raise ScannersLoadingException("No scanners loaded")

    def get(self, scanner_type: ScannerEnum) -> Scanner:
        """
        Method to get specific scanner from self._scanners
        """
        try:
            return self._scanners[scanner_type]
        except KeyError as expt:
            raise ScannersNotFoundException(
                f"{scanner_type} does not exists has not been loaded"
            ) from expt
