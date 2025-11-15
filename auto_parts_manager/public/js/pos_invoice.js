// Copyright (c) 2023, Your Company and contributors
// For license information, please see license.txt

frappe.ui.form.on("POS Invoice", {
  refresh: function (frm) {
    // Add VIN Search button
    frm.add_custom_button(__("VIN Search"), function () {
      // Open modal for VIN input
      let d = new frappe.ui.Dialog({
        title: __("Enter VIN"),
        fields: [
          {
            label: __("VIN"),
            fieldname: "vin",
            fieldtype: "Data",
            reqd: 1,
          },
        ],
        primary_action_label: __("Search Parts"),
        primary_action(values) {
          if (!values.vin) {
            frappe.msgprint(__("Please enter a VIN."));
            return;
          }

          // Call backend method to get compatible parts
          frappe.call({
            method:
              "auto_parts_manager.auto_parts_manager.doctype.vin_lookup.vin_lookup.get_compatible_parts_for_vin",
            args: {
              vin: values.vin,
            },
            callback: function (r) {
              if (r.message) {
                let parts = r.message;
                if (parts.length === 0) {
                  frappe.msgprint(
                    __("No compatible parts found for this VIN.")
                  );
                  return;
                }

                // Add parts to POS items
                parts.forEach(function (part_name) {
                  // Get item details (assuming Item doctype has name as part_name)
                  frappe.call({
                    method: "frappe.client.get",
                    args: {
                      doctype: "Item",
                      name: part_name,
                    },
                    callback: function (item_r) {
                      if (item_r.message) {
                        // Add to items table
                        frm.add_child("items", {
                          item_code: item_r.message.item_code,
                          item_name: item_r.message.item_name,
                          qty: 1,
                          rate: item_r.message.standard_rate || 0,
                        });
                        frm.refresh_field("items");
                        frappe.msgprint(__("Parts added to transaction."));
                      }
                    },
                  });
                });
              }
              d.hide();
            },
          });
        },
      });
      d.show();
    });
  },
});
