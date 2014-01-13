from ftw.builder.dexterity import DexterityBuilder
from ftw.builder import builder_registry
from plone.namedfile.file import NamedBlobImage


class SliderContainerBuilder(DexterityBuilder):
    portal_type = 'ftw.slider.Container'

builder_registry.register('slider container', SliderContainerBuilder)



class SliderPaneBuilder(DexterityBuilder):
    portal_type = 'ftw.slider.Pane'

    def with_dummy_content(self):
        self.arguments["image"] = NamedBlobImage(data='data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',
                                                filename=u'test_image.gif')
        return self

builder_registry.register('slider pane', SliderPaneBuilder)
