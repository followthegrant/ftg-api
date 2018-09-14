from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, A

import settings
from serializers import ResultList


client = Elasticsearch(hosts=[':'.join((settings.ELASTIC['HOST'], settings.ELASTIC['PORT']))])


def search(q):
    if not q:
        return
    search = Search(using=client, index=settings.ELASTIC['INDEX']).query(
        'query_string',
        fields=[
            'author.name^3',
            'author.institutions^2',
            'disclosure^1.5',
            'paper.title',
            'paper.journal',
            'paper.publisher',
            'paper.tags',
            'paper.abstract'
        ],
        default_operator='AND',
        query=q
    )
    search.aggs.bucket('authors', A('terms', field='author.name.term'))
    search.aggs.bucket('institutions', A('terms', field='author.institutions.term'))
    search.aggs.bucket('tags', A('terms', field='paper.tags.term'))
    search.aggs.bucket('journals', A('terms', field='paper.journal.term'))
    search.aggs.bucket('publishers', A('terms', field='paper.publisher.term'))
    search.aggs.bucket('languages', A('terms', field='paper.lang'))
    search.aggs.bucket('years', A('date_histogram', field='paper.date', interval='year', format='yyyy'))
    return ResultList(search)
