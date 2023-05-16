import os

from corsheaders.defaults import default_headers, default_methods
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = "DEBUG" True)
TEMPLATE_DEBUG = DEBUG

DEFAULT_FROM_EMAIL = "DEFAULT_FROM_EMAIL" "support@Bubbas.com")

CONTACT_NUMBER = "CONTACT_NUMBER" "850 009 9499")

PEEL_URL = "PEEL_URL" "http://Bubbas.com/")

# stackoverflow app
SOF_APP_ID = "SOFAPPID"
SOF_APP_SECRET = "SOFAPPSECRET"
SOF_APP_KEY = "SOFAPPKEY"

broker_api = "BROKER_API" "http://guest:guest@localhost:15672/api/")

# Enable debug logging

logging = "DEBUG"

GIT_APP_ID = "GITAPPID"
GIT_APP_SECRET = "GITAPPSECRET"

ALLOWED_HOSTS = ["*"]

# tw app
tw_oauth_token_secret = "twoauthtokensecret"
tw_oauth_token = "twoauthtokensecret"

TW_APP_KEY = "TWAPPKEY"
TW_APP_SECRET = "TWAPPSECRET"
OAUTH_TOKEN = "OAUTHTOKEN"
OAUTH_SECRET = "OAUTHSECRET"

PJ_TW_APP_KEY = "PJTWAPPKEY"
PJ_TW_APP_SECRET = "PJTWAPPSECRET"

# fb app
FB_APP_ID = "FACEBOOK_APP_ID"
FB_SECRET = "FACEBOOK_APP_SECRET"
FB_Bubbas_PAGEID = "FBBubbasPAGEID"

# google app
GOOGLE_CLIENT_ID = GOOGLE_OAUTH2_CLIENT_ID = "GOOGLE_CLIENT_ID"
GOOGLE_CLIENT_SECRET = GOOGLE_OAUTH2_CLIENT_SECRET = "GOOGLE_CLIENT_SECRET"
GOOGLE_LOGIN_HOST = "GOOGLE_LOGIN_HOST"

# ln app
LN_API_KEY = "LNAPIKEY"
LN_SECRET_KEY = "LNSECRETKEY"
LN_OAUTH_USER_TOKEN = "LNOAUTHUSERTOKEN"
LN_OAUTH_USER_SECRET = "LNOAUTHUSERSECRET"
LN_COMPANYID = "LNCOMPANYID"

# re-captcha
RECAPTCHA_PUBLIC_KEY = "RECAPTCHAPUBLICKEY"
RECAPTCHA_PRIVATE_KEY = "RECAPTCHAPRIVATEKEY"
RECAPTCHA_USE_SSL = False

# Make this unique, and don"t share it with anybody.
SECRET_KEY = '"SCRET_KEY")'

ADMINS = (
    # ("Your Name", "your_email@example.com"),
)

MANAGERS = ADMINS

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://dbmasteruser:smarty24@ls-50b9e3677c432aa3ffe9dbfac126276facaa8f38.cacqug8qj9tp.eu-west-3.rds.amazonaws.com:5432/postgres',
        conn_max_age=600)}

TIME_ZONE = "Asia/Calcutta"

LANGUAGE_CODE = "en-us"

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = False


# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "compressor.finders.CompressorFinder",
)

HTML_MINIFY = "HTML_MINIFY" False)

ROOT_URLCONF = "jobsp.urls"

# Python dotted path to the WSGI application used by Django"s runserver.
WSGI_APPLICATION = "jobsp.wsgi.application"

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.messages",
    "sorl.thumbnail",
    "compressor",
    "storages",
    "peeldb",
    # 'django_simple_forum',
    # "haystack",
    "dashboard",
    "search",
    "simple_pagination",
    "tellme",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    # "django_ses",
)

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # "hmin.middleware.MinMiddleware",
    # "hmin.middleware.MarkMiddleware",
    # "jobsp.middlewares.DetectMobileBrowser",
    "jobsp.middlewares.LowerCased",
]


CORS_ALLOWED_ORIGINS = ["http://localhost:4200", "http://127.0.0.1:4200"]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.Bubbas\.com$",
]
CORS_ALLOW_METHODS = list(default_methods)
CORS_ALLOW_HEADERS = list(default_headers)


AUTH_USER_MODEL = "peeldb.User"
LOGIN_URL = "/"

AUTHENTICATION_BACKENDS = (
    "social.auth_backend.PasswordlessAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR + "/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # "jobsp.context_processors.export_vars",
                "peeldb.context_processors.get_pj_icons",
            ],
        },
    },
]

AM_ACCESS_KEY = AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY"
AM_PASS_KEY = AWS_SECRET_ACCESS_KEY = "AWS_SECRET_KEY"
# AWS_SES_REGION_NAME = "AWS_SES_REGION_NAME"
# AWS_SES_REGION_ENDPOINT = "AWS_SES_REGION_ENDPOINT"
AWS_STORAGE_BUCKET_NAME = "AWS_STORAGE_BUCKET_NAME"


COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]
COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]
COMPRESS_REBUILD_TIMEOUT = 5400


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"
COMPRESS_OUTPUT_DIR = "CACHE"
COMPRESS_URL = STATIC_URL
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ("text/less", "lessc {infile} {outfile}"),
    ("text/x-sass", "sass {infile} {outfile}"),
    ("text/x-scss", "sass {infile} {outfile}"),
)

