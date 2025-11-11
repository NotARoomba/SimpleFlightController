import json
import re

# Load the CDN mappings
with open('assets/cdn.json', 'r') as f:
    data = json.load(f)

# Create a dictionary mapping filenames to CDN URLs
mappings = {m['original_filename']: m['cdn_url'] for m in data['mappings']}

# Read the GUIDE.md file
with open('GUIDE.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Function to replace image references
def replace_image(match):
    alt_text = match.group(1)
    filename = match.group(2)
    
    if filename in mappings:
        return f'![{alt_text}]({mappings[filename]})'
    else:
        # Keep the original if no mapping found
        return match.group(0)

# Replace all asset references with CDN URLs
new_content = re.sub(r'!\[(.*?)\]\(assets/(.*?)\)', replace_image, content)

# Write the updated content back
with open('GUIDE.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Updated GUIDE.md with CDN URLs')
print(f'Total mappings: {len(mappings)}')
