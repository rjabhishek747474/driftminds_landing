import os

# Read environment variables with fallback to placeholder strings (so it doesn't fail locally)
replacements = [
    # 1. EmailJS Credentials
    ("YOUR_SERVICE_ID", os.environ.get("EMAILJS_SERVICE_ID", "YOUR_SERVICE_ID")),
    ("YOUR_TEMPLATE_ID", os.environ.get("EMAILJS_TEMPLATE_ID", "YOUR_TEMPLATE_ID")),
    ("YOUR_PUBLIC_KEY", os.environ.get("EMAILJS_PUBLIC_KEY", "YOUR_PUBLIC_KEY")),
    
    # 2. Phone Numbers
    ("+91-XXXXXXXXXX", os.environ.get("PHONE_NUMBER_FORMATTED", "+91-XXXXXXXXXX")),
    ("91XXXXXXXXXX", os.environ.get("PHONE_NUMBER_RAW", "91XXXXXXXXXX")),
    ("XXXXXXXXXX", os.environ.get("PHONE_NUMBER_SHORT", "XXXXXXXXXX")),
    
    # 3. Emails
    ("contact@yourdomain.com", os.environ.get("EMAIL_ADDRESS", "contact@yourdomain.com")),
    
    # 4. Locations
    ("YOUR_CITY_1, STATE_1 and YOUR_CITY_2, STATE_2", os.environ.get("LOCATIONS_COMMA_FULL", "YOUR_CITY_1, STATE_1 and YOUR_CITY_2, STATE_2")),
    ("YOUR_CITY_1, STATE_1", os.environ.get("LOCATION_CITY_1_STATE_1", "YOUR_CITY_1, STATE_1")),
    ("YOUR_CITY_2, STATE_2", os.environ.get("LOCATION_CITY_2_STATE_2", "YOUR_CITY_2, STATE_2")),
    ("YOUR_CITY_1 & YOUR_CITY_2", os.environ.get("LOCATIONS_AMPERSAND", "YOUR_CITY_1 & YOUR_CITY_2")),
]

# Find all HTML files in the project
html_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

print(f"Build: Found {len(html_files)} HTML files to process.")

# Replace placeholders in each file
for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified_content = content
    for placeholder, real_val in replacements:
        if real_val:
            modified_content = modified_content.replace(placeholder, real_val)
            
    if modified_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(modified_content)
        print(f"Build: Successfully injected variables into {file_path}")
    else:
        print(f"Build: No changes needed for {file_path}")

print("Build step: HTML files populated successfully!")
