
from conf import module



def read(key):
	
	key = [item for item in key.split(chr(47)) if item]
	
	return module.popen("%s %s" % (module.attrib.read, "/%s" % chr(47).join(key))).read().strip() 
def write(key, value):
	
	key = [item for item in key.split(chr(47)) if item]
	key = "/%s" % chr(47).join(key)
	
	
	value = module.dumps(str(value))
	
	if value == '"False"': value = "false"
	elif value == '"True"': value = "true"
		

	return module.write("%s %s %s" % (module.attrib.write, key, value))
def listkey(directory):
	
	dirs = [item for item in directory.split(chr(47)) if item]
	keylist = module.popen("%s %s" % (module.attrib.list, "/%s/" % chr(47).join(dirs))).readlines()
	
	
	
	return [key.strip() for key in keylist]
def load(directory, dumpf):
	""" dumpf: database.ini """
	module.write("%s %s < %s" % (module.attrib.load, directory, dumpf))
	
def dump(directory):
	""" directory: ../database.ini """
	return module.popen("%s %s" % (module.attrib.dump, directory)).read()
def watch(directory):
	return module.watch(directory)
	
def export(path, dump):
	with open(path, "w") as f : 
		f.write(dump)
		







