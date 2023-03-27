import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

# from .forms import PictureForm
from .models import Author, Quote


# Create your views here.
def main(request):
    return render(request, 'app_my_site/index.html', context={"title": "AUTHOR_QUOTE"})


@login_required
def upload_author(request):
    pass
    # form = PictureForm(instance=Picture())
    # if request.method == "POST":
    #     form = PictureForm(request.POST, request.FILES, instance=Picture())
    #     if form.is_valid():
    #         pic = form.save(commit=False)
    #         pic.user = request.user
    #         pic.save()
    #         return redirect(to='app_instagram:pictures')
    # return render(request, 'app_instagram/upload.html', context={"title": "Web 9 Group", "form": form})

def upload_quote(request):
    pass

@login_required
def authors_descr(request):
    pass
    # pictures = Picture.objects.filter(user=request.user).all()
    # return render(request, 'app_instagram/pictures.html',
    #               context={"title": "Web 9 Group", "pictures": pictures, "media": settings.MEDIA_URL})


@login_required
def remove(request, pic_id):
    picture = Picture.objects.filter(pk=pic_id, user=request.user)
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, str(picture.first().path)))
    except OSError as e:
        print(e)
    picture.delete()
    return redirect(to='app_instagram:pictures')


@login_required
def edit(request, pic_id):
    if request.method == "POST":
        description = request.POST.get("description")
        Picture.objects.filter(pk=pic_id, user=request.user).update(description=description)
        return redirect(to='app_instagram:pictures')
    picture = Picture.objects.filter(pk=pic_id, user=request.user).first()
    return render(request, 'app_instagram/edit.html',
                  context={"title": "Web 9 Group", "pic": picture, "media": settings.MEDIA_URL})