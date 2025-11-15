# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import frappe
import unittest
from frappe.tests.utils import FrappeTestCase
from unittest.mock import patch, Mock
from auto_parts_manager.auto_parts_manager.doctype.vehicle.vehicle import Vehicle

class TestVehicle(FrappeTestCase):
	fixtures = ["vehicle"]

	def test_validate_vin_success(self):
		"""Test valid VIN validation"""
		vehicle = frappe.new_doc('Vehicle')
		vehicle.vin = "1HGCM82633A123456"  # Valid sample VIN
		try:
			vehicle.validate_vin()
			self.assertTrue(True)  # No exception raised
		except Exception:
			self.fail("Valid VIN should not raise exception")

	def test_validate_vin_invalid_length(self):
		"""Test invalid VIN length"""
		vehicle = frappe.new_doc('Vehicle')
		vehicle.vin = "12345"  # Too short
		with self.assertRaises(frappe.ValidationError) as cm:
			vehicle.validate_vin()
		self.assertIn("Invalid VIN format", str(cm.exception))

	def test_validate_vin_invalid_characters(self):
		"""Test VIN with invalid characters"""
		vehicle = frappe.new_doc('Vehicle')
		vehicle.vin = "1HGCM82633A12345O"  # Contains 'O' which is invalid
		with self.assertRaises(frappe.ValidationError) as cm:
			vehicle.validate_vin()
		self.assertIn("Invalid VIN format", str(cm.exception))

	@patch('requests.get')
	def test_decode_vin_success(self, mock_get):
		"""Test successful VIN decoding"""
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

		vehicle = frappe.new_doc('Vehicle')
		vehicle.vin = "1HGCM82633A123456"
		with patch('frappe.conf.get', return_value='fake_api_key'):
			with patch('frappe.db.get_single_value', return_value=None):
				vehicle.decode_vin()

		self.assertEqual(vehicle.brand, 'Honda')
		self.assertEqual(vehicle.model, 'Civic')
		self.assertEqual(vehicle.year, '2003')
		self.assertEqual(vehicle.engine_type, '1.7L')
		self.assertEqual(vehicle.fuel_type, 'Essence')

	@patch('requests.get')
	def test_decode_vin_api_failure(self, mock_get):
		"""Test VIN decoding when API fails"""
		mock_get.side_effect = Exception("API Error")

		vehicle = frappe.new_doc('Vehicle')
		vehicle.vin = "1HGCM82633A123456"
		with patch('frappe.conf.get', return_value='fake_api_key'):
			with patch('frappe.db.get_single_value', return_value=None):
				with patch('frappe.log_error'):
					vehicle.decode_vin()

		# Should fallback to validation
		self.assertEqual(vehicle.brand, None)  # Not set

	def test_decode_vin_no_vin(self):
		"""Test decode_vin with no VIN"""
		vehicle = frappe.new_doc('Vehicle')
		vehicle.decode_vin()  # Should return without doing anything
		self.assertTrue(True)