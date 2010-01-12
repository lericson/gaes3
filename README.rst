To access `Amazon AWS S3`_ from `Google App Engine`_, you not only need an S3
interface like simples3_, but you'll also need a ported version of that
interface that works with Google's own ``urlfetch`` extension API.

``gaes3`` is exactly that, and is layered on top of simples3_.

Usage is exactly like simples3_, but with a different class::

    >>> from gaes3 import AppEngineS3Bucket
    >>> bucket = AppEngineS3Bucket("foo", access_key, secret_key)
    >>> bucket.info("foo")["mimetype"]
    'text/plain'

.. _Amazon AWS S3: http://aws.amazon.com/s3/
.. _Google App Engine: http://appengine.google.com/
.. _simples3: http://sendapatch.se/projects/simples3/
