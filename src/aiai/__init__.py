"""
.. include:: ../../README.md
"""

import logging
import os

import pkg_resources
from aiai_eval.evaluator import Evaluator  # noqa
from termcolor import colored

# Fetches the version of the package as defined in pyproject.toml
__version__ = pkg_resources.get_distribution("aiai").version


# Set up logging
fmt = colored("%(asctime)s [%(levelname)s] <%(name)s>\n↳ ", "cyan") + colored(
    "%(message)s", "yellow"
)
logging.basicConfig(level=logging.INFO, format=fmt)


# Disable parallelisation when tokenizing, as that can lead to errors
os.environ["TOKENIZERS_PARALLELISM"] = "false"


# Tell Windows machines to use UTF-8 encoding
os.environ["ConEmuDefaultCp"] = "65001"
os.environ["PYTHONIOENCODING"] = "UTF-8"
