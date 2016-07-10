from time import time
from urllib.parse import urlparse
from django.http import JsonResponse
from django.shortcuts import render
from .services import track_person_visit, attach_info_to_person, send_person_event


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
    return render(req, 'tracker/tracker.js', {
        'server': req.scheme + '://' + req.get_host()
    }, content_type="application/x-javascript")


def track(req):
    """
    Tracks user visit

    FIXME: Looks like mega trash.

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


def attach_info(req):
    info_type = req.GET.get('t', None)
    info_value = req.GET.get('v', None)

    if info_type is None or info_value is None:
        return error()

    referer = req.META.get("HTTP_REFERER", None)
    parsed_uri = urlparse(referer)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    if domain:
        uid = req.COOKIES.get('uid', None)
        person = attach_info_to_person(uid, info_type, info_value)
        return success(person.uid)
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
        person = send_person_event(uid, event_type, event_value)
        return success(person.uid)
    else:
        return error()
