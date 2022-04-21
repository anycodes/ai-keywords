import bottle
import json
import jieba.analyse

@bottle.route('/')
def index():
    return bottle.template('./html/index.html')

@bottle.route('/keywords', method='POST')
def keywords():
    postData = json.loads(bottle.request.body.read().decode("utf-8"))
    type = postData.get("type", 'tfidf')
    text = postData.get("text", None)
    count = int(postData.get("count", 5))
    if not text:
        return {"error": "The text is required"}
    if type == 'tfidf':
        return {"keywords": jieba.analyse.extract_tags(sentence=text,topK=count,allowPOS=('ns','n'))}
    elif type == 'textrank':
        return {"keywords": jieba.analyse.textrank(text, topK=count, allowPOS=('ns','n'))}
    else:
        return {"error": "The value range of type is ['textrank', 'tfidf']"}

if __name__ == "__main__":
    bottle.run(host='0.0.0.0', debug=False, port=9000)
else:
    app = bottle.default_app()