import logging
from typing import Dict, List, Optional

from src.watcher_scanner.lib.logger import LogContextModel, log_context_var
from src.watcher_scanner.scanners_registry.scanners.scanner import Scanner
from src.watcher_scanner.scanners_registry.scanners.windows_ad_scanner.windows_ad_scanner import (  # pylint: disable=C0301
    WindowsADScanner,
)
from src.watcher_scanner.scanners_registry.schema import ScannerEnum

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
                    logging.error(  # pylint: disable=W1203
                        f"{scanner} scanner type is not registered"
                    )

            log_context_var.set(
                LogContextModel(
                    modules=", ".join(scanners),
                    requested_scanner=" - ".join(self._scanners.keys()),
                )
            )
        logging.debug("All scanners have been successfuly loaded")
