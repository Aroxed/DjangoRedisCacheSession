import datetime
import time

from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(10)  # sec
def get_long_running_result(request):
    time.sleep(3)
    return HttpResponse("Current time is %s" % datetime.datetime.now())
