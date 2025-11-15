# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import frappe
import unittest
from frappe.tests.utils import FrappeTestCase
from auto_parts_manager.auto_parts_manager.doctype.auto_part.auto_part import AutoPart

class TestAutoPart(FrappeTestCase):
	fixtures = ["auto_part", "auto_part_compatible_vin"]

	def test_get_compatible_parts_success(self):
		"""Test getting compatible parts for a valid VIN"""
		# Assuming fixtures have data, test with a VIN that has compatible parts
		vin = "1HGCM82633A123456"  # Sample VIN
		parts = AutoPart.get_compatible_parts(vin)
		self.assertIsInstance(parts, list)
		# Check structure if parts exist
		if parts:
			for part in parts:
				self.assertIn('name', part)
				self.assertIn('part_code', part)
				self.assertIn('oem_reference', part)

	def test_get_compatible_parts_no_vin(self):
		"""Test getting compatible parts with empty VIN"""
		parts = AutoPart.get_compatible_parts("")
		self.assertEqual(parts, [])

	def test_get_compatible_parts_invalid_vin(self):
		"""Test getting compatible parts with VIN that has no matches"""
		vin = "INVALIDVIN1234567"
		parts = AutoPart.get_compatible_parts(vin)
		self.assertEqual(parts, [])

	def test_get_compatible_parts_none_vin(self):
		"""Test getting compatible parts with None VIN"""
		parts = AutoPart.get_compatible_parts(None)
		self.assertEqual(parts, [])

	def test_get_compatible_parts_sql_structure(self):
		"""Test that the SQL query returns expected columns"""
		vin = "1HGCM82633A123456"
		parts = AutoPart.get_compatible_parts(vin)
		if parts:
			expected_keys = {'name', 'part_code', 'oem_reference', 'purchase_price', 'sale_price', 'stock_qty'}
			for part in parts:
				self.assertTrue(set(part.keys()).issubset(expected_keys))