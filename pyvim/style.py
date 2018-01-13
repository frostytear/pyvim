"""
The styles, for the colorschemes.
"""
from __future__ import unicode_literals
from prompt_toolkit.styles import Style, merge_styles
from prompt_toolkit.styles.pygments import style_from_pygments

from pygments.styles import get_all_styles, get_style_by_name

__all__ = (
    'generate_built_in_styles',
    'get_editor_style_by_name',
)


def get_editor_style_by_name(name):
    """
    Get Style class.
    This raises `pygments.util.ClassNotFound` when there is no style with this
    name.
    """
    return merge_styles([
        style_from_pygments(get_style_by_name(name)),
        Style.from_dict(style_extensions),
    ])


def generate_built_in_styles():
    """
    Return a mapping from style names to their classes.
    """
    return dict((name, get_editor_style_by_name(name)) for name in get_all_styles())


style_extensions = {
    # Toolbar colors.
    'toolbar.status':                '#ffffff bg:#444444',
    'toolbar.status.cursorposition': '#bbffbb bg:#444444',
    'toolbar.status.percentage':     '#ffbbbb bg:#444444',

    # Flakes color.
    'flakeserror':            'bg:#ff4444 #ffffff',

    # Flake messages
    'flakemessage.prefix':    'bg:#ff8800 #ffffff',
    'flakemessage':           '#886600',

    # Highlighting for the text in the command bar.
    'commandline.command':    'bold',
    'commandline.location':   'bg:#bbbbff #000000',

    # Frame borders (for between vertical splits.)
    'frameborder':            'bold', #bg:#88aa88 #ffffff',

    # Messages
    'message':                'bg:#bbee88 #222222',

    # Welcome message
    'welcome.title':          'underline',
    'welcome.body':           '',
    'welcome.body.key':       '#0000ff',
    'welcome.pythonversion':  'bg:#888888 #ffffff',

    # Tabs
    'tabbar':                 'noinherit reverse',
    'tabbar.tab':             'underline',
    'tabbar.tab.active':      'bold noinherit',

    # Arg count.
    'arg':                    'bg:#cccc44 #000000',

    # Buffer list
    'bufferlist':               'bg:#aaddaa #000000',
    'bufferlist.title':         'underline',
    'bufferlist.lineno':        '#666666',
    'bufferlist.active':        'bg:#ccffcc',
    'bufferlist.active.lineno': '#666666',
    'bufferlist.searchmatch':   'bg:#eeeeaa',

    # Completions toolbar.
    'completions-toolbar':                    'bg:#aaddaa #000000',
    'completions-toolbar.arrow':              'bg:#aaddaa #000000 bold',
    'compeltions-toolbar completion':         'bg:#aaddaa #000000',
    'completions-toolbar current-completion': 'bg:#444444 #ffffff',
}
