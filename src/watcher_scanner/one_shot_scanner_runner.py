from datetime import datetime
from typing import Any, Optional

from src.watcher_scanner.lib.exception import (
    OneShotScannerException,
    ScannersLoadingException,
)
from src.watcher_scanner.lib.logger import Logger
from src.watcher_scanner.scanners_registry import ScannersRegistry
from src.watcher_scanner.schema import ScannerEnum

Logger()


class OneShotScannerRunner:
    """
    Class used to run One Shot, instead of a consuming/producing service
    """

    _exec_date: Optional[datetime] = None
    _requested_scanner: ScannerEnum
    _scanners = ScannersRegistry = ScannersRegistry()

    def __init__(self, requested_scanner: ScannerEnum) -> None:
        """
        Init OneShotScannerRunner with the requested scanner
        """
        try:
            self._requested_scanner = requested_scanner
            self._scanners.load(scanners=[self._requested_scanner])
        except ScannersLoadingException as expt:
            raise OneShotScannerException(
                "Unable to initiate OneShotScannerRunner"
            ) from expt

    def run(self, payload: Any, exec_date: datetime = datetime.now()) -> None:
        """
        Method called to run a One Shot scan
        """
        self._exec_date = exec_date
        scanner = self._scanners.get(self._requested_scanner)
        scanner.run(payload=payload)

    @property
    def exec_date(self) -> datetime | None:
        """
        Getter for self._exec_date
        """
        return self._exec_date
