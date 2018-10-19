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
Class for resampling a raster grid to match that of another.
"""

def run():
    setup(name="resampleGDAL",
          version="0.1",
          description="Class for resampling a raster grid to match that of another.",
          author="Emily Pease",
          packages=["resampleGDAL"],
          author_email = 'emilypease@utexas.edu'
          )
if __name__ == "__main__":
    run()