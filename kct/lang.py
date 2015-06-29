from .settings.py import *

lang = {};

if LANGUAGE_CODE == 'en-us':
	lang['name'] = 'lianggouming';
	lang['version'] = 'version-0.1';
elif LANGUAGE_CODE == 'zh-hans':
	lang['name'] = '梁够明';
	lang['version'] = '版本-0.1';