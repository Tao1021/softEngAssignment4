from jsontosql.parse_Json import *
import sys
from nose.tools import *

def test_version():
    eq_(sys.version_info[0], 3, 'Python is not version 3')

def test_openJson():
    file = 'test_json.json'
    data = open_Json(file)
    ok_(data[0]["address"] == 'Smithfield North', 'Incorrect read input from first dict.')
    ok_(data[1]["number"] == 20, 'Incorrect read input from second dict.')