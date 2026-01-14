# test_pixelden.py
"""
Tests for PixelDen module.
"""

import unittest
from pixelden import PixelDen

class TestPixelDen(unittest.TestCase):
    """Test cases for PixelDen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PixelDen()
        self.assertIsInstance(instance, PixelDen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PixelDen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
