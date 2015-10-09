#coding:utf-8
import time 
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from app.autonumber.config import CONFIG
from app.autonumber import models

class SessionExpiredMiddleware:
    sessiontime = 0

    @staticmethod
    def process_request(session,):
        last_activity = session.get('last_activity',0)
        now = time.time()

        if (now - last_activity) > CONFIG['sessiontime']:
            return True

        session['last_activity'] = now
        SessionExpiredMiddleware.sessiontime = CONFIG['sessiontime']
        session.set_expiry(SessionExpiredMiddleware.sessiontime)
        return False

    @staticmethod
    def set_expiry(session):
        session['last_activity'] = time.time()
        SessionExpiredMiddleware.sessiontime = CONFIG['sessiontime']
        session.set_expiry(CONFIG['sessiontime'])

class GetCaseSerialNumber:
    @staticmethod
    def get(type = 0):
        year = time.strftime('%Y',time.localtime(time.time()))
        cnt = models.Case.objects.filter(createdate__year=int(year)).count() or 0
        retstr = CONFIG['documenttype'][type][1] % (year, cnt+1)
        return retstr
        