import settings


def SearchHit(hit):
    return {k: v for k, v in hit.to_dict().items() if k not in settings.EXCLUDE_FIELDS}


def AggBucket(agg):
    return [{
        'name': b.get('key_as_string', b['key']),
        'count': b['doc_count']
    } for b in agg['buckets']]


def ResultList(search, page=None):
    s = search[:settings.PAGINATION]
    res = s.execute()
    return {
        'total': res.hits.total,
        'disclosures': [SearchHit(h) for h in res.hits],
        'facets': {
            k: AggBucket(v) for k, v in res.aggs.to_dict().items()
        }
    }
