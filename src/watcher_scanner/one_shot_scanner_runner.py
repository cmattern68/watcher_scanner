from datetime import datetime
from typing import Optional

from src.watcher_scanner.lib.logger import Logger
from src.watcher_scanner.scanners_registry.scanners_registry import ScannersRegistry
from src.watcher_scanner.scanners_registry.schema import ScannerEnum

Logger()


class OneShotScannerRunner:
    """
    Class used to run One Shot, instead of a consuming/producing service
    """

    _exec_date: Optional[datetime] = None
    _requested_scanner: Optional[ScannerEnum] = None
    _scanners = ScannersRegistry = ScannersRegistry()

    def __init__(self, requested_scanner: ScannerEnum) -> None:
        """
        Init OneShotScannerRunner with the requested scanner
        """
        self._requested_scanner = requested_scanner
        self._scanners.load(scanners=[self._requested_scanner])

    def run(self, exec_date: datetime = datetime.now()) -> None:
        """
        Method called to run a One Shot scan
        """
        self._exec_date = exec_date

    @property
    def exec_date(self) -> datetime | None:
        """
        Getter for self._exec_date
        """
        return self._exec_date
