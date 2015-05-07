"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['files']
OPTIONS = {
            'iconfile': 'icon.icns',
            'includes': ['PySide.QtCore', 'PySide.QtGui', 'PySide.QtNetwork', 'configobj', 'PIL.Jpeg2KImagePlugin'],
            'packages': ['PIL'],
            'excludes': ['numpy', 'matplotlib', 'PyQt5', 'PySide.QtXmlPatterns', 'PySide.QtWebEngineCore', 'PySide.QtDesigner', 'PySide.QtScript', 'PySide.QtWebkit', 'Cython', 'selenium', 'scapy', 'pytz', 'pygments', 'pip', 'netaddr', 'mercurial', 'cx_Freeze', 'bpython', 'astroid', 'Shiboken', 'PyInstaller', 'sip', 'llvmpy', 'llvm', 'pylint', 'unittest', 'pysideuic', 'email', 'Tkinter', 'multiprocessing', 'yaml', 'logilab', 'urwid', 'test', 'networkx' ],
            'dylib_excludes':['QtXml.framework', 'QtWebkit.framework', 'QtScript.framework', 'QtDesigner.framework', 'QtWebEngineCore.framework', 'QtXmlPatterns.framework', 'QtNetwork.framework', 'QtGui.framework', 'QtCore.framework']
        }

setup(
    name='Web2Executable',
    version='0.2.2b',
    app=APP,
    author='Joey Payne',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
