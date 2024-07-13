from src.watcher_scanner.one_shot_scanner_runner import OneShotScannerRunner


scanner = OneShotScannerRunner(
    requested_scanner="windows_ad_scanner"
)
scanner.run(
    {}
)
