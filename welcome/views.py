import os

from django.shortcuts import render
from .forms import UploadFileForm
from PIL import Image, ImageOps, ImageFilter
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def applyfilter(filename, preset):
	inputfile = os.path.join(settings.BASE_DIR, 'media', 'input', filename)
	file = os.path.splitext(filename)[0]
	ext = filename.split('.')[-1]
	outputfilename = file + '-out.' + ext
	outputpath = os.path.join(settings.BASE_DIR, 'media', 'output', outputfilename)
	im = Image.open(inputfile)
	if preset == 'gray':
		im = ImageOps.grayscale(im)
	elif preset == 'edge':
		im = ImageOps.grayscale(im)
		im = im.filter(ImageFilter.FIND_EDGES())
	elif preset == 'poster':
		im = ImageOps.posterize(im, 3)
	elif preset == 'solar':
		im = ImageOps.solarize(im, threshold=80)
	elif preset == 'blur':
		im = im.filter(ImageFilter.BLUR)
	elif preset == 'sepia':
		sepia = []
		r,g,b = (239, 224, 185)
		for i in range(255):
			sepia.extend((r*i/255, g*i/255, b*i/255))
		im = im.convert("L")
		im.putpalette(sepia)
		im = im.convert("RGB")
	else:
		print 'Preset not defined!'
	im.save(outputpath)
	return outputfilename

def handle_upload(f, preset):
	uploadfile = os.path.join(settings.BASE_DIR, 'media', 'input', f.name)
	with open(uploadfile, 'wb+') as dest:
		for chunk in f.chunks():
			dest.write(chunk)
	outputfile = applyfilter(f.name, preset)
	return outputfile

@login_required(login_url="/auth/login/")
def index(req):
	form = UploadFileForm()
	if req.method == 'POST':
		form = UploadFileForm(req.POST, req.FILES)
		if form.is_valid():
			preset = req.POST['preset']
			outputfilename = handle_upload(req.FILES['filefield'], preset)
			messages.success(req, 'Filter Applied !')
			return render(req, 'welcome/result.html', {'outputfilename': outputfilename})
		else:
			messages.error(req, 'Error Occured !')
			return render(req, 'welcome/index.html', {'form': form})
	else:
		return render(req, 'welcome/index.html', {'form':form})

def health(request):
    return HttpResponse(PageView.objects.count())
