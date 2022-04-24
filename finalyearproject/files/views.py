from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ScanForm
from .models import Scan
# Create your views here.

def upload_scan(request):
    if request.method == 'POST':
        form = ScanForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.scan = request.FILES['image']
            # print(image.scan)
            #return HttpResponseRedirect("/")
            image.save()
            segmented_image = dummy(image)
            return render(request, 'files/details.html', {'image': image, 'segmented_image' : segmented_image})
    # if request.method == 'GET':
    #     scans = Scan.objects.order_by('name')
    #     return render(request, "files/images.html", {"images": scans})
    else:
        form = ScanForm
    return render(request, 'files/upload.html', {'form':form}) # scan.html


def dummy(image):
    """
    image.image.url will contain the url of submitted image
    pass the submitted image through ML model to produce segmented image
    save segmented image under /media/scans/segmented/ and return path to segmented image
    """
    submitted_image_path = image.image.url
    return "/media/scans/segmented/dummy_segmented.png"