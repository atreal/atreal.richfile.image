from zope.i18nmessageid import MessageFactory
RichFileImageMessageFactory = MessageFactory('atreal.richfile.image')

from atreal.richfile.image.interfaces import IImage

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    try:
        from atreal.richfile.qualifier.registry import registerRFPlugin
    except:
        return
    
    supported_mimetypes = [
        'image/png',
        'image/gif',
        'image/jpeg',
        ]
    
    registerRFPlugin(IImage, supported_mimetypes)
    
