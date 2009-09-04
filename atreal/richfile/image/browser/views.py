from zope.interface import implements

from atreal.richfile.image.interfaces import IImageable

from atreal.richfile.qualifier.common import RFView
from atreal.richfile.qualifier.interfaces import IRFView
from atreal.richfile.image import RichFileImageMessageFactory as _

class RFImageView(RFView):
    
    plugin_interface = IImageable
    kss_id = 'image'
    viewlet_name = 'atreal.richfile.image.viewlet'
    update_message = _('The image preview has been updated.')
    active_message = _('Image preview activated.')
    unactive_message = _('Image preview un-activated.') 
    

