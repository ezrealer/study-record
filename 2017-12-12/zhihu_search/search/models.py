from django.db import models
from datetime import datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean, analyzer, InnerObjectWrapper, Completion, Keyword, Text, \
    Integer

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["localhost"])


# 重写analyzer
class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])


# 知乎问答字段
class AnswerType(DocType):
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyzer="ik_max_word")
    url = Keyword()
    answer_num = Integer()
    topics = Text(analyzer="ik_max_word")
    crawl_time = Date()
    zhihu_id = Integer()
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = 'zhihu'
        doc_type = 'answer'


# 伯乐在线文章字段
class ArticleType(DocType):
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyzer="ik_max_word")
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    praise_num = Integer()
    comment_num = Integer()
    fav_num = Integer()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "jobbole"
        doc_type = "artcile"

#慕课网字段
class MoocType(DocType):
    suggest = Completion(analyzer=ik_analyzer)
    class_title = Text(analyzer="ik_max_word")
    class_diff = Keyword()
    class_stu = Integer()
    class_des = Text(analyzer="ik_max_word")
    class_url = Keyword()
    class_type = Keyword()

    class Meta:
        index = "mooc"
        doc_type = "class_info"


if __name__ == "__main__":
    AnswerType.init()
    ArticleType.init()
    MoocType.init()

