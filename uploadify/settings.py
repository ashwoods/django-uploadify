from django.conf import settings

# Upload path that files are sent to
UPLOADIFY_UPLOAD_PATH = settings.UPLOADIFY_PATH = getattr(settings, 'UPLOADIFY_PATH', '%s%s' % (settings.MEDIA_URL, 'js/uploadify/'))

# Uploadify root folder path, relative to MEDIA_ROOT
UPLOADIFY_PATH = settings.UPLOADIFY_PATH = getattr(settings, 'UPLOADIFY_UPLOAD_PATH', '%s%s' % (settings.STATIC_ROOT, 'uploads/'))

# Include the JS Script calls in the templatetag
UPLOADIFY_INCLUDE_JS = settings.UPLOADIFY_INCLUDE_JS = getattr(settings,  'UPLOADIFY_INCLUDE_JS', True)
