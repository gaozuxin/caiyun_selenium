import requests

# 获取网页源码
headers = {
    "Host":"cy.newssdk.com",
    "Cookie": "laravel_session=eyJpdiI6IkxkUWg0VmhNQ0M4ckVOUHBPa05LM3c9PSIsInZhbHVlIjoia0djcWhmXC9xbnJCV1lzQjNmK3RnTUt1MzJJQVJER0gzSkxLVll5Y01ienlMT1NmUkdVRWZBNmpjNXFTbkptdzAiLCJtYWMiOiJlYjcxMjE0MGZjOTZkY2JhZDZjODc3NDNiMzc1M2ZmZTQ4M2Y5NmQ0MTI1NzIyOGQwMmNhNTE5NzgzNTgwM2M5In0%3D",
    # "Content-type": "application/json",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",

}
r = requests.get("http://cy.newssdk.com/search", headers=headers)
print(r.text)


# 获取指定数据
data ={
        "message": "",
        "searchtype": None,
        "status": 0,
        "total": 91889,
        "li": [{
            "publish_time": "2018-12-06",
            "amountOfMoney": 15182629,
            "title": "\u5929\u9547\u53bf\u65b0\u5e73\u5821\u9547\u7b49\u516d\u4e61\u95472018\u5e74\u519c\u6751\u5371\u623f\u6539\u9020\u5de5\u7a0b\u65bd\u5de5\u62db\u6807\u63a7\u5236\u4ef7",
            "area": "\u5168\u56fd",
            "is_following": 1,
            "is_title": 1,
            "item_id": "695750809",
            "url": "\/detail?i=695750809"
        },
        {
            "is_following": 1,
            "amountOfMoney": 0,
            "is_title": 1,
            "title": "2018\u5e74\u5ffb\u5dde\u6d8c\u76c8\u73af\u5883\u5efa\u8bbe\u6709\u9650\u516c\u53f8\u571f\u5730\u5f00\u53d1\u6574\u6cbb\u9879\u76ee\u5ffb\u5e9c\u533a\u5170\u6751\u4e61\u3001\u5e84\u78e8\u9547\u3001\u8c46\u7f57\u9547\u571f\u5730\u6e05\u67e5\u3001\u52d8\u6d4b\u3001\u53ef\u884c\u6027\u7814\u7a76\u62a5\u544a\u3001\u8bbe\u8ba1\uff08\u5305\u62ec\u9884\u7b97\u7f16\u5236\uff09\u62db\u6807\u516c\u544a",
            "item_id": "624042908",
            "area": "\u5168\u56fd",
            "publish_time": "2018-12-06",
            "url": "\/detail?i=624042908"
        },
        {
            "is_following": 1,
            "publish_time": "2018-12-06",
            "item_id": "582165007",
            "title": "\u4e2d\u5171\u5927\u5e86\u5e02\u59d4\u515a\u6821\u590f\u51c9\u88ab\u53ca\u835e\u9ea6\u4fdd\u5065\u6795\u91c7\u8d2d\u590f\u51c9\u88ab\u53ca\u835e\u9ea6\u4fdd\u5065\u6795\u91c7\u8d2d\u4e2d\u6807\u516c\u544a\u4e2d\u6807\u516c\u793a",
            "is_title": 1,
            "area": "\u9ed1\u9f99\u6c5f",
            "amountOfMoney": 0,
            "url": "\/detail?i=582165007"
        },
        {
            "area": "\u5168\u56fd",
            "title": "\u56fd\u5bb6\u7edf\u8ba1\u5c40\u7b2c\u56db\u6b21\u5168\u56fd\u7ecf\u6d4e\u666e\u67e5\u5317\u4eac\u6570\u636e\u4e2d\u5fc3\u6570\u636e\u8bbe\u5907\u91c7\u8d2d\u9879\u76ee\u4e2d\u6807\u516c\u544a",
            "is_following": 1,
            "amountOfMoney": 0,
            "is_title": 1,
            "item_id": "582164907",
            "publish_time": "2018-12-06",
            "url": "\/detail?i=582164907"
        },
        {
            "amountOfMoney": 0,
            "title": "\u4e1c\u839e\u5e02\u5858\u53a6\u9547\u4eba\u6c11\u653f\u5e9c\u529e\u516c\u5ba4\u5858\u53a6\u9547\u653f\u5e9c\u4f1a\u8bae\u7cfb\u7edf\u6539\u9020\u91c7\u8d2d\u9879\u76ee\u516c\u5f00\u62db\u6807\u516c\u544a",
            "area": "\u5e7f\u4e1c",
            "is_title": 1,
            "is_following": 1,
            "publish_time": "2018-12-06",
            "item_id": "582165107",
            "url": "\/detail?i=582165107"
        },
        {
            "area": "\u6cb3\u5317",
            "item_id": "582165307",
            "title": "\u4e34\u897f\u53bf2018\u5e74\u68c9\u82b1\u7eff\u8272\u9ad8\u8d28\u9ad8\u6548\u521b\u5efa\u9879\u76ee\u62db\u6807\u516c\u544a",
            "publish_time": "2018-12-06",
            "is_title": 1,
            "amountOfMoney": 548000,
            "is_following": 1,
            "url": "\/detail?i=582165307"
        },
        {
            "area": "\u798f\u5efa",
            "publish_time": "2018-12-06",
            "item_id": "582165407",
            "is_title": 1,
            "is_following": 1,
            "title": "2018\u5e74\u957f\u6c40\u53bf\u571f\u58e4\u9178\u5316\u8015\u5730\u6cbb\u7406\u571f\u58e4\u8c03\u7406\u5242\u8d27\u7269\u7c7b\u91c7\u8d2d\u9879\u76ee\u62db\u6807\u516c\u544a",
            "amountOfMoney": 0,
            "url": "\/detail?i=582165407"
        },
        {
            "publish_time": "2018-12-06",
            "area": "\u5168\u56fd",
            "item_id": "582164807",
            "is_following": 1,
            "title": "\u590d\u65e6\u5927\u5b66\u9644\u5c5e\u80bf\u7624\u533b\u9662\u5168\u81ea\u52a8\u914d\u8840\u53ca\u8840\u578b\u5206\u6790\u4eea\u516c\u5f00\u62db\u6807\u516c\u544a",
            "amountOfMoney": 0,
            "is_title": 1,
            "url": "\/detail?i=582164807"
        },
        {
            "is_title": 1,
            "publish_time": "2018-12-06",
            "amountOfMoney": 0,
            "area": "\u5168\u56fd",
            "title": "\u4e2d\u5c71\u5927\u5b66\u56fe\u4e66\u99862019-2020\u5e74\u8fdb\u53e3\u539f\u7248\u62a5\u520a\u91c7\u8d2d\u9879\u76ee\u516c\u5f00\u62db\u6807\u516c\u544a",
            "item_id": "582164607",
            "is_following": 1,
            "url": "\/detail?i=582164607"
        },
        {
            "title": "\u590d\u65e6\u5927\u5b66\u9644\u5c5e\u80bf\u7624\u533b\u9662\u5168\u81ea\u52a8\u8840\u7ec6\u80de\u5206\u6790\u4eea\u516c\u5f00\u62db\u6807\u516c\u544a",
            "publish_time": "2018-12-06",
            "is_title": 1,
            "area": "\u5168\u56fd",
            "amountOfMoney": 0,
            "item_id": "695750909",
            "is_following": 1,
            "url": "\/detail?i=695750909"
        }],
        "page": None,
        "size": 10
    }
url1 ='http://cy.newssdk.com'
for index in range(len(data["li"])):
    print(data["li"][index]["title"])
    print(url1+data["li"][index]["url"][1:])