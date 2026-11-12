import json
from url_domain_extract import transform
def test_transform():
    value='EXAMPLE.COM/path'
    if True: result=transform(value)
    else: result=transform(json.loads(value))
    assert 'example.com' in json.dumps(result,ensure_ascii=False)
