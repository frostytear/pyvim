"""
The welcome message. This is displayed when the editor opens without any files.
"""
from __future__ import unicode_literals
from prompt_toolkit.layout.utils import fragment_list_len

import pyvim
import platform
import sys
version = sys.version_info
pyvim_version = pyvim.__version__

__all__ = (
    'WELCOME_MESSAGE_TOKENS',
    'WELCOME_MESSAGE_WIDTH',
    'WELCOME_MESSAGE_HEIGHT',
)

WELCOME_MESSAGE_WIDTH = 34


def _t(fragments):
    """
    Center tokens on this line.
    """
    length = fragment_list_len(fragments)

    return [('class:Welcome', ' ' * int((WELCOME_MESSAGE_WIDTH - length) / 2))] \
        + fragments + [('class:token.Welcome', '\n')]


WELCOME_MESSAGE_TOKENS = (
    _t([('class:welcome.title', 'PyVim - Pure Python Vi clone')]) +
    _t([('class:welcome.body', 'Still experimental')]) +
    _t([('class:welcome.body', '')]) +
    _t([('class:welcome.body', 'version %s' % pyvim_version)]) +
    _t([('class:welcome.body', 'by Jonathan Slenders')]) +
    _t([('class:welcome.body', '')]) +
    _t([('class:welcome.body', 'type :q'),
        ('class:welcome.body.key', '<Enter>'),
        ('class:welcome.body', '            to exit')]) +
    _t([('class:welcome.body', 'type :help'),
        ('class:welcome.body.key', '<Enter>'),
        ('class:welcome.body', ' or '),
        ('class:welcome.body.key', '<F1>'),
        ('class:welcome.body', ' for help')]) +
    _t([('class:welcome.body', '')]) +
    _t([('class:welcome.body', 'All feedback is appreciated.')]) +
    _t([('class:welcome.body', '')]) +
    _t([('class:welcome.body', '')]) +

    _t([('class:welcome.pythonversion', ' %s %i.%i.%i ' % (
        platform.python_implementation(),
        version[0], version[1], version[2]))])
)

WELCOME_MESSAGE_HEIGHT = ''.join(t[1] for t in WELCOME_MESSAGE_TOKENS).count('\n')
