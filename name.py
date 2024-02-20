import json,shutil,glob,os,re
import eyed3
try:
	os.mkdir('mp3')
except OSError:
	pass

def get_integer_length(x):
	first=x.split('.')[0]
	return len(first)

def parse_name(filename):
	info={'orig':filename}
	print(filename)
	m=re.search(r'^S(\d+)E([0-9.]+)',filename)
	S=E=None
	if m:
		S,E=m.groups(1)
	else:
		m=re.search(r'^Episode ([0-9.]+)',filename)
		if m:
			S='1'
			E=m.group(1)
		else:
			if filename.startswith('KJB100'):
				S='2'
				E='15.5'
			elif filename.startswith('KJB Holiday'):
				S='2'
				E='14.75'
			else:
				print('No match')
	if S is not None and E is not None:
		parts = filename.split(':',1)
		if len(parts)==1:
			rest=parts[0]
			m=re.search('^Episode ([0-9.]+)(.*)',rest)
			if m:
				rest=m.group(2).strip().strip('-').strip()
		else:
			prefix,rest=parts
		rest=rest.strip()
		rest=rest.replace('/','_').replace(':','')
		if 'Agent Secret FX-18' in rest:
			# They misnamed this file, so we have to fix it
			S='3'
			E='2'
		if get_integer_length(E)==1:
			E='0'+E
		if get_integer_length(S)==1:
			S='0'+S
		info['out_filename']=out_filename='S{}E{}_{}.mp3'.format(S,E,rest)
		print('Final: S{}E{}: {}'.format(S,E,rest))
		info['name']=rest
		info['S']=S
		info['E']=E
		info['full_name']='S{}E{}: {}'.format(S,E,rest)
		return info

def track_number_to_integer(e):
	parts=e.split('.')
	if len(parts)==1:
		return int(e)*100
	else:
		a,b=[int(x) for x in parts]
		return a*100+b

def apply_id3(path, info, attrib):
	audiofile=eyed3.load(path)
	audiofile.initTag()
	kjb="Kill James Bond!"
	audiofile.tag.artist = kjb
	audiofile.tag.album = '{} Season {}'.format(kjb,info['S'])
	audiofile.tag.album_artist = kjb
	audiofile.tag.title = info['full_name']
	audiofile.tag.track_num = track_number_to_integer(info['E'])
	audiofile.tag.release_date = attrib['published_at'].split('.')[0]
	audiofile.tag.save()

for jsonfile in glob.glob('*.json'):
	with open(jsonfile,'r') as f:
		data=json.load(f)
		entries=data['data']

		for entry in entries:
			if entry['type']=='post':
				attrib=entry['attributes']
				if attrib['post_type']!='audio_file':
					continue
				number=attrib['patreon_url'].split('-')[-1]
				#print(number)
				good_name=attrib['title']
				info = parse_name(good_name)
				if info is not None:
					mp3s=glob.glob('{}_post_*.mp3'.format(number))
					if len(mp3s)!=1:
						print('Wrong number of mp3s! {}'.format(mp3s))
					else:
						mp3file=mp3s[0]
						outpath=os.path.join('mp3',info['out_filename'])
						shutil.copy2(mp3file,outpath)
						apply_id3(outpath,info,attrib)
				else:
					print("No info for file {}".format(good_name))
