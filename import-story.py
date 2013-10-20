import xml.parsers.expat
Story = {}
Story['scenes'] = {}
ElementStack = []
CurrentScene = ''
CurrentOption = ''

def start_element(name, attrs):
	global ElementStack
	ElementStack.append( name )


def character_data(data):
	global Story
	global ElementStack
	global CurrentScene
	global CurrentOption
	stackTop = ElementStack[-1]
	if stackTop == 'scene-name':
		CurrentScene = data
		Story['scenes'][CurrentScene] = {}
		Story['scenes'][CurrentScene]['options'] = {}
	elif stackTop == 'story-text':
		Story['scenes'][CurrentScene]['story-text'] = data
	elif stackTop == 'option-text':
		CurrentOption = data
		Story['scenes'][CurrentScene]['options'][CurrentOption] = {}
	elif stackTop == 'option-requires':
		Story['scenes'][CurrentScene]['options'][CurrentOption]['option-requires'] = data
	elif stackTop == 'option-destination':
		Story['scenes'][CurrentScene]['options'][CurrentOption]['option-destination'] = data
	elif stackTop == 'add-inventory':
		Story['scenes'][CurrentScene]['options'][CurrentOption]['add-inventory'] = data
	elif stackTop == 'remove-inventory':
		Story['scenes'][CurrentScene]['options'][CurrentOption]['remove-inventory'] = data
	elif stackTop == 'tite':
		Story['title'] = data
	elif stackTop == 'description':
		Story['description'] = data
	elif stackTop == 'version':
		Story['version'] = data
	elif stackTop == 'start-scene':
		Story['start-scene'] = data


def end_element(name):
	global ElementStack
	ElementStack.pop()


def parse_story(filename):
	parser = xml.parsers.expat.ParserCreate()
	parser.StartElementHandler = start_element
	parser.EndElementHandler = end_element
	parser.CharacterDataHandler = character_data
	parser.ParseFile(open('/home/derek/Desktop/xml-example.xml', 'rb'))
	return Story


