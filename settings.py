# Scrapy settings for Qunar project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "Qunar"
SPIDER_MODULES = ["Qunar.spiders"]
NEWSPIDER_MODULE = "Qunar.spiders"
REDIRECT_ENABLED = False
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
             " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"#设置用户代理
ROBOTSTXT_OBEY = False#不遵守爬虫协议
DOWNLOAD_DELAY = 3#设置等待时间，降低爬虫频率
DEFAULT_REQUEST_HEADERS = {#引入用户代码，Cookie等设置请求头
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
   'Cookie':'SECKEY_ABVK=pciIOQLFUrpS14w033wgBETSwqAKn02mNpBngk+1hTw%3D; BMAP_SECKEY=wEkqtMJAGIXO8Zll54rQ8eD9ZTXQjX6COZ2eFdnznmfxBX-7BkW0QHkk2JuJJfHELEqe-aUVnsJIgOVP5nW2d4EYYA8w8a9s-1GrZBEqHZ5wY-imNp_F71JgwcGwQO4VdGPFmjdR5dFzBQVrV6IolEXXjzNeq-yEjsxMpMZTkmutTlTXKGkRXL4XLOZlWQvU; QN1=0000ef80306c58ba71a0951d; QN300=s%3Dbing; QN99=4763; QunarGlobal=10.66.42.199_-2c9240c1_18c020601c6_-779b|1700841524637; _i=VInJOADDZ-pq3O51YxVk1RWcdhqq; QN601=5195d7bef3bd9362263546af7a8ab1a5; QN48=0000f3002f1058ba71a81733; QN269=58C520A08AE211EE96D2FA163E763FD9; fid=b70d8d1a-ff47-4ec1-94ac-848c2f52ba9b; QN57=17009724662160.6570329759305302; QN205=s%3Dbing; HN1=v1192cf7380ad0bfe28d0b56c2a3e91e8b; HN2=qkzzcqgsrngkk; ctt_june=1683616182042##iK3wWK3wWhPwawPwa%3DjmVDjmXPfDaRXnXSHIXKWDX%3DDsXSa8WRiTX%3DXwERvmiK3siK3saKg8aKg8WKt%3DWKjOVuPwaUvt; QN621=1490067914133%252Ctestssong%3DDEFAULT%26fr%3Dtejia_inter_search; quinn=c51b76ae9ed8ed8962e547a570ca5128bd3596eec5a1ed7fff304849f83a38ea2389c2594cef6b413d6380bd57770186; QN277=s%3Dbing; ctf_june=1683616182042##iK3waKjNWhPwawPwasj8aD3AaS3AX2XnXSX%2BVRD%2BWs3OE2jsa2XnVPDAas3%2BiK3siK3saKg8aKg%3DVRP8aKa%2BauPwaUvt; cs_june=0bc7f90a047416308e4053925af0f25b57de51ee818fa7390f53182397a6a6ff1903b574ba839acc60b81c2803d03ae779bf3ba73f7c5b86d6746dedc568af80b17c80df7eee7c02a9c1a6a5b97c1179f1c4e159c7b7a221233bf32c89647a925a737ae180251ef5be23400b098dd8ca; ariaDefaultTheme=null; QN243=708; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=lFYyqyGMcTvwLP8Z92nh5pAg8DzcW1hE; QN163=0; Hm_lvt_15577700f8ecddb1a927813c81166ade=1701482320,1701647420,1702212652,1702260697; QN63=%E4%BA%9A%E6%B4%B2%7C%E5%8C%97%E7%BE%8E%E6%B4%B2%7C%E6%AC%A7%E6%B4%B2%7C%E6%96%B0%E5%8A%A0%E5%9D%A1%7C%E7%BE%8E%E5%9B%BD%7C%E6%97%A5%E6%9C%AC%7C%E5%90%8D%E8%83%9C%E5%8F%A4%E8%BF%B9%E7%83%AD%E9%97%A8%E6%8E%A8%E8%8D%90%7C%E5%9F%8E%E5%B8%82%E5%90%8D%E8%83%9C%E5%8F%A4%E8%BF%B9%E7%83%AD%E9%97%A8%E6%8E%A8%E8%8D%90%7C%E5%B9%BF%E5%B7%9E%E5%90%8D%E8%83%9C%E5%8F%A4%E8%BF%B9%E7%83%AD%E9%97%A8%E6%8E%A8%E8%8D%90%7C%E6%B7%B1%E5%9C%B3; QN71="MjAyLjEwNS45MS4yMzM65bm/5beeOjE="; QN67=15854%2C14709%2C32468%2C196642%2C4505%2C457260%2C8104%2C11895%2C513383%2C510498; _vi=aWQ7y8ly6OC_NwXfsCC7_cbmfmB1O6kClTeBe2rYW9JAEccX3LBhXV5M3zzYZYYE6nAfXRuI2XuE97IaKgZE1u_Ko4iZyW2vU9plpfa5J2xSqiUQb5A1gGYSBWyUSM8n5Rx7IkaX5FKji5oGFYkh40XVTzKmPg08HOdHJDK4E0-b; QN58=1702286604392%7C1702286604392%7C1; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1702286605; QN271=8751b098-0367-4cb7-9f4b-393d0e5079b2; QN267=0737134915eca6eaac; JSESSIONID=A81E200E208E30E25488BAF0BE3DE789; __qt=v1%7CVTJGc2RHVmtYMS9MS2pXN3djNGltL1lSSVlWcytPQ3FPa2R4TklxKzJueGlZSXUxeGhuM2NYZlNuZnRZWE5XYUUxQVdkekhzQXR1a3VIRmI2MU1KV3NzQVhOU2w1YWN5b1lVZmxCQXI1SldybVpmbW95Uk9QSkJ4K1FpNVMya2lnMTJvSCtYdk9tcmk0ODJoaDlKcGdUVExkMjlyVHBpS2pUeU9LOHMrUlJVPQ%3D%3D%7C1702286965987%7CVTJGc2RHVmtYMTg3SC9RVFFyYnAvTUZSTVE3SDFjK0pVQVJQWjNLTzBrcHF2TWZiTFVZQm1pWmllVXplVzBQZVJkdVA2QkhyZVBoWFNWNWl0a0w4NUE9PQ%3D%3D%7CVTJGc2RHVmtYMSt4NzhCSTBoVzgwNlJ1bXhLVDdyOTQrL1h6ZVh6cGNlcEJMcUFmVU9CZGFsR2s2RW4rUWNwVGRyWEY0N0hQOHZwL0ltdk5HczZWK2tXdGNtd1N1YmVoTlpZS0J0aHNyUXc4WTNaY0VCNDVXWVVURzFaWitpeGwxUzBURXlEWWh3ajhZRFhJY2N1aW5tWW56N0RHTTg4RWw3WWtlZll1SkxPd0JxYUdTc3dlU2VhdFNxRFM3cTJ4LzdpbGFxY0dibGRiOWNCd3owM0tLRGh4ZktKZGxrY0Y4MlFUcEUxazdnYjQ3M3ZwM0g3SVArQUFnSFJ4bXJJREFDaGhnQWs0aDREczJ2MUdHNmdPY3dNemtBVDZ6RDluM2FEcHlFNzZNWnB2ajAzWUt1QVQ2Q1Vyb0VzYi9GWE9NYi9jdHg4QlhxMHlSYTBLcHVobDhIV1NBdDFIOWhnU3pJRk9mc2YwWkFtblZLZTFNZElsRXRKeElwUDk1dWxpRUZYYzVlclhnK2FNNlBuamlCa2FYZEgwNTdMRGhyNEZuL1pQd3dCOVlzMWIvR3BkZm52eUFlTkZRQ3BIQkxObWZITnd0eXAzWFhybzdCdHNLMWx6NWk1VnNFbTZ5R1QrMjI0ODdaUUN5NFJ1MDk0dW5BOHV3TE90eHpyUERTaGc3UVRqck14KytRRVFyWCtzbWNEYnV6RHI1cmdVYVh3M1pQY3VSSTRCdStwa2x2Qkl4UDFQMEVhNzJrazlvQU0wOWJBTTlHNFljaEdmbFNBa0xQS3BNbldYNVZGT1JSM21jNXRVTWtLZGxlU1p1MjFyQUovZ205ZjAyT3JBVmlORlUvM2Rhd1RsVUN1QnZzR1ZRMkdSWjNvVUxCdUtFVTR4aTUxbGlnZDFpWWFiVDc2MnIvRnRPL2loWlh6eTVnOG40QVJSdzV6Z1lBMzF3bmlmenIvSk8zQ28yTDB1RnhNOStCUDV0UWtZaktEL2Q1blVBcG8vTVJZb2RQNzFsWTkw',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
ITEM_PIPELINES = {#打开存储通道
   "Qunar.pipelines.QunarPipeline": 300,
}
# FEED_URL='file:D:/trave1.csv'
# FEED_FORMAT='csv'
# FEED_EXPORT_FIELDS=['Title',
#                 'TravelLink',
#                 'Date'
#                 'Days',
#                 'Photo_Nums',
#                 'Fee',
#                 'People',
#                 'Places',
#                 'Views',
#                 'Love',
#                 'Comment']
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#    # 'Cookie':'QN1=0000ef80306c58ba71a0951d; QN300=s%3Dbing; QN99=4763; QunarGlobal=10.66.42.199_-2c9240c1_18c020601c6_-779b|1700841524637; _i=VInJOADDZ-pq3O51YxVk1RWcdhqq; QN601=5195d7bef3bd9362263546af7a8ab1a5; QN48=0000f3002f1058ba71a81733; QN269=58C520A08AE211EE96D2FA163E763FD9; fid=b70d8d1a-ff47-4ec1-94ac-848c2f52ba9b; QN57=17009724662160.6570329759305302; QN205=s%3Dbing; HN1=v1192cf7380ad0bfe28d0b56c2a3e91e8b; HN2=qkzzcqgsrngkk; ctt_june=1683616182042##iK3wWK3wWhPwawPwa%3DjmVDjmXPfDaRXnXSHIXKWDX%3DDsXSa8WRiTX%3DXwERvmiK3siK3saKg8aKg8WKt%3DWKjOVuPwaUvt; QN621=1490067914133%252Ctestssong%3DDEFAULT%26fr%3Dtejia_inter_search; quinn=c51b76ae9ed8ed8962e547a570ca5128bd3596eec5a1ed7fff304849f83a38ea2389c2594cef6b413d6380bd57770186; QN277=s%3Dbing; ctf_june=1683616182042##iK3waKjNWhPwawPwasj8aD3AaS3AX2XnXSX%2BVRD%2BWs3OE2jsa2XnVPDAas3%2BiK3siK3saKg8aKg%3DVRP8aKa%2BauPwaUvt; cs_june=0bc7f90a047416308e4053925af0f25b57de51ee818fa7390f53182397a6a6ff1903b574ba839acc60b81c2803d03ae779bf3ba73f7c5b86d6746dedc568af80b17c80df7eee7c02a9c1a6a5b97c1179f1c4e159c7b7a221233bf32c89647a925a737ae180251ef5be23400b098dd8ca; ariaDefaultTheme=null; QN243=708; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=lFYyqyGMcTvwLP8Z92nh5pAg8DzcW1hE; QN163=0; QN267=0737134915d5dde243; _vi=3jWqzH3j1cfdCkzX0Lc_K29m-zrTfy6a1mDVC5ppKDie6gfIu-6SENDSsXJEdEJJhxAaRKE-oL96-JnzUmOfi5F6R_OzADxhBfPiTBFZmjl3RehrKnWgi5kusMBjxsBsJxK1taSR1q7lRa0XwS_H7bBuhsLZGgxz1uOrOE6uZU35; QN58=1702269412046%7C1702269412046%7C1; QN271=7c5cffd8-15c7-4a49-b7d1-d6ae0e3c8cdf',
#    'Cookie':'SECKEY_ABVK=pciIOQLFUrpS14w033wgBETSwqAKn02mNpBngk+1hTw%3D; BMAP_SECKEY=wEkqtMJAGIXO8Zll54rQ8eD9ZTXQjX6COZ2eFdnznmfxBX-7BkW0QHkk2JuJJfHELEqe-aUVnsJIgOVP5nW2d4EYYA8w8a9s-1GrZBEqHZ5wY-imNp_F71JgwcGwQO4VdGPFmjdR5dFzBQVrV6IolEXXjzNeq-yEjsxMpMZTkmutTlTXKGkRXL4XLOZlWQvU; QN1=0000ef80306c58ba71a0951d; QN300=s%3Dbing; QN99=4763; QunarGlobal=10.66.42.199_-2c9240c1_18c020601c6_-779b|1700841524637; _i=VInJOADDZ-pq3O51YxVk1RWcdhqq; QN601=5195d7bef3bd9362263546af7a8ab1a5; QN48=0000f3002f1058ba71a81733; QN269=58C520A08AE211EE96D2FA163E763FD9; fid=b70d8d1a-ff47-4ec1-94ac-848c2f52ba9b; QN57=17009724662160.6570329759305302; QN205=s%3Dbing; HN1=v1192cf7380ad0bfe28d0b56c2a3e91e8b; HN2=qkzzcqgsrngkk; ctt_june=1683616182042##iK3wWK3wWhPwawPwa%3DjmVDjmXPfDaRXnXSHIXKWDX%3DDsXSa8WRiTX%3DXwERvmiK3siK3saKg8aKg8WKt%3DWKjOVuPwaUvt; QN621=1490067914133%252Ctestssong%3DDEFAULT%26fr%3Dtejia_inter_search; quinn=c51b76ae9ed8ed8962e547a570ca5128bd3596eec5a1ed7fff304849f83a38ea2389c2594cef6b413d6380bd57770186; QN277=s%3Dbing; ctf_june=1683616182042##iK3waKjNWhPwawPwasj8aD3AaS3AX2XnXSX%2BVRD%2BWs3OE2jsa2XnVPDAas3%2BiK3siK3saKg8aKg%3DVRP8aKa%2BauPwaUvt; cs_june=0bc7f90a047416308e4053925af0f25b57de51ee818fa7390f53182397a6a6ff1903b574ba839acc60b81c2803d03ae779bf3ba73f7c5b86d6746dedc568af80b17c80df7eee7c02a9c1a6a5b97c1179f1c4e159c7b7a221233bf32c89647a925a737ae180251ef5be23400b098dd8ca; ariaDefaultTheme=null; QN243=708; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=lFYyqyGMcTvwLP8Z92nh5pAg8DzcW1hE; QN163=0; Hm_lvt_15577700f8ecddb1a927813c81166ade=1701482320,1701647420,1702212652,1702260697; QN63=%E4%BA%9A%E6%B4%B2%7C%E5%8C%97%E7%BE%8E%E6%B4%B2%7C%E6%AC%A7%E6%B4%B2%7C%E6%96%B0%E5%8A%A0%E5%9D%A1%7C%E7%BE%8E%E5%9B%BD%7C%E6%97%A5%E6%9C%AC%7C%E5%90%8D%E8%83%9C%E5%8F%A4%E8%BF%B9%E7%83%AD%E9%97%A8%E6%8E%A8%E8%8D%90%7C%E5%9F%8E%E5%B8%82%E5%90%8D%E8%83%9C%E5%8F%A4%E8%BF%B9%E7%83%AD%E9%97%A8%E6%8E%A8%E8%8D%90%7C%E5%B9%BF%E5%B7%9E%E5%90%8D%E8%83%9C%E5%8F%A4%E8%BF%B9%E7%83%AD%E9%97%A8%E6%8E%A8%E8%8D%90%7C%E6%B7%B1%E5%9C%B3; QN71="MjAyLjEwNS45MS4yMzM65bm/5beeOjE="; QN67=15854%2C14709%2C32468%2C196642%2C4505%2C457260%2C8104%2C11895%2C513383%2C510498; _vi=aWQ7y8ly6OC_NwXfsCC7_cbmfmB1O6kClTeBe2rYW9JAEccX3LBhXV5M3zzYZYYE6nAfXRuI2XuE97IaKgZE1u_Ko4iZyW2vU9plpfa5J2xSqiUQb5A1gGYSBWyUSM8n5Rx7IkaX5FKji5oGFYkh40XVTzKmPg08HOdHJDK4E0-b; QN58=1702286604392%7C1702286604392%7C1; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1702286605; QN271=8751b098-0367-4cb7-9f4b-393d0e5079b2; QN267=0737134915eca6eaac; JSESSIONID=A81E200E208E30E25488BAF0BE3DE789; __qt=v1%7CVTJGc2RHVmtYMS9MS2pXN3djNGltL1lSSVlWcytPQ3FPa2R4TklxKzJueGlZSXUxeGhuM2NYZlNuZnRZWE5XYUUxQVdkekhzQXR1a3VIRmI2MU1KV3NzQVhOU2w1YWN5b1lVZmxCQXI1SldybVpmbW95Uk9QSkJ4K1FpNVMya2lnMTJvSCtYdk9tcmk0ODJoaDlKcGdUVExkMjlyVHBpS2pUeU9LOHMrUlJVPQ%3D%3D%7C1702286965987%7CVTJGc2RHVmtYMTg3SC9RVFFyYnAvTUZSTVE3SDFjK0pVQVJQWjNLTzBrcHF2TWZiTFVZQm1pWmllVXplVzBQZVJkdVA2QkhyZVBoWFNWNWl0a0w4NUE9PQ%3D%3D%7CVTJGc2RHVmtYMSt4NzhCSTBoVzgwNlJ1bXhLVDdyOTQrL1h6ZVh6cGNlcEJMcUFmVU9CZGFsR2s2RW4rUWNwVGRyWEY0N0hQOHZwL0ltdk5HczZWK2tXdGNtd1N1YmVoTlpZS0J0aHNyUXc4WTNaY0VCNDVXWVVURzFaWitpeGwxUzBURXlEWWh3ajhZRFhJY2N1aW5tWW56N0RHTTg4RWw3WWtlZll1SkxPd0JxYUdTc3dlU2VhdFNxRFM3cTJ4LzdpbGFxY0dibGRiOWNCd3owM0tLRGh4ZktKZGxrY0Y4MlFUcEUxazdnYjQ3M3ZwM0g3SVArQUFnSFJ4bXJJREFDaGhnQWs0aDREczJ2MUdHNmdPY3dNemtBVDZ6RDluM2FEcHlFNzZNWnB2ajAzWUt1QVQ2Q1Vyb0VzYi9GWE9NYi9jdHg4QlhxMHlSYTBLcHVobDhIV1NBdDFIOWhnU3pJRk9mc2YwWkFtblZLZTFNZElsRXRKeElwUDk1dWxpRUZYYzVlclhnK2FNNlBuamlCa2FYZEgwNTdMRGhyNEZuL1pQd3dCOVlzMWIvR3BkZm52eUFlTkZRQ3BIQkxObWZITnd0eXAzWFhybzdCdHNLMWx6NWk1VnNFbTZ5R1QrMjI0ODdaUUN5NFJ1MDk0dW5BOHV3TE90eHpyUERTaGc3UVRqck14KytRRVFyWCtzbWNEYnV6RHI1cmdVYVh3M1pQY3VSSTRCdStwa2x2Qkl4UDFQMEVhNzJrazlvQU0wOWJBTTlHNFljaEdmbFNBa0xQS3BNbldYNVZGT1JSM21jNXRVTWtLZGxlU1p1MjFyQUovZ205ZjAyT3JBVmlORlUvM2Rhd1RsVUN1QnZzR1ZRMkdSWjNvVUxCdUtFVTR4aTUxbGlnZDFpWWFiVDc2MnIvRnRPL2loWlh6eTVnOG40QVJSdzV6Z1lBMzF3bmlmenIvSk8zQ28yTDB1RnhNOStCUDV0UWtZaktEL2Q1blVBcG8vTVJZb2RQNzFsWTkw',
#    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "Qunar.middlewares.QunarSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "Qunar.middlewares.QunarDownloaderMiddleware": 543,
# }

DOWNLOADER_MIDDLEWARES = {
    # 关闭默认方法
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # 开启
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "Qunar.pipelines.QunarPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
# FEED_URL='file:D:/trave1.csv'
# FEED_FORMAT='csv'
# FEED_EXPORT_FIELDS=['Title',
#                 'TravelLink',
#                 'Date'
#                 'Days',
#                 'Photo_Nums',
#                 'Fee',
#                 'People',
#                 'Places',
#                 'Views',
#                 'Love',
#                 'Comment']