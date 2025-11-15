// Copyright (c) 2023, Your Company and contributors
// For license information, please see license.txt

frappe.ui.form.on("VIN Lookup", {
  refresh: function (frm) {
    frm.add_custom_button(__("Decode VIN"), function () {
      if (!frm.doc.vin_input) {
        frappe.msgprint(__("Please enter a VIN before decoding."));
        return;
      }
      frappe.call({
        method: "decode_vin_custom_button",
        doc: frm.doc,
        callback: function (r) {
          if (!r.exc) {
            frm.reload_doc();
            frappe.msgprint(__("VIN decoded and compatible parts retrieved."));
          }
        },
      });
    });
  },
});
