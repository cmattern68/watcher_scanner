from datetime import datetime

from src.watcher_scanner.scanners_registry import ScannersRegistry


class OneShotRunner:
    """
    Class used to run One Shot, instead of a consuming/producing service
    """

    _exec_date: datetime
    _requested_scanner: str
    _modules = ScannersRegistry = ScannersRegistry()

    def run(
        self, exec_date: datetime = datetime.now(), requested_scanner: str = "windows_ad"
    ) -> None:
        """
        Method called to run a One Shot scan
        """
        self._exec_date = exec_date
        self._requested_scanner = requested_scanner
        self._modules.load()

    @property
    def exec_date(self) -> datetime:
        """
        Getter for self._exec_date
        """
        return self._exec_date
