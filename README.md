# Auto Parts Manager

A comprehensive ERPNext app for managing auto parts inventory, sales, and vehicle information with VIN decoding capabilities.

## Features

- **VIN Decoding**: Decode vehicle identification numbers using external API to automatically populate vehicle details
- **Vehicle Management**: Track vehicles with VIN, brand, model, year, engine type, and fuel type
- **Auto Parts Catalog**: Manage parts inventory with compatibility mapping to specific VINs
- **POS Integration**: Quick VIN-based parts search directly in ERPNext Point of Sale
- **Multi-brand Support**: Supports European and American vehicle brands

## Prerequisites

- ERPNext v15.x
- Python 3.12.3
- Node.js v20.19.5
- Yarn 1.22.22
- Bench tool

## Installation

### Step 1: Get the App

```bash
bench get-app auto_parts_manager https://github.com/khechine/auto_parts_manager.git
```

### Step 2: Install on Site

```bash
bench --site [your-site-name] install-app auto_parts_manager
```

### Step 3: Run Migration

```bash
bench --site [your-site-name] migrate
```

This will install the app and load sample data (fixtures) including:

- 20 sample vehicles
- 10 auto part categories
- 20 sample auto parts with compatibility data

## API Key Setup

The app uses VINDecoder.eu API for VIN decoding. To enable this feature:

1. Visit [VINDecoder.eu](https://vindecoder.eu/) and sign up for a free API key
2. In ERPNext, go to **Auto Parts Manager Settings** (or create if not exists)
3. Set the **VIN Decoder API Key** field with your API key

The free tier provides 20 lookups per month for testing.

## Usage

### VIN Lookup

1. Navigate to **Auto Parts Manager > VIN Lookup**
2. Enter a 17-character VIN
3. Click **Decode VIN** button
4. View decoded vehicle information (brand, model, year, engine type, fuel type)
5. See compatible parts list automatically populated

![VIN Lookup Screenshot](screenshots/vin_lookup.png)

### Vehicle Management

1. Navigate to **Auto Parts Manager > Vehicle**
2. Create a new vehicle record
3. Enter VIN (optional - will trigger automatic decoding)
4. Fill in additional details: customer, license plate (matricule)
5. Save to store vehicle information

The VIN field validates format and automatically decodes if API key is configured.

![Vehicle Management Screenshot](screenshots/vehicle_management.png)

### Auto Part Catalog

1. Navigate to **Auto Parts Manager > Auto Part**
2. Create new part with:
   - Part code (unique identifier)
   - OEM reference
   - Category (link to Auto Part Category)
   - Purchase/sale prices
   - Stock quantity
3. Add compatible VINs in the **Compatible VINs** table
4. Link to ERPNext Item for inventory management

![Auto Part Catalog Screenshot](screenshots/auto_part_catalog.png)

### POS Integration

1. Open ERPNext Point of Sale
2. Click **VIN Search** button
3. Enter vehicle VIN in the modal
4. Compatible parts are automatically added to the transaction
5. Complete the sale as usual

![POS Integration Screenshot](screenshots/pos_integration.png)

## Screenshots

- [VIN Lookup Interface](screenshots/vin_lookup.png)
- [Vehicle Management](screenshots/vehicle_management.png)
- [Auto Part Catalog](screenshots/auto_part_catalog.png)
- [POS Integration](screenshots/pos_integration.png)

## Troubleshooting

### VIN Decoding Issues

- **API Key Not Configured**: Ensure VIN Decoder API key is set in Auto Parts Manager Settings
- **Invalid VIN Format**: VIN must be exactly 17 characters, containing only valid characters (no I, O, Q)
- **API Limit Exceeded**: Free tier allows 20 lookups/month. Upgrade or wait for reset
- **Network Issues**: App has retry logic (3 attempts) and falls back to basic validation

### POS Integration Problems

- **Button Not Showing**: Ensure POS Invoice doctype is properly loaded
- **Parts Not Found**: Verify compatible parts exist in catalog for the entered VIN
- **Permission Issues**: Check user has "Auto Manager" or "Sales User" role

### Common Issues

- **Migration Fails**: Ensure all dependencies are installed and site is accessible
- **Fixtures Not Loading**: Check file permissions and database connectivity
- **JavaScript Errors**: Clear browser cache and reload page

### Logs and Debugging

Check ERPNext error logs for API call failures:

- Go to **Error Log** in ERPNext Desk
- Filter by "VIN Decoding Error" for API issues

### Support

For issues not covered here:

1. Check ERPNext version compatibility
2. Verify all prerequisites are met
3. Review recent changes in app code
4. Contact developer at mehdi.khechine@example.com

## License

MIT License - see [LICENSE](license.txt) file for details
