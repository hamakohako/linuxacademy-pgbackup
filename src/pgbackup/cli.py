from argparse import Action, ArgumentParser

known_drivers = ['local', 's3']


class DriverAction(Action):
	def __call__(self, parser, namespace, values, option_string=None):
		driver, destination = values
		if driver.lower() not in known_drivers:
			parser.error("Unknown driver, available drivers are 'local' and 's3'")
		namespace.driver = driver.lower()
		namespace.destination = destination

def create_parser():
	parser = ArgumentParser()
	parser.add_argument('url', help='URL of the PostgreSQL database to backup')
	parser.add_argument('--driver',
		help='how and where to store the backup',
		nargs = 2,
		required=True,
		action=DriverAction)
	return parser
