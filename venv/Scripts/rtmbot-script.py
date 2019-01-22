#!C:\Users\orsha\PycharmProjects\AVERAGEBOT\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rtmbot==0.4.1','console_scripts','rtmbot'
__requires__ = 'rtmbot==0.4.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('rtmbot==0.4.1', 'console_scripts', 'rtmbot')()
    )
