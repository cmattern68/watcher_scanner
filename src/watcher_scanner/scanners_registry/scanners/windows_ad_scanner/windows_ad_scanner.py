from typing import Any

from src.watcher_scanner.scanners_registry.scanners.scanner import Scanner
from src.watcher_scanner.scanners_registry.schema import ScannerEnum, ScannerExitStatus


class WindowsADScanner(Scanner):
    """
    Windows Active Directory Scanner
    """

    _scanner_type = ScannerEnum.WINDOWS_AD_SCANNER

    def run(self, payload: Any) -> ScannerExitStatus:
        """
        Method to run the scan for WindowsADScanner
        """
        print(f"Run scan for {self._scanner_type} scanner type")
        return ScannerExitStatus.UNKNOWN

    def report(self):
        """
        Method to generate the report from the data for WindowsADScanner
        """
        return None
