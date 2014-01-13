from ftw.builder import Builder
from ftw.builder import create
from ftw.slider.testing import SLIDER_FUNCTIONAL_TESTING
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles
from unittest2 import TestCase
from ftw.testbrowser import browsing


class TestSliderCreation(TestCase):

    layer = SLIDER_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Contributor', 'Manager'])
        login(self.portal, TEST_USER_NAME)

        slider_container = create(Builder('slider container'))
        self.slider_pane = create(Builder('slider pane')
                             .within(slider_container)
                             .with_dummy_content())
        self.subfolder = create(Builder('folder'))


    @browsing
    def test_slider_appears(self, browser):
        browser.login().open(view='folder_contents')
        self.assertEquals(1, len(browser.css('#slider-panes')))

    @browsing
    def test_slider_doesnt_appear_in_subfolder(self, browser):
        browser.login().open(self.subfolder, view='folder_contents')
        self.assertEquals(0, len(browser.css('#slider-panes')))

    @browsing
    def test_slider_appears_in_subfolder_if_checked(self, browser):
        self.slider_pane.setShow_in_subcontent = True
        browser.login().open(self.subfolder, view='folder_contents')
        self.assertEquals(1, len(browser.css('#slider-panes')))
