from django.conf import settings


def site(request):
    return {setting: getattr(settings, setting, None) for setting in [
        'SITE_URL', 'LANGUAGES', 'DEBUG', 'TITLE', 'LOGO_PATH',
        'CONTACT_SUBREDDIT', 'CONTACT_TWITTER', 'CONTACT_EMAIL'
    ]}