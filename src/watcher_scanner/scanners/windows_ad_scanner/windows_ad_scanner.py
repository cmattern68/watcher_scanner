import logging
from datetime import datetime
from typing import Any

from src.watcher_scanner.scanners.scanner import Scanner
from src.watcher_scanner.schema import ScannerEnum, ScannerExitStatus, ScannerState


class WindowsADScanner(Scanner):
    """
    Windows Active Directory Scanner
    """

    _type = ScannerEnum.WINDOWS_AD_SCANNER

    def run(
        self, payload: Any, exec_time: datetime = datetime.now()
    ) -> ScannerExitStatus:
        """
        Method to run the scan for WindowsADScanner
        """
        self._exec_time = exec_time
        self._state = ScannerState.RUNNING
        logging.info(f"Run scan for {self._type} scanner type on state {self._state}")
        return ScannerExitStatus.UNKNOWN

    def report(self):
        """
        Method to generate the report from the data for WindowsADScanner
        """
        return None
