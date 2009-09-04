from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from atreal.richfile.qualifier.browser.viewlets import RichfileViewlet
from atreal.richfile.image.interfaces import IImage
from atreal.richfile.image.interfaces import IImageable
from atreal.richfile.image.browser.controlpanel import IRichFileImageSchema
from atreal.richfile.image import RichFileImageMessageFactory as _

class ImageViewlet(RichfileViewlet):
    
    marker_interface = IImage
    plugin_interface = IImageable
    plugin_id = 'image'
    plugin_title = 'Image preview'
    controlpanel_interface = IRichFileImageSchema
    
        
    index = ViewPageTemplateFile("viewlet.pt")
