from . import __version__ as app_version

app_name = "auto_parts_manager"
app_title = "Auto Parts Manager"
app_publisher = "ERPBox"
app_description = "ERPNext app for selling auto parts with VIN search"
app_email = "support@erpbox.online"
app_license = "MIT"
app_version = "1.0.0"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/auto_parts_manager/css/auto_parts_manager.css"
# app_include_js = "/assets/auto_parts_manager/js/auto_parts_manager.js"

# include js, css files in header of web template
# web_include_css = "/assets/auto_parts_manager/css/auto_parts_manager.css"
# web_include_js = "/assets/auto_parts_manager/js/auto_parts_manager.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "auto_parts_manager/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "auto_parts_manager.utils.jinja_methods",
#	"filters": "auto_parts_manager.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "auto_parts_manager.install.before_install"
# after_install = "auto_parts_manager.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "auto_parts_manager.uninstall.before_uninstall"
# after_uninstall = "auto_parts_manager.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "auto_parts_manager.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Auto Part": "auto_parts_manager.permissions.get_auto_part_permissions",
	"Vehicle": "auto_parts_manager.permissions.get_vehicle_permissions",
	"Auto Part Category": "auto_parts_manager.permissions.get_auto_part_category_permissions",
}

has_permission = {
	"Auto Part": "auto_parts_manager.permissions.has_auto_part_permission",
	"Vehicle": "auto_parts_manager.permissions.has_vehicle_permission",
	"Auto Part Category": "auto_parts_manager.permissions.has_auto_part_category_permission",
}
#
# has_permission = {
#	"event": "auto_parts_manager.doctype.event.event.has_permission",
#	"task": "auto_parts_manager.doctype.task.task.has_permission"
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"auto_parts_manager.tasks.all"
#	],
#	"daily": [
#		"auto_parts_manager.tasks.daily"
#	],
#	"hourly": [
#		"auto_parts_manager.tasks.hourly"
#	],
#	"weekly": [
#		"auto_parts_manager.tasks.weekly"
#	],
#	"monthly": [
#		"auto_parts_manager.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "auto_parts_manager.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "auto_parts_manager.event.get_events"
# }
#
# each overriding function accepts a `data` parameter;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "auto_parts_manager.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Receipt"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"auto_parts_manager.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# translated_search_doctypes = []

# import frappe
# from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
# from frappe.custom.doctype.property_setter.property_setter import make_property_setter

# standard_portal_menu_items = [
#	{"title": _("Announcements"), "route": "/announcements", "reference_doctype": "Announcement", "role": "Member"},
#	{"title": _("Blog Post"), "route": "/blog", "reference_doctype": "Blog Post", "role": "Member"},
#	{"title": _("Discussion"), "route": "/discussion", "reference_doctype": "Discussion", "role": "Member"},
#	{"title": _("Marketplace"), "route": "/marketplace", "reference_doctype": "Marketplace", "role": "Member"}
# ]

website_route_rules = [
	{"from_route": "/auto-parts/<path:app_path>", "to_route": "auto-parts"},
]

# doctype_js = {
#	"POS Invoice": "public/js/pos_invoice.js"
# }

# fixtures = [
#	{"dt": "Custom Field", "filters": [["module", "=", "Auto Parts Manager"]]},
#	{"dt": "Property Setter", "filters": [["module", "=", "Auto Parts Manager"]]},
# ]

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

# Required Apps
# --------------
required_apps = []

# Further help
# ------------

# More info about the app: https://docs.erpnext.com/docs/user/manual/en/auto-parts-manager