COMPRESS_OFFLINE_CONTEXT = {
    "STATIC_URL": "STATIC_URL",
}

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


# Haystack settings for Elasticsearch
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "peeldb.backends.ConfigurableElasticSearchEngine",
        "URL": "http://127.0.0.1:9200/",
        "INDEX_NAME": "job_haystack",
        "TIMEOUT": 60,
    },
}

# HAYSTACK_CONNECTIONS = {
#     "default": {
#         "ENGINE": "haystack.backends.elasticsearch7_backend.Elasticsearch7SearchEngine",
#         "URL": "http://127.0.0.1:9200/",
#         "INDEX_NAME": "haystack",
#     },
# }


HAYSTACK_SIGNAL_PROCESSOR = "haystack.signals.RealtimeSignalProcessor"
HAYSTACK_DEFAULT_OPERATOR = "OR"
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 1

SUPPORT_EMAILS = [
    "ashwin@micropyramid.com",
]


THUMBNAIL_COLORSPACE = None
THUMBNAIL_PRESERVE_FORMAT = False
THUMBNAIL_FORMAT = "PNG"
THUMBNAIL_CACHE_TIMEOUT = 3600 * 24 * 365 * 10

TIMEZONE = "Asia/Calcutta"
LOGO = "http://localhost:8000/logo.png"

# BULK_SMS_USERNAME = "BULKSMSUSERNAME"
# BULK_SMS_PASSWORD = "BULKSMSPASSWORD"
# BULK_SMS_FROM = "BULKSMSFROM"

MINIFIED_URL = "MINIFIED_URL"


THUMBNAIL_BACKEND = "jobsp.thumbnailname.SEOThumbnailBackend"
THUMBNAIL_DEBUG = True

THUMBNAIL_FORCE_OVERWRITE = True

# SMS_AUTH_KEY = "SMSAUTHKEY"


# AWS_ENABLED = "AWSENABLED"
# DISQUS_SHORTNAME = ""

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
#         "LOCATION": "127.0.0.1:11211",
#         "TIMEOUT": 48 * 60 * 60,
#         "OPTIONS": {"server_max_value_length": 1024 * 1024 * 2,},
#     }
# }

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.dummy.DummyCache",
#     }
# }

# CACHE_BACKEND = "CACHE_BACKEND" "memcached://127.0.0.1:11211/")

FB_ACCESS_TOKEN = "FBACCESSTOKEN"
FB_PAGE_ACCESS_TOKEN = "FBPAGEACCESSTOKEN"
FB_GROUP_ACCESS_TOKEN = "FBGROUPACCESSTOKEN"
FB_ALL_GROUPS_TOKEN = "FBALLGROUPSTOKEN"
FB_DEL_ACCESS_TOKEN = "FBDELACCESSTOKEN"
REC_FB_ACCESS_TOKEN = "RECFBACCESSTOKEN"

URLS = [
    "http://stage.Bubbas.com/",
    "http://stage.Bubbas.com/fresher-jobs/",
    "http://stage.Bubbas.com/jobs/",
    "http://stage.Bubbas.com/companies/",
]

DAILY_REPORT_USERS = [
    "kamal.seo@gmail.com",
    "varun@micropyramid.com",
    "ashwin@micropyramid.com",
]
# MIDDLEWARE_CLASSES = MIDDLEWARE

if "ENV_TYPE" == "DEV":
    INSTALLED_APPS = INSTALLED_APPS + (
        # "debug_toolbar",
        # "template_profiler_panel",
        "behave_django",
    )

    # MIDDLEWARE = [
    #     "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ] + MIDDLEWARE

    INTERNAL_IPS = ("127.0.0.1",)

    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.versions.VersionsPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.settings.SettingsPanel",
        "debug_toolbar.panels.headers.HeadersPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.logging.LoggingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
        "template_profiler_panel.panels.template.TemplateProfilerPanel",
    ]

    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    TEST_RUNNER = "django_behave.runner.DjangoBehaveTestSuiteRunner"

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}
        },
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s "
                "%(process)d %(thread)d %(message)s"
            },
            "standard": {
                "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                #'datefmt' : "%d/%b/%Y %H:%M:%S"
            },
        },
        "handlers": {
            "mail_admins": {
                "level": "ERROR",
                "filters": ["require_debug_false"],
                "class": "django.utils.log.AdminEmailHandler",
            },
            # 'file_log': {
            #     'level':'DEBUG',
            #     'class':'logging.handlers.TimedRotatingFileHandler',
            #     'filename': BASE_DIR + '/logs/django_dev.log',
            #     'when': 'S', # this specifies the interval
            #     'interval': 5, # defaults to 1, only necessary for other values
            #     # 'maxBytes': 1024*1024*5,# 5 MB
            #     'backupCount': 5,
            #     'formatter':'standard',
            # }
        },
        "loggers": {
            "django.request": {
                "handlers": ["mail_admins"],
                "level": "ERROR",
                "propagate": True,
            },
            # 'request-logging': {
            #     'level': 'DEBUG',
            #     'handlers': ['file_log'],
            #     'propagate': False,
            # },
        },
    }

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        # 'rest_framework.authentication.SessionAuthentication',
    ]
}

REST_USE_JWT = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# EMAIL_BACKEND = "django_ses.SESBackend"

MP_CELERY_MONITOR_KEY = "MP_CELERY_MONITOR_KEY"
CELERY_MONITOR_URL = "CELERY_MONITOR_URL"
