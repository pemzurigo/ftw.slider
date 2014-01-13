from Products.CMFCore.utils import getToolByName
from ftw.slider.interfaces import SLIDER_VIEW
from plone.app.layout.viewlets import ViewletBase


class SliderViewlet(ViewletBase):

    def render(self):
        containers = self.context.getFolderContents(
            contentFilter={'portal_type': 'ftw.slider.Container'},
            full_objects=True)

#        import pdb; pdb.set_trace()

        if len(containers) == 0:
            # also check for sliders which will be shown in subcontent
            path = filter(None, self.context.getPhysicalPath())
            paths = []
            for position in range(1, len(path)+1):
                paths.append('/'.join(path[:position]))
            catalog = getToolByName(self.context, 'portal_catalog')
            # import pdb; pdb.set_trace()

            brains = catalog(path=dict(query=paths, depth=1),
                             show_in_subcontent=True,
                             portal_type='ftw.slider.Container')
            if len(brains):
                containers = [brains[0].getObject()]

        self.container = len(containers) > 0 and containers[0] or None
        if self.container:
            view = self.container.restrictedTraverse(SLIDER_VIEW, None)
            if view:
                return view()
        return ''
