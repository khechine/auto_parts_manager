# -*- coding: utf-8 -*-
# Copyright (c) 2023, Your Company and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
import json

class VINLookup(Document):
    def before_save(self):
        self.decode_vin_and_get_parts()

    def decode_vin_and_get_parts(self):
        if not self.vin_input:
            return

        # Decode VIN using Vehicle.decode_vin method
        vehicle = frappe.new_doc('Vehicle')
        vehicle.vin = self.vin_input
        vehicle.decode_vin()

        # Store decoded data as JSON
        decoded_info = {
            "vin": vehicle.vin,
            "brand": vehicle.brand,
            "model": vehicle.model,
            "year": vehicle.year,
            "engine_type": vehicle.engine_type,
            "fuel_type": vehicle.fuel_type
        }
        self.decoded_data = json.dumps(decoded_info, indent=4)

        # Get compatible parts
        from frappe.core.doctype.auto_part.auto_part import AutoPart
        compatible_parts = AutoPart.get_compatible_parts(self.vin_input)

        # Populate the table (assuming the table field is linked to Auto Part)
        self.set('compatible_parts_list', [])
        for part in compatible_parts:
            self.append('compatible_parts_list', {
                'auto_part': part.name  # Assuming the link field is named 'auto_part'
            })

    @frappe.whitelist()
    def decode_vin_custom_button(self):
        self.decode_vin_and_get_parts()
        self.save()
        frappe.msgprint(_("VIN decoded and compatible parts retrieved."))

    @frappe.whitelist()
    def get_compatible_parts_for_vin(vin):
        # Decode VIN using Vehicle.decode_vin method
        vehicle = frappe.new_doc('Vehicle')
        vehicle.vin = vin
        vehicle.decode_vin()

        # Get compatible parts
        from frappe.core.doctype.auto_part.auto_part import AutoPart
        compatible_parts = AutoPart.get_compatible_parts(vin)

        # Return list of part names (item_codes)
        return [part.name for part in compatible_parts]