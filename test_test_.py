def post(self):
	log.debug("uploading...")
	# get idarea
	iFrame = self.get_argument("iframe",False)
	idarea = self.get_argument("idarea","")

	# get the uploaded filename
	host = self.request.host
	log.debug("host=%s" % host)
	file1 = self.request.files['file1'][0]
	original_fname = file1['filename']

	# get the file extension
	extension = os.path.splitext(original_fname)[-1]

	# verify the image type
	img_type = imghdr.what(original_fname,file1['body'])
	log.debug("img_type=%s" % img_type)
	if not img_type:
	  self.finish("Wrong file type")
	  return

	# get the time stamp
	yyyy = time.strftime("%Y")
	mm = time.strftime("%m")
	dd = time.strftime("%d")
	img_folder = "uploads/"+yyyy+"/"+mm+"/"+dd+"/"
	if not os.path.exists(img_folder):
	  os.makedirs(img_folder)

	fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
	final_filename= img_folder+fname+extension
	log.debug("saved to %s" % final_filename)
	output_file = open(final_filename, 'w')
	output_file.write(file1['body'])

if __name__ == "__main__":
  import os.path
  basedir = os.path.dirname(__file__)
  print basedir
  print __file__
  print os.path.abspath(os.path.join(basedir,os.path.pardir,'static/upload'))
  print os.path.pardir
  