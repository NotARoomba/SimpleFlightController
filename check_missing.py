import json

with open('assets/cdn.json', 'r') as f:
    data = json.load(f)

filenames = [m['original_filename'] for m in data['mappings']]

missing = ['pcb_route_differential_menu.png', 'pcb_differential_pair_select.png', 'pcb_clearance_setting.png']

print("Checking for missing files:")
for name in missing:
    if name in filenames:
        print(f"{name}: FOUND")
    else:
        print(f"{name}: MISSING")
