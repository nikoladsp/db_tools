import setuptools


def get_version() -> str:
	import re
	from os.path import dirname, join

	topline = re.compile(
		r'^(\w%(name_chars)s*) \(([^\(\) \t]+)\)'
		r'((\s+%(name_chars)s+)+)\;'
		% {'name_chars': '[-+0-9a-z.]'},
		re.IGNORECASE)

	version = '0.0.0'

	try:
		changelog_path = join(dirname(__file__), 'debian/changelog')
		with open(changelog_path, 'r') as fd:
			for line in fd.readlines():
				top_match = topline.match(line.strip())
				if top_match:
					version = top_match.group(2)
					break
	except FileNotFoundError:
		pass

	return version


if __name__ == '__main__':
	setuptools.setup(
		version=get_version(),
	)
