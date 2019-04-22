import os
import sys

from bentoml import archive
from bentoml.cli import create_bentoml_cli

__VERSION__ = "0.0.2019_04_22_e5d9f7d0"

__module_path = os.path.abspath(os.path.dirname(__file__))

TextClassificationService = archive.load_bento_service_class(__module_path)

cli=create_bentoml_cli(__module_path)

def load():
    return archive.load(__module_path)

__all__ = ['__version__', 'TextClassificationService', 'load']
