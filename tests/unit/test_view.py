#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import os

from methodview import MethodView
from mock import Mock
from unittest import TestCase

os.environ['DJANGO_SETTINGS_MODULE'] = 'methodview.view'


def create_request(method):
    request = Mock(META={}, POST={}, GET={}, method=method)
    return request


class BasicMethodTest(TestCase):

    class TestView(MethodView):
        def get(self, request):
            return 'GOT'

        def post(self, request):
            return 'POSTED'

    def test(self):
        view = BasicMethodTest.TestView()

        request = create_request('GET')
        res = view(request)
        self.assertEqual('GOT', res)

        request = create_request('POST')
        res = view(request)
        self.assertEqual('POSTED', res)


class AcceptHeaderTest(TestCase):

    class TestView(MethodView):
        def get(self, request):
            return 'GOT DEFAULT'

        def get_text_html(self, request):
            return 'GOT TEXT HTML'

        def get_application_json(self, request):
            return 'GOT APPLICATION JSON'

    def test(self):
        view = AcceptHeaderTest.TestView()

        request = create_request('GET')
        res = view(request)
        self.assertEqual('GOT DEFAULT', res)

        request.META['HTTP_ACCEPT'] = 'text/html'
        res = view(request)
        self.assertEqual('GOT TEXT HTML', res)

        request.META['HTTP_ACCEPT'] = 'application/json'
        res = view(request)
        self.assertEqual('GOT APPLICATION JSON', res)
