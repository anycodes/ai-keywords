# 中文文本关键词提取

通过本应用，用户可以一键部署并体验基于 TF-IDF 算法和 Textrank 算法的中文文本关键词提取能力。

当完成应用部署之后，通过返回的域名，可以进行体验：

![图片alt](https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1650539997672_20220421111957889557.png)

关于接口：

路径：`/keywords`

入参： 
- Headers
    - `Content-type: application/json`
- Body
    - `text`: 要提取关键词的文本
    - `count`: 关键词个数
    - `type`: 提取算法类型，取值tfidf, textrank
    
测试：
```
import requests
import base64
def getResult(content, count, wtype):
    data = json.dumps({"text": content, "count": count, "type": wtype})
    txt = requests.post("http://ai-keywords.start-ai.1767215449378635.cn-chengdu.fc.devsapp.net/keywords", data=data,
                        headers={'Content-Type': 'application/json'})
    return txt.content.decode("utf-8")
print(getResult("文本", 5, "tfidf"))
```