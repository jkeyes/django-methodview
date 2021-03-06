"""Test for media range."""
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from methodview.media_range import MediaRange
from unittest import TestCase


class MediaRangeTest(TestCase):
    """Test media range parsing."""

    def test_any_media(self):
        """Test for any media accepted."""
        media_range = MediaRange("*/*")
        self.assertEqual(media_range.content_type, "*/*")
        self.assertTrue(media_range.any_media)
        self.assertTrue(media_range.any_subtype)

    def test_any_subtype(self):
        """Test for any subtype accepted."""
        media_range = MediaRange("image/*")
        self.assertEqual(media_range.content_type, "image/*")
        self.assertFalse(media_range.any_media)
        self.assertTrue(media_range.any_subtype)

    def test_png(self):
        """Test for specific content type."""
        media_range = MediaRange("image/png")
        self.assertEqual(media_range.content_type, "image/png")
        self.assertEqual(media_range.mtype, "image")
        self.assertEqual(media_range.subtype, "png")
        self.assertFalse(media_range.any_media)
        self.assertFalse(media_range.any_subtype)

    def test_invalid_asterix(self):
        """Test invalid setitng - *."""
        media_range = MediaRange("*")
        self.assertEqual(media_range.content_type, "*/*")
        self.assertTrue(media_range.any_media)
        self.assertTrue(media_range.any_subtype)

    def test_invalid_media(self):
        """Test an invalud setting - 'image'."""
        media_range = MediaRange("image")
        self.assertEqual(media_range.content_type, "image/*")
        self.assertEqual(media_range.mtype, "image")
        self.assertEqual(media_range.subtype, "*")
        self.assertFalse(media_range.any_media)
        self.assertTrue(media_range.any_subtype)
