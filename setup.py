import sys
from distutils.core import setup
import codecs
try:
	codecs.lookup('mbcs')
except LookupError:
	ascii = codecs.lookup('ascii')
	func = lambda name, enc = ascii: {True: enc}.get(name=='mbcs')
	codecs.register(func)

DESCRIPTION = """\
Classes for resampling raster grids.
"""

def run():
    setup(name="ResampleRaster",
          version="0.1",
          description="Classes for resampling raster grids",
          author="Emily Pease",
          packages=["resampleraster"],
          author_email = 'emilypease@utexas.edu'
          )
if __name__ == "__main__":
    run()
