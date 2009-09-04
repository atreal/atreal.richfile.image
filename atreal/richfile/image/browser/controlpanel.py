from zope.interface import Interface
from zope.component import adapts
from zope.interface import implements
from zope.schema import TextLine, Choice, List, Bool
from zope.formlib import form

from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

from atreal.richfile.image import RichFileImageMessageFactory as _
from atreal.richfile.image.interfaces import IImageable
from plone.app.controlpanel.form import ControlPanelForm
from atreal.richfile.qualifier.common import RFControlPanel


class IRichFileImageSchema(Interface):
    """ """
    
    rf_image_collapsed = Bool(
        title=_(u"label_rf_image_collapsed",
                default=u"Display collapsed ?"),
        description=_(u"help_rf_image_collapsed",
                      default=u"Do you want the plugin's display to be collapsed ?"
                     ),
        default=False)

    
class RichFileImageControlPanelAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(IRichFileImageSchema)

    rf_image_collapsed = ProxyFieldProperty(IRichFileImageSchema['rf_image_collapsed'])


    
class RichFileImageControlPanel(RFControlPanel):
    template = ZopeTwoPageTemplateFile('controlpanel.pt')
    form_fields = form.FormFields(IRichFileImageSchema)
    label = _("RichFileImage settings")
    description = _("RichFileImage settings for this site.")
    form_name = _("RichFileImage settings")
    plugin_iface = IImageable
    supported_ifaces = ('atreal.richfile.image.interfaces.IImage',)
    
