import logging

from structlog import configure, stdlib, get_logger
from structlog.contextvars import merge_contextvars
from structlog.stdlib import ProcessorFormatter, ExtraAdder, add_logger_name
from structlog.processors import TimeStamper, UnicodeDecoder, StackInfoRenderer, format_exc_info

import fwzzlhjtb520ky7cblteynsev as the_log_types
import mijdauya2j3h7lg3d8hcl6qkk as add_log_level

import v3ujgujq4i6tl12ekdt67jlrj as Custom_Logger
import tgkprp3uv0su7oiiiss0xy8db as Custom_Struct_Logger
import ova1dei6r5u67vbwazwbq1o2y as Custom_Logger_Factory

for _log_type_ in the_log_types._:
    logging.addLevelName(_log_type_.level, _log_type_.to_string())
    stdlib.LEVEL_TO_NAME[_log_type_.level] = _log_type_.to_string()
    stdlib.NAME_TO_LEVEL[_log_type_.to_string()] = _log_type_.level

logging.setLoggerClass(Custom_Logger._)

configure(
    wrapper_class=Custom_Struct_Logger._,
    logger_factory=Custom_Logger_Factory._(),
    processors=[
        merge_contextvars,
        ExtraAdder(),
        add_log_level._,
        add_logger_name,
        TimeStamper(fmt="iso"),
        StackInfoRenderer(),
        format_exc_info,
        UnicodeDecoder(),
        ProcessorFormatter.wrap_for_formatter,
    ],
)


def eg9x3zs7idyi7jqow3neesk6m() -> Custom_Struct_Logger._:
    return get_logger("default")
