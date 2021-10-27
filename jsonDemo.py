import requests



url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1631846341570&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'



head={
    "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

responce = requests.get(url,headers=head)
# print(responce.status_code)
print(responce.content.decode())