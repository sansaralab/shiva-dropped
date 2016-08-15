from time import time
from urllib.parse import urlparse
from django.http import JsonResponse
from django.shortcuts import render
from .services import track_person_visit, attach_contact_to_person, send_person_event, attach_data_to_person


def success(uid):
    resp = JsonResponse({
        'ok': True
    }, status=200)
    resp.set_cookie('uid', uid, time() + 315360000, httponly=True)
    return resp


def error():
    return JsonResponse({
        'ok': False
    }, status=403)


def tracker_serve(req):
    return render(req, 'tracker/tracker.min.js', {
        'server': req.scheme + '://' + req.get_host()
    }, content_type="application/x-javascript")


def track(req):
    """
    Tracks user visit

    :param req:
    :return:
    """
    page = req.GET.get('p', None)
    if page is None:
        return error()

    referer = req.META.get("HTTP_REFERER", None)
    parsed_uri = urlparse(referer)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    if domain:
        uid = req.COOKIES.get('uid', None)
        user_agent = req.META.get("HTTP_USER_AGENT", None)
        user_ip = req.META.get("REMOTE_ADDR", None)
        person = track_person_visit(uid, page, user_agent, user_ip)
        return success(person.uid)
    else:
        return error()


def attach_contact(req):
    contact_type = req.GET.get('t', None)
    contact_value = req.GET.get('v', None)

    if contact_type is None or contact_value is None:
        return error()

    referer = req.META.get("HTTP_REFERER", None)
    parsed_uri = urlparse(referer)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    if domain:
        uid = req.COOKIES.get('uid', None)
        response = attach_contact_to_person(uid, contact_type, contact_value)
        return success(response.person.uid)
    else:
        return error()


def attach_data(req):
    data_type = req.GET.get('t', None)
    data_value = req.GET.get('v', None)

    if data_type is None or data_value is None:
        return error()

    referer = req.META.get("HTTP_REFERER", None)
    parsed_uri = urlparse(referer)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    if domain:
        uid = req.COOKIES.get('uid', None)
        response = attach_data_to_person(uid, data_type, data_value)
        return success(response.person.uid)
    else:
        return error()


def send_event(req):
    event_type = req.GET.get('t', None)
    event_value = req.GET.get('v', '')

    if event_type is None:
        return error()

    referer = req.META.get("HTTP_REFERER", None)
    parsed_uri = urlparse(referer)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    if domain:
        uid = req.COOKIES.get('uid', None)
        response = send_person_event(uid, event_type, event_value)
        return success(response.person.uid)
    else:
        return error()
