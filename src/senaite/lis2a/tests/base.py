# -*- coding: utf-8 -*-

import transaction
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.testing import zope
from senaite.core.tests.base import BaseTestCase
from senaite.core.tests.layers import BaseLayer


class SimpleTestLayer(BaseLayer):

    def setUpZope(self, app, configurationContext):
        super(SimpleTestLayer, self).setUpZope(app, configurationContext)

        # Load ZCML
        import plone.jsonapi.core
        import senaite.jsonapi
        import senaite.lis2a
        self.loadZCML(package=plone.jsonapi.core)
        self.loadZCML(package=senaite.jsonapi)
        self.loadZCML(package=senaite.lis2a)

        # Install product and call its initialize() function
        zope.installProduct(app, "plone.jsonapi.core")
        zope.installProduct(app, "senaite.jsonapi")
        zope.installProduct(app, "senaite.lis2a")

    def setUpPloneSite(self, portal):
        super(SimpleTestLayer, self).setUpPloneSite(portal)
        applyProfile(portal, "senaite.lis2a:default")
        transaction.commit()


SIMPLE_TEST_LAYER_FIXTURE = SimpleTestLayer()
SIMPLE_TESTING = FunctionalTesting(
    bases=(SIMPLE_TEST_LAYER_FIXTURE, ),
    name="senaite.lis2a:SimpleTesting"
)


class SimpleTestCase(BaseTestCase):
    """Use for test cases which do not rely on demo data
    """
    layer = SIMPLE_TESTING
