from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from src.watcher_scanner.schema import ScannerEnum, ScannerExitStatus, ScannerState


class Scanner(ABC):
    """
    Scanner Interface for all implemented scanners
    """

    _type: ScannerEnum
    _exec_time: datetime
    _state: ScannerState = ScannerState.UNINITIALIZED

    def __init__(self) -> None:
        self._start_time = datetime.now()
        self._state = ScannerState.LOADED

    @property
    def start_time(self) -> datetime:
        """
        Property for self._start_time
        """
        return self._start_time

    @property
    def type(self) -> ScannerEnum:
        """
        Property for self._type
        """
        return self._type

    @property
    def exec_time(self) -> str:
        """
        Property for self._type as string
        """
        return self._exec_time.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def state(self) -> ScannerState:
        """
        Property for self._state
        """
        return self._state

    @abstractmethod
    def run(
        self, payload: Any, exec_time: datetime = datetime.now()
    ) -> ScannerExitStatus:
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
