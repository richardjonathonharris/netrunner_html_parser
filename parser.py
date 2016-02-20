import os

class Parser(object):
	def __init__(self):
		self.file_name = input('Please enter file name: ')
		self.file_to_read = None
		self.file_mem = None
		self.parsed_dict = None
		self.latest_key = None
	
	def get_files(self):
		if not self.file_name:
			files = os.listdir(os.getcwd())
			found_files = [file for file in files if file[-4:] == '.txt']
			if len(found_files) == 0:
				return 'No files found'
			else:
				return found_files

		else:
			file_exists = os.path.isfile(self.file_name)
			if file_exists:
				return [self.file_name]
			else:
				return 'Could not find that file'
	def read_file(self):
		with open(self.file_to_read, 'rb') as open_file:
			data = open_file.read()
		self.file_mem = data

	def parse_file(self):
		self.file_mem = self.file_mem.split(b'\n')
		self.file_mem = [item for item in self.file_mem if item != b'']
		self.parsed_dict = {}
		for item in self.file_mem:
			if item[0:3] == b'###':
				key = item[4:].split(b' ')[0]
				self.parsed_dict[key] = []
				self.latest_key = key
			elif item[0:2] == b'* ':
				print(item)
				card_parse = {}
				card_parse['number'] = item[2:3]
				# put some regex here
				card_parse['title'] = item.split(b'[')[1]
				self.parsed_dict[self.latest_key].append(card_parse)
			else:
				pass
		return self.parsed_dict

	def run(self):
		file_to_read = self.get_files()
		for file in file_to_read:
			self.file_to_read = file
			self.read_file()
			for item in self.parse_file():
				print(item)
			print(self.parsed_dict)
			print('printed parsed dict')

if __name__ == '__main__':
	parse = Parser()
	parse.run()
