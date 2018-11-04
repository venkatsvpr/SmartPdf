import PyPDF2
import magic
import hashlib
import tempfile
import comtypes.client
import re
import os
from comtypes import CoInitialize

TEMPORARY_DIR_PATH = None

TEMPORARY = "D:/Temp"
