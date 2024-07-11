from enum import IntEnum, StrEnum


class ScannerExitStatus(IntEnum):
    """
    Possible end of scan status
    """

    SUCCESS = 0
    FAILED = 84
    UNKNOWN = 85


class ScannerEnum(StrEnum):
    """
    All Available Scanners
    """

    WINDOWS_AD_SCANNER = "windows_ad_scanner"
