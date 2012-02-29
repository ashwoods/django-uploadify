from django.conf import settings

# Upload PATH that files are sent to
UPLOADIFY_UPLOAD_PATH = settings.UPLOADIFY_UPLOAD_PATH = getattr(settings, 'UPLOADIFY_UPLOAD_PATH', '%s%s' % (settings.MEDIA_URL, 'uploads/'))

# Uploadify STATIC MEDIA default PATH
UPLOADIFY_DEFAULT_PATH = settings.UPLOADIFY_DEFAULT_PATH  = getattr(settings, 'UPLOADIFY_DEFAULT_PATH', '%s%s' % (settings.STATIC_ROOT, 'uploadify/'))

# Default PATH to the specific files. Only needed if you have to override (i.e. when using CDN)
UPLOADIFY_PATH_JS  = settings.UPLOADIFY_PATH_JS  = getattr(settings, 'UPLOADIFY_PATH_JS', '%s%s' % (UPLOADIFY_DEFAULT_PATH, 'jquery.uploadify.v2.1.4.min.js'))
UPLOADIFY_PATH_SWF = settings.UPLOADIFY_PATH_SWF = getattr(settings, 'UPLOADIFY_PATH_SWF' '%s%s' % (UPLOADIFY_DEFAULT_PATH, 'uploadify.swf'))


# Include the JS Script calls in the templatetag, set to False if you want to include your own tags, i.e. for use with django-compressor
UPLOADIFY_INCLUDE_JS = settings.UPLOADIFY_INCLUDE_JS = getattr(settings,  'UPLOADIFY_INCLUDE_JS', True)
