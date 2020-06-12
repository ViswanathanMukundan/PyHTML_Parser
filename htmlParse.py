'''...Just a basic HTML parsing code...'''


def tagExtractor(data):
	t = []
	for i in range(len(data)):
		if data[i] == '<':
			s = ""
			while data[i] != '>':
				s += data[i]
				i += 1
			s += '>'
			t.append(s)
	return t
def contentExtractor(data):
	d = []
	for i in range(len(data)-1):
		if data[i] == '>' and data[i+1] != '<':
			s = ""
			i += 1
			while data[i] != '<':
				s += data[i]
				i += 1
			if len(s) > 0:
				d.append(s)
	return d 
data = "<html><h1>This is the title of the page</h1><p>This is a sample paragraph denoting my capability of successfully creating my first html document.</p></html>"
print("Tags: " , tagExtractor(data))
print("Data: " , contentExtractor(data))
			
