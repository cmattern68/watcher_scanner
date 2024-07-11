from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from src.watcher_scanner.scanners_registry.schema import ScannerEnum, ScannerExitStatus


class Scanner(ABC):
    """
    Scanner Interface for all implemented scanners
    """

    _scanner_type: ScannerEnum

    def __init__(self) -> None:
        self._start_time = datetime.now()

    @property
    def start_time(self) -> datetime:
        """
        Property for self._start_time
        """
        return self._start_time

    @property
    def scanner_type(self) -> ScannerEnum:
        """
        Property for self._scanner_type
        """
        return self._scanner_type

    @abstractmethod
    def run(self, payload: Any) -> ScannerExitStatus:
        """
        Method to run the scan from a specific payload
        """
        raise NotImplementedError

    @abstractmethod
    def report(self):
        """
        Method to generate the report from the data
        """
        raise NotImplementedError
