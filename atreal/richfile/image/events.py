from zope.interface.interfaces import IInterface
from zope.component import queryUtility

from atreal.richfile.image.interfaces import IImageable


def is_richfileimage_installed():
    """
    """
    return queryUtility(IInterface, name=u'atreal.richfile.image.IRichFileImageSite', default=False)


def buildAndStoreImage(obj, event):
    """
    """
    if not is_richfileimage_installed():
        return
    print "atreal.richfile.image: build and store image for %s" % ('/'.join(obj.getPhysicalPath()),)
    IImageable(obj).process()


def cleanImageData(obj, event):
    """
    """
    if not is_richfileimage_installed():
        return
    print "atreal.richfile.image: clean data for %s" % ('/'.join(obj.getPhysicalPath()),)
    IImageable(obj).cleanUp()
