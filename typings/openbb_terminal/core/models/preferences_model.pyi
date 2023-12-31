"""
This type stub file was generated by pyright.
"""

from typing import Literal, Optional
from pydantic import NonNegativeInt, PositiveFloat, PositiveInt
from pydantic.dataclasses import dataclass
from openbb_terminal.core.models import BaseModel

@dataclass(config=dict(validate_assignment=True, frozen=True))
class PreferencesModel(BaseModel):
    """Data model for preferences."""
    PLOT_BACKEND: Optional[str] = ...
    PLOT_DPI: PositiveInt = ...
    PLOT_HEIGHT: PositiveInt = ...
    PLOT_WIDTH: PositiveInt = ...
    PLOT_HEIGHT_PERCENTAGE: PositiveFloat = ...
    PLOT_WIDTH_PERCENTAGE: PositiveFloat = ...
    PLOT_OPEN_EXPORT: bool = ...
    PLOT_ENABLE_PYWRY: bool = ...
    PLOT_PYWRY_WIDTH: PositiveInt = ...
    PLOT_PYWRY_HEIGHT: PositiveInt = ...
    FILE_OVERWRITE: bool = ...
    SHOW_VERSION: bool = ...
    RETRY_WITH_LOAD: bool = ...
    USE_TABULATE_DF: bool = ...
    USE_INTERACTIVE_DF: bool = ...
    USE_CLEAR_AFTER_CMD: bool = ...
    USE_DATETIME: bool = ...
    USE_PROMPT_TOOLKIT: bool = ...
    USE_PLOT_AUTOSCALING: bool = ...
    ENABLE_THOUGHTS_DAY: bool = ...
    ENABLE_QUICK_EXIT: bool = ...
    OPEN_REPORT_AS_HTML: bool = ...
    ENABLE_EXIT_AUTO_HELP: bool = ...
    REMEMBER_CONTEXTS: bool = ...
    ENABLE_RICH_PANEL: bool = ...
    ENABLE_CHECK_API: bool = ...
    TOOLBAR_HINT: bool = ...
    PREVIOUS_USE: bool = ...
    TIMEZONE: str = ...
    FLAIR: str = ...
    USE_LANGUAGE: str = ...
    REQUEST_TIMEOUT: PositiveInt = ...
    MONITOR: NonNegativeInt = ...
    MPL_STYLE: str = ...
    PMF_STYLE: str = ...
    RICH_STYLE: str = ...
    CHART_STYLE: Literal["dark", "light"] = ...
    TABLE_STYLE: Literal["dark", "light"] = ...
    GUESS_EASTER_EGG_FILE: str = ...
    USER_DATA_DIRECTORY = ...
    USER_DATA_SOURCES_FILE: str = ...
    USER_EXPORTS_DIRECTORY = ...
    USER_CUSTOM_IMPORTS_DIRECTORY = ...
    USER_PORTFOLIO_DATA_DIRECTORY = ...
    USER_ROUTINES_DIRECTORY = ...
    USER_PRESETS_DIRECTORY = ...
    USER_REPORTS_DIRECTORY = ...
    USER_CUSTOM_REPORTS_DIRECTORY = ...
    USER_FORECAST_MODELS_DIRECTORY = ...
    USER_FORECAST_WHISPER_DIRECTORY = ...
    USER_STYLES_DIRECTORY = ...
    def __repr__(self) -> str:
        ...
    


