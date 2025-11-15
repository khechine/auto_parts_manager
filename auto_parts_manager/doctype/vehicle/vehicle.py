# -*- coding: utf-8 -*-
# Copyright (c) 2023, Your Company and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import re
import requests
import time

class Vehicle(Document):
    def validate(self):
        self.validate_vin()

    def validate_vin(self):
        if self.vin:
            if not re.match(r'^[A-HJ-NPR-Z0-9]{17}$', self.vin):
                frappe.throw(_("Invalid VIN format. VIN must be 17 characters long and contain only valid characters (no I, O, Q)."))

    def decode_vin(self):
        """Decode VIN using VINDecoder.eu API"""
        if not self.vin:
            return

        api_key = frappe.conf.get('vin_decoder_api_key') or frappe.db.get_single_value('Auto Parts Manager Settings', 'vin_decoder_api_key')
        if not api_key:
            frappe.log_error("VIN Decoder API key not configured", "VIN Decoding Error")
            self.validate_vin()  # Fallback to basic validation
            return

        max_retries = 3
        for attempt in range(max_retries):
            try:
                url = f"https://vindecoder.eu/api/{self.vin}?key={api_key}"
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()

                # Populate fields based on API response
                if 'brand' in data:
                    self.brand = data['brand']
                if 'model' in data:
                    self.model = data['model']
                if 'year' in data:
                    self.year = data['year']
                if 'engine_type' in data:
                    self.engine_type = data['engine_type']
                if 'fuel_type' in data:
                    # Map API fuel type to select options
                    fuel_mapping = {
                        'diesel': 'Diesel',
                        'petrol': 'Essence',
                        'electric': 'Électrique',
                        'hybrid': 'Hybride'
                    }
                    self.fuel_type = fuel_mapping.get(data['fuel_type'].lower(), data['fuel_type'])

                frappe.msgprint(_("VIN decoded successfully."))
                return

            except requests.exceptions.RequestException as e:
                frappe.log_error(f"VIN Decoding API call failed (attempt {attempt + 1}): {str(e)}", "VIN Decoding Error")
                if attempt < max_retries - 1:
                    time.sleep(1)  # Wait 1 second before retry
            except Exception as e:
                frappe.log_error(f"Error processing VIN decoding response: {str(e)}", "VIN Decoding Error")
                break

        # If all retries failed, fallback to basic validation
        frappe.msgprint(_("VIN decoding failed. Falling back to basic validation."))
        self.validate_vin()
        # Example test with sample VIN (commented out for production)
        # self.vin = "1HGCM82633A123456"  # Sample VIN for testing