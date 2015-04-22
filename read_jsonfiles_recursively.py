from findtools.find_files import (find_files, Match)
import json


sh_files_pattern = Match(filetype='f', name='json*.txt')
found_files = find_files(path='/Users/geeshan', match=sh_files_pattern)

filenames = []

for found_file in found_files:		
	print found_file 
	#filenames.append(found_file)

	with open(found_file) as f:
	    for line in f:
	        while True:
	            try:
	                jfile = json.loads(line)
	                print json.dumps(jfile['b'])
	                #f.close
	                break
	            except ValueError:
	                # Not yet a complete JSON value
	                line += next(f)
	                
    				