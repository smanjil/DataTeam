
import json
import falcon

class Resource(object):
    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/abc.png'
                }
            ]
        }

        # create json representation
        resp.body = json.dumps(doc, ensure_ascii = False)

        # not required as default status returned by framework in 200
        resp.status = falcon.HTTP_200
