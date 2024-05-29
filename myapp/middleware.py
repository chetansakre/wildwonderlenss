# middleware.py
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import login,logout

from django.contrib import auth
from django.conf import settings

# class AutoLogoutMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             if timezone.now() - request.user.last_login > timedelta(minutes=1):
#                 logout(request)  # Logout if 5 or more days since last login
#         response = self.get_response(request)
#         return response


# class AutoLogout:
#   def process_request(self, request):
#     if not request.user.is_authenticated() :
#       #Can't log out if not logged in
#       return

#     try:
#       if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
#         auth.logout(request)
#         del request.session['last_touch']
#         return
#     except KeyError:
#       pass

#     request.session['last_touch'] = datetime.now()





from .models import Visitor

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the session ID
        session_id = request.session.session_key

        # Get the IP address
        ip_address = request.META.get('REMOTE_ADDR')

        # Check if a session exists
        if session_id:
            # Check if the session exists in the database
            if not Visitor.objects.filter(session_id=session_id).exists():
                # If the session doesn't exist, create a new record
                Visitor.objects.create(session_id=session_id)
        elif ip_address:
            # Check if the IP address exists in the database
            if not Visitor.objects.filter(ip_address=ip_address).exists():
                # If the IP address doesn't exist, create a new record
                Visitor.objects.create(ip_address=ip_address)

        response = self.get_response(request)
        return response
