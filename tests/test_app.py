
import json
import falcon
from falcon import testing
import pytest
from look.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_list_images(client):
    doc = {
        "images": [
            {
                "href": "/images/abc.png"
            }
        ]
    }

    response = client.simulate_get('/images')
    result_doc = response.content

    doc = json.dumps(doc)

    assert result_doc.decode() == doc
    assert response.status == falcon.HTTP_OK
