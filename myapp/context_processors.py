# from .models import ViewerCount

# def viewer_count(request):
#     viewer_count_obj = ViewerCount.objects.first()
#     if viewer_count_obj is None:
#         viewer_count_obj = ViewerCount.objects.create(count=0)
#     else:
#         viewer_count_obj.count += 1
#         viewer_count_obj.save()
#     return {'viewer_count': viewer_count_obj.count}

