from . import __version__ as app_version

app_name = "auto_parts_manager"
app_title = "Auto Parts Manager"
app_publisher = "ERPBox"
app_description = "ERPNext app for selling auto parts with VIN search"
app_email = "support@erpbox.online"
app_license = "MIT"
app_version = "1.0.0"

fixtures = [
	"Auto Part Category",
	"Auto Part",
	"Vehicle",
	"Role",
	"Role Permission"
]

desk_links = [
	{
		"label": "Vehicle",
		"url": "/app/vehicle",
		"icon": "fa fa-car",
		"roles": ["Auto Manager", "Sales User"]
	},
	{
		"label": "Auto Part",
		"url": "/app/auto-part",
		"icon": "fa fa-cogs",
		"roles": ["Auto Manager", "Sales User"]
	},
	{
		"label": "Auto Part Category",
		"url": "/app/auto-part-category",
		"icon": "fa fa-tags",
		"roles": ["Auto Manager", "Sales User"]
	}
]

app_include_js = [
    "/assets/auto_parts_manager/js/pos_invoice.js",
    "/assets/auto_parts_manager/js/vehicle.js",
    "/assets/auto_parts_manager/js/vin_lookup.js"
]

required_apps = []