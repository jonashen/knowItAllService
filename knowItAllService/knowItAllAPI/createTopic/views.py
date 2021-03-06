from django.http import JsonResponse
from django.db import IntegrityError
from ..models import *
from ..constants import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# https://stackoverflow.com/a/3711911
def createTopic(request):
    if request.method != "POST":
        return JsonResponse(POST_400, status=400)

    # Grab the query parameters; note that .GET must be used to grab parameters from the actual URL
    title = request.GET.get(title_param)
    category = request.GET.get(category_param)
    tags = request.GET.get(tags_param)

    # Check if all parameters provided
    if any(var is None for var in [title, category, tags]):
        return JsonResponse(createTopic_400_ALL, status=400)

    # Check if category is valid
    if not category.isdigit() or not (1 <= int(category) <= 4):
        return JsonResponse(createTopic_400_C, status=400)
    category = int(category)

    # Store data into db
    topic = Topic(title=title,category=Category.objects.get(pk=category), avRating=0, numReviews=0)
    try:
        topic.save()

        # Store each tag into db
        tList = tags.split(',')
        for tag in tList:
            t = Tag.objects.filter(title=tag)
            # Tag doesn't exist in db yet
            if len(t) == 0:
                t = Tag(title=tag)
                t.save()
            else:
                t = t.first()

            tl = TagLinker.objects.filter(tagID=t, type='topic', topicID=topic)
            if len(tl) == 0:
                tl = TagLinker(tagID=t, type='topic', topicID=topic)
                tl.save()
            else:
                tl = tl.first()
            tl.save()

        return JsonResponse(createTopic_SUCCESS(t.title, CATEGORIES.get(category), tList), status=200)

    except IntegrityError:
        return JsonResponse(UNIQUE_400, status=400)