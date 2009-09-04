from zope.interface import implements

from zope.annotation.interfaces import IAnnotations

from atreal.richfile.image.interfaces import IImageable
from BTrees.OOBTree import OOBTree

import PIL.Image
from cStringIO import StringIO

from atreal.richfile.qualifier.common import RFPlugin

class ToImageableObject(RFPlugin):
    """
    """
    implements(IImageable)


    def process(self):
        """
        """
        print "atreal.richfile.image: processing..."
        self.setSubObject ('preview', self._scale (self.context.data, 400, 400))
        self.setSubObject ('thumb', self._scale (self.context.data, 128, 128))
        print "atreal.richfile.image: built and stored!"
  
    
    def _scale(self, data, w, h, default_format = 'PNG'):
        """ scale image """
        size = int(w), int(h)
        original_file=StringIO(data)
        image = PIL.Image.open(original_file)
        original_mode = image.mode
        if original_mode == '1':
            image = image.convert('L')
        elif original_mode == 'P':
            image = image.convert('RGBA')
        image.thumbnail(size, PIL.Image.ANTIALIAS)
        format = image.format and image.format or default_format
        if original_mode == 'P' and format == 'GIF':
            image = image.convert('P')
        thumbnail_file = StringIO()
        image.save(thumbnail_file, format, quality=88)
        thumbnail_file.seek(0)
        return thumbnail_file.read()
