import sys

from django.conf import settings
from django.views.debug import technical_500_response


class UserBasedExceptionMiddleware(object):
    """Taken from http://ericholscher.com/blog/2008/nov/15/debugging-django-production-environments/
    this provides a way of making debugging information available to superusers (or users from
    approved IP addresses) while giving everyone else the standard 500 page."""
    def process_exception(self, request, exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            return technical_500_response(request, *sys.exc_info())
