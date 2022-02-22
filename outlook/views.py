from dateutil import tz, parser
from outlook.auth_helper import get_sign_in_flow, get_token_from_code
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta

def home(request):
  context = initialize_context(request)

  return render(request, 'outlook/home.html', context)

def initialize_context(request):
  context = {}

  # Check for any errors in the session
  error = request.session.pop('flash_error', None)

  if error != None:
    context['errors'] = []
    context['errors'].append(error)

  # Check for user in the session
  context['user'] = request.session.get('user', {'is_authenticated': False})
  return context

def sign_in(request):
  # Get the sign-in flow
  flow = get_sign_in_flow()
  # Save the expected flow so we can use it in the callback
  try:
    request.session['auth_flow'] = flow
  except Exception as e:
    print(e)
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(flow['auth_uri'])

def callback(request):
  # Make the token request
  result = get_token_from_code(request)
  # Temporary! Save the response in an error so it's displayed
  request.session['flash_error'] = { 'message': 'Token retrieved', 'debug': format(result) }
  return HttpResponseRedirect(reverse('home'))