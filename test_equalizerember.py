# test_equalizerember.py
"""
Tests for EqualizerEmber module.
"""

import unittest
from equalizerember import EqualizerEmber

class TestEqualizerEmber(unittest.TestCase):
    """Test cases for EqualizerEmber class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EqualizerEmber()
        self.assertIsInstance(instance, EqualizerEmber)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EqualizerEmber()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
