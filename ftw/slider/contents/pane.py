from ftw.slider import _
from ftw.slider.interfaces import IPane
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.directives import form
from plone.directives.form import Schema
from plone.formwidget.contenttree import ContentTreeFieldWidget
from plone.formwidget.contenttree import PathSourceBinder
from plone.namedfile.field import NamedImage
from zope import schema
from zope.interface import implements


class IPaneSchema(Schema):
    text = RichText(
        title=_(u'label_text', default=u'Text'),
        description=_(u'help_text', default=u''),
        required=False,
        )
    image = NamedImage(
        title=_(u'label_image', default='Image'),
        required=True,
        )
    form.widget(link=ContentTreeFieldWidget)
    link = schema.Choice (
        title=_(u'label_link', default=u'Link'),
        description=_(u'help_link', default=u''),
        required=False,
        source=PathSourceBinder()
        )
    show_in_subcontent = schema.Bool(
        title=_(u'label_show_in_subcontent', default=u'Show in subcontent'),
        description=_(u'help_show_in_subcontent', default=u''),
        default=False
    )


class Pane(Container):
    implements(IPane)
