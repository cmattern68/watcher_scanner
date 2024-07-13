from enum import IntEnum, StrEnum


class ScannerExitStatus(IntEnum):
    """
    Possible end of scan status
    """

    SUCCESS = 0
    FAILED = 84
    UNKNOWN = 85


class ScannerState(StrEnum):
    """
    Scanner Modules States
    """

    LOADED = "loaded"
    FAILED = "failed"
    NOT_FOUND = "not_found"
    RUNTIME_ERROR = "runtime_errpr"
    BUSY = "busy"
    RUNNING = "running"
    UNINITIALIZED = "uninitialized"


class ScannerEnum(StrEnum):
    """
    All Available Scanners
    """

    WINDOWS_AD_SCANNER = "windows_ad_scanner"
