from django.shortcuts import render
from django.views.generic import View
from search.models import AnswerType
from search.models import ArticleType
from search.models import MoocType
from django.http import HttpResponse
import json

# Create your views here.
class SearchSuggest(View):
    def get(self, request):
        key_words = request.GET.get('s', '')
        s_type = request.GET.get('s_type', 'article')
        re_datas = []
        if key_words:
            if (s_type=='question'):
                zhihu_s = AnswerType.search()
                zhihu_s = zhihu_s.suggest('my_suggest', key_words, completion={
                    "field": "suggest",
                    "fuzzy": {
                        "fuzziness": 2
                    },
                    "size": 10
                })
                suggestions = zhihu_s.execute_suggest()
            elif(s_type=='article'):
                jobbole_s = ArticleType.search()
                jobbole_s = jobbole_s.suggest('my_suggest', key_words, completion={
                    "field": "suggest", "fuzzy": {
                        "fuzziness": 2
                    },
                    "size": 10

                })
                suggestions = jobbole_s.execute_suggest()
            else:
                mooc_s = MoocType.search()
                mooc_s = mooc_s.suggest('my_suggest', key_words, completion={
                    "field": "suggest", "fuzzy": {
                        "fuzziness": 2
                    },
                    "size": 10

                })
                suggestions = mooc_s.execute_suggest()

            for match in suggestions.my_suggest[0].options:
                source = match._source
                if (s_type=='mooc'):
                    re_datas.append(source['class_title'])
                else:
                    re_datas.append(source['title'])
        return HttpResponse(json.dumps(re_datas), content_type="application/json")