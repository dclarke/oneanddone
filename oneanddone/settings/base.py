# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from django.core.urlresolvers import reverse_lazy

from funfactory.settings_base import *


# Django Settings
##############################################################################

# Defines the views served for root URLs.
ROOT_URLCONF = 'oneanddone.urls'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

INSTALLED_APPS = (
    'oneanddone.base',

    # Django contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    # Third-party apps.
    'commonware.response.cookies',
    'django_browserid',
    'django_nose',
    'funfactory',
    'jingo_minify',
    'product_details',
    'south',
    'tower',
    'session_csrf',
)

MIDDLEWARE_CLASSES = (
    'funfactory.middleware.LocaleURLMiddleware',
    'multidb.middleware.PinningRouterMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'session_csrf.CsrfMiddleware',  # Must be after auth middleware.
    'django.contrib.messages.middleware.MessageMiddleware',
    'commonware.middleware.FrameOptionsHeader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'session_csrf.context_processor',
    'django.contrib.messages.context_processors.messages',
    'funfactory.context_processors.i18n',
    'funfactory.context_processors.globals',
    'django_browserid.context_processors.browserid',
)

AUTHENTICATION_BACKENDS = (
   'django.contrib.auth.backends.ModelBackend',
   'django_browserid.auth.BrowserIDBackend',
)

LOCALE_PATHS = (
    os.path.join(ROOT, 'locale'),
)


# Third-party Libary Settings
##############################################################################

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
    'registration',
    'browserid',
]

# Accepted locales
PROD_LANGUAGES = ('de', 'en-US', 'es', 'fr',)

# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'base': (
            'browserid/persona-buttons.css',
            'css/sandstone/sandstone-resp.less',
            'css/one-and-done.less'
        ),
    },
    'js': {
        'base': (
            'js/libs/jquery-2.0.3.min.js',
            'https://login.persona.org/include.js',
            'browserid/browserid.js',
            'js/site.js',
        ),
    }
}

# Use staticfiles loaders for finding resources for minification.
JINGO_MINIFY_USE_STATIC = True

# Do not preprocess LESS files.
LESS_PREPROCESS = False

# Testing configuration.
NOSE_ARGS = ['--logging-clear-handlers', '--logging-filter=-factory,-south']

# Should robots.txt deny everything or disallow a calculated list of URLs we
# don't want to be crawled?  Default is false, disallow everything.
# Also see http://www.google.com/support/webmasters/bin/answer.py?answer=93710
ENGAGE_ROBOTS = False

# Always generate a CSRF token for anonymous users.
ANON_ALWAYS = True

# Tells the extract script what files to look for L10n in and what function
# handles the extraction. The Tower library expects this.
DOMAIN_METHODS['messages'] = [
    ('oneanddone/**.py',
        'tower.management.commands.extract.extract_tower_python'),
    ('oneanddone/**/templates/**.html',
        'tower.management.commands.extract.extract_tower_template'),
    ('templates/**.html',
        'tower.management.commands.extract.extract_tower_template'),
]

# Authentication settings.
LOGIN_URL = reverse_lazy('base.home')
LOGIN_REDIRECT_URL = reverse_lazy('base.home')
LOGIN_REDIRECT_URL_FAILURE = reverse_lazy('base.home')
LOGOUT_REDIRECT_URL = reverse_lazy('base.home')


# Project-specific Settings
##############################################################################

