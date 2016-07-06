from time import time
from urllib.parse import urlparse
from django.http import JsonResponse
from django.shortcuts import render
from .services import track_person_visit


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
        new_uid = track_person_visit(uid, page, user_agent, user_ip)
        return success(new_uid)
    else:
        return error()
