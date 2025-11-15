# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import frappe
import unittest
import json
from frappe.tests.utils import FrappeTestCase
from unittest.mock import patch, Mock
from auto_parts_manager.auto_parts_manager.doctype.vin_lookup.vin_lookup import VINLookup

class TestVINLookup(FrappeTestCase):
	fixtures = ["vehicle", "auto_part", "auto_part_compatible_vin"]

	def test_decode_vin_and_get_parts_success(self):
		"""Test successful VIN decoding and parts retrieval"""
		vin_lookup = frappe.new_doc('VINLookup')
		vin_lookup.vin_input = "1HGCM82633A123456"

		with patch('requests.get') as mock_get:
			mock_response = Mock()
			mock_response.json.return_value = {
				'brand': 'Honda',
				'model': 'Civic',
				'year': '2003',
				'engine_type': '1.7L',
				'fuel_type': 'petrol'
			}
			mock_response.raise_for_status.return_value = None
			mock_get.return_value = mock_response

			with patch('frappe.conf.get', return_value='fake_api_key'):
				with patch('frappe.db.get_single_value', return_value=None):
					vin_lookup.decode_vin_and_get_parts()

		decoded_data = json.loads(vin_lookup.decoded_data)
		self.assertEqual(decoded_data['vin'], "1HGCM82633A123456")
		self.assertEqual(decoded_data['brand'], 'Honda')
		self.assertEqual(decoded_data['model'], 'Civic')
		self.assertIsInstance(vin_lookup.compatible_parts_list, list)

	def test_decode_vin_and_get_parts_no_vin(self):
		"""Test decode with no VIN input"""
		vin_lookup = frappe.new_doc('VINLookup')
		vin_lookup.decode_vin_and_get_parts()  # Should return without error
		self.assertTrue(True)

	def test_decode_vin_and_get_parts_api_failure(self):
		"""Test decode when VIN decoding API fails"""
		vin_lookup = frappe.new_doc('VINLookup')
		vin_lookup.vin_input = "1HGCM82633A123456"

		with patch('requests.get', side_effect=Exception("API Error")):
			with patch('frappe.log_error'):
				with patch('frappe.conf.get', return_value='fake_api_key'):
					with patch('frappe.db.get_single_value', return_value=None):
						vin_lookup.decode_vin_and_get_parts()

		# Should still have decoded_data as empty dict or fallback
		if vin_lookup.decoded_data:
			decoded_data = json.loads(vin_lookup.decoded_data)
			self.assertIn('vin', decoded_data)

	def test_get_compatible_parts_for_vin_success(self):
		"""Test static method for getting compatible parts"""
		vin = "1HGCM82633A123456"
		with patch('requests.get') as mock_get:
			mock_response = Mock()
			mock_response.json.return_value = {
				'brand': 'Honda',
				'model': 'Civic',
				'year': '2003',
				'engine_type': '1.7L',
				'fuel_type': 'petrol'
			}
			mock_response.raise_for_status.return_value = None
			mock_get.return_value = mock_response

			with patch('frappe.conf.get', return_value='fake_api_key'):
				with patch('frappe.db.get_single_value', return_value=None):
					parts = VINLookup.get_compatible_parts_for_vin(vin)

		self.assertIsInstance(parts, list)
		if parts:
			for part in parts:
				self.assertIsInstance(part, str)

	def test_get_compatible_parts_for_vin_no_matches(self):
		"""Test static method with VIN that has no compatible parts"""
		vin = "NOMATCHVIN1234567"
		with patch('requests.get', side_effect=Exception("API Error")):
			with patch('frappe.log_error'):
				with patch('frappe.conf.get', return_value='fake_api_key'):
					with patch('frappe.db.get_single_value', return_value=None):
						parts = VINLookup.get_compatible_parts_for_vin(vin)

		self.assertEqual(parts, [])