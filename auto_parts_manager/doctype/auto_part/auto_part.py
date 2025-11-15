# -*- coding: utf-8 -*-
# Copyright (c) 2023, Your Company and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class AutoPart(Document):
    @staticmethod
    def get_compatible_parts(vin):
        """Query compatible parts based on VIN"""
        # Get parts where the VIN is in the compatible_vins table
        compatible_parts = frappe.db.sql("""
            SELECT DISTINCT ap.name, ap.part_code, ap.oem_reference,
                   ap.purchase_price, ap.sale_price, ap.stock_qty
            FROM `tabAuto Part` ap
            INNER JOIN `tabAuto Part Compatible VIN` apcv ON ap.name = apcv.parent
            WHERE apcv.vin = %s
            ORDER BY ap.part_code
        """, (vin,), as_dict=True)
        return compatible_parts