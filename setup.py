from setuptools import setup

APP = ['Desktop_Countdown.py']
DATA_FILES = ['eventsfr.json']
OPTIONS = {
    'iconfile': 'app_icon.ico',
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
)
