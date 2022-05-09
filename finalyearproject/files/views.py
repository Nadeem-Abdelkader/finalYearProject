from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ScanForm
from .models import Scan
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt


# Create your views here.

def upload_scan(request):
    if request.method == 'POST':
        form = ScanForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.scan = request.FILES['image']
            # print(image.scan)
            # return HttpResponseRedirect("/")
            image.save()
            segmented_image = ml_model(image)
            return render(request, 'files/details.html', {'image': image, 'segmented_image': segmented_image})
    # if request.method == 'GET':
    #     scans = Scan.objects.order_by('name')
    #     return render(request, "files/images.html", {"images": scans})
    else:
        form = ScanForm
    return render(request, 'files/upload.html', {'form': form})  # scan.html


def ml_model(image):
    """
    image.image.url will contain the url of submitted image
    pass the submitted image through ML model to produce segmented image
    save segmented image under /media/scans/segmented/ and return path to segmented image
    """
    submitted_image_path = image.image.url
    print(submitted_image_path)
    print(os.getcwd())
    img = cv2.imread(
        "/Users/nadeem/Documents/Monash/Monash Year 3 Semester 2/Computer Science Project 2/FYP/finalYearProject/finalyearproject" + submitted_image_path)
    b, g, r = cv2.split(img)

    rgb_img = cv2.merge([r, g, b])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # noise removal
    kernel = np.ones((2, 2), np.uint8)
    # opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    # sure background area
    sure_bg = cv2.dilate(closing, kernel, iterations=3)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(sure_bg, cv2.DIST_L2, 3)
    # Threshold
    ret, sure_fg = cv2.threshold(dist_transform, 0.1 * dist_transform.max(), 255, 0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1
    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0
    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]
    # plt.imshow(rgb_img)
    # plt.xticks([]), plt.yticks([])
    # plt.imshow(thresh, 'gray')
    plt.imsave(
        "/Users/nadeem/Documents/Monash/Monash Year 3 Semester 2/Computer Science Project 2/FYP/finalYearProject/finalyearproject/media/scans/segmented/segmented.png",
        thresh)
    # plt.xticks([]), plt.yticks([])
    # plt.tight_layout()
    # plt.savefig("segmented_image.png")

    return "/media/scans/segmented/segmented.png"
