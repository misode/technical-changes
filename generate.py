from glob import glob
import json
import os

versions = [e.replace('\\', '/') for e in glob('*/*.md')]

changes = []
for name in versions:
	[group, version] = name.removesuffix('.md').split('/')
	with open(name, 'r') as f:
		text = f.read().split('\n\n')
	for change in text:
		i = change.index('|')
		tags = change[0:i].strip().split(' ')
		content = change[i+1:].strip().replace('->', '→').replace('\n...\n', '\n\n')
		changes.append({
			'group': group,
			'version': version,
			'tags': tags,
			'content': content,
		})

os.makedirs('generated', exist_ok=True)
with open('generated/changes.json', 'w') as f:
	json.dump(changes, f, indent=2)
	f.write('\n')
with open('generated/changes.min.json', 'w') as f:
	json.dump(changes, f)

print(f'Generated {len(changes)} changes from {len(versions)} versions')
