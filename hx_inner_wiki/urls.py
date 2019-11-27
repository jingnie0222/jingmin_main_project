from django.urls import path
#from .views import inner_wiki_list
from .views import inner_wiki_list, inner_wiki_new, inner_wiki_edit, inner_wiki_detail, inner_wiki_delete
from editor_md.views import upload_image

urlpatterns = [
    path('inner_wiki_list/', inner_wiki_list),
    path('inner_wiki_edit/', inner_wiki_edit),
    path('inner_wiki_new/', inner_wiki_new),
    path('inner_wiki_detail_<task_id>', inner_wiki_detail),
    path('inner_wiki_delete/', inner_wiki_delete),

    path('upload/image', upload_image, name='editor_upload_image'),
]
