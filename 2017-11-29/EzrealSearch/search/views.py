from django.shortcuts import render
from django.views.generic.base import View
from search.models import ArticleType
from search.models import AnswerType
from django.http import HttpResponse
import json

from elasticsearch import Elasticsearch #为实现搜索功能引入的模块
# Create your views here.

client = Elasticsearch(hosts=["127.0.0.1"])

#实现搜索建议、补全
class SearchSuggest(View):
    def get(self, request):
        key_words = request.GET.get('s', '')
        re_datas = []
        if key_words:
            s = ArticleType.search()
            s = s.suggest('my_suggest', key_words, completion={
                "field": "suggest","fuzzy":{
                    "fuzziness": 2
                },
                "size": 10

            })
            suggestions = s.execute_suggest()
            for match in suggestions.my_suggest[0].options:
                source = match._source
                re_datas.append(source['title'])

        return HttpResponse(json.dumps(re_datas), content_type="application/json")

#实现搜索功能
class SearchView(View):
    def get(self, request):
        key_words = request.GET.get("q", "")
        response = client.search(
            index = "jobbole",
            body = {
                "query":{
                    "multi_match":{
                        "query":key_words,
                        "fields":["tags", "title", "content"]
                    }
                },
                "from":0,
                "size":10,
                "highlight":{
                    "pre_tags": ['<span class="keyWord">'],
                    "post_tags": ['</span>'],
                    "fields":{
                        "title":{},
                        "content":{},
                    }
                }
            }
        )
        total_nums = response["hits"]["total"]
        hit_list = []
        for hit in response["hits"]["hits"]:
            hit_dict = {}
            if "title" in hit["highlight"]:
                hit_dict["title"] = hit["highlight"]["title"]
            else:
                hit_dict["title"] = hit["_source"]["title"]
            if "content" in hit["highlight"]:
                hit_dict["content"] = hit["highlight"]["content"][:400]
            else:
                hit_dict["content"] = hit["_source"]["content"][:400]

            hit_dict["create_date"] = hit["_source"]["create_date"]
            hit_dict["url"] = hit["_source"]["url"]
            hit_dict["score"] = hit["_score"]

            hit_list.append(hit_dict)

        return render(request, "result.html", {"all_hits":hit_list, "key_words":key_words})

