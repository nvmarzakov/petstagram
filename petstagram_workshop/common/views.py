from django.shortcuts import render, redirect

from petstagram_workshop.common.models import PhotoLike
from petstagram_workshop.photos.models import Photo


def apply_user_like_photo(photo):
    # TODO: fix this for current user when authentication is available
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


# Create your views here.
def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_like_photo(photo) for photo in photos]

    context = {
        'photos': Photo.objects.all(),
    }
    return render(request, 'common/home-page.html', context, )


def get_user_liked_photos(photo_id):
    # TODO: fix when auth
    return PhotoLike.objects.filter(photo_id=photo_id)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)
    if user_liked_photos:
        PhotoLike.objects.filter(photo_id=photo_id) \
            .delete()
    else:
        # Variant 2
        PhotoLike.objects.create(
            photo_id=photo_id
        )

    redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    return redirect(redirect_path)

    # Variant 1
    # photo_like = PhotoLike(
    #     photo_id=photo_id,
    # )
    # photo_like.save()

    # Variant 2
    # Variant 3 (wrong - additional call to db)
    # Correct, only if validation is needed
    # photo = Photo.objects.get(pk=photo_id)
    #
    # PhotoLike.objects.create(
    #     photo=photo
    # )
