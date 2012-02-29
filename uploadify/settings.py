from django.conf import settings

# Upload PATH that files are sent to
UPLOADIFY_UPLOAD_PATH = settings.UPLOADIFY_UPLOAD_PATH = getattr(settings, 'UPLOADIFY_UPLOAD_PATH', '%s%s' % (settings.MEDIA_URL, 'uploads/'))

# Uploadify STATIC MEDIA default PATH
UPLOADIFY_PATH = settings.UPLOADIFY_PATH  = getattr(settings, 'UPLOADIFY_PATH', '%s%s' % (settings.STATIC_ROOT, 'uploadify/'))

# Include the JS Script calls in the templatetag, set to False if you want to include your own tags, i.e. for use with django-compressor
UPLOADIFY_INCLUDE_JS = settings.UPLOADIFY_INCLUDE_JS = getattr(settings,  'UPLOADIFY_INCLUDE_JS', True)
