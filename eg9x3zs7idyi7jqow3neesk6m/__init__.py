from importlib.metadata import version, PackageNotFoundError
from .eg9x3zs7idyi7jqow3neesk6m import eg9x3zs7idyi7jqow3neesk6m as _

try:
    __version__ = version("eg9x3zs7idyi7jqow3neesk6m")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["_", "__version__"]
