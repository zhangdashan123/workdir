import re
from urllib.parse import quote, unquote

detail_url = 'https://travelads.koddi.com/TravelAdsService/v4/Hotels/TravelAdClickRedirect?trackingData=Cmp-WFkOh8Kva5MCgHv4sUz0A0ZCKQotj7Lt8Avq0KzY3faHDYbNkguXeNuH9+wnEASfKVInTjizGOyk2oYcjJnjxszzb1KkX9zUSMY5sAqdtJh4Ri0pQ1YTinR+apxfKWnyX26sY/M59265Wt5WiWs8EoX58kwUJNlqpaeX0k8Kpg9eRLJZZ+snellJM2zAJaYx8ZbiHrCjGM8y2LH38ETn+Ktf2ByfepIBHFLDsSODPqTUQNA4VuNr4Q+iuU9+dmUE3fm/A3WwgdHW5n5GZyd+5z+ja9yZPVUMAtMM/eOXSb0cDegiC8ulgfPuejv94utX2OkmRXs1C/olJXIeLre7Oa7LQ1U3afWUUirjJpIxT6kwKC62GdfbMW2n2TkfTXmO5cUkLUA+s4LodE19doSHCsYkpWd5gupf7jFxIrnUJ14fOUvPmQVqUjXtoLp+rAKa1SR2asaH5lW2XV+4j3iLhu0/4o6IF3ZO2yzR/gR8Ig2xYIW5aq8IxtvyynTxG3pCJM97Khz/K4rZcoxsEIS/LjGIyZT6IXmOtgnh3PTCg0rrMWyajkxxo212OXTOJaKFQW9El5NX4Ye4Vh/1Xg52l4U8suscBvCEbtXDNtoDINlkFlcP27CYkeaI+fszfRw4JYrb+CH8+SyrigPR0GIcTbz1bbsty2rF5sQ1I3FKxRXJse8v/VasvN3eZ837JiE0DP9y0B2491gsreNF8mcLI0BX90b4RSoZeK7MmAPNmSC5hVh0DgisqxeNmTI5R6VBax3Vn81VYI+ehJqyqxQOy5Iuyc6U9EwtB4vUNwoS3vUhrnzuADoQze/6HL/gvVStJPUcZoWECxpgKUpBCEus0QYTAgLERX3B9dlwhv2hmso2BmJqdxWKZtBnlSCoj/fO3Y4WI01/TKDl4S9My6q02iW3mSCOquLap4cUdTWVfpHbsjOKdFvTmD3muj1ntOcKhiEboQ45c+dMWU31xaolTRI0Ut+UEDQbM+emqrB84gq6TvNf1m+yaS02r9LO7UP3+NGEB7bNw29+peoerFTbGoulIIZC9//y34by5zmDnsUQALJuWdqTz4O9heWueIpzNx8VJK4J9MdA03CxTqSJOy0xZAE/LgUMIU/7z7Mq5ApiFxQ9xGwIHLHNiqhCcb7isU78CQAO/vE71dvyHebQaFX+HPuH8GROZiil3AlSV1w=&rank=2&testVersionOverride=9662.36494.0%2C13487.51625.0%2C14567.99990.0%2C11433.82360.1%2C24597.99990.0&destinationUrl=https%3A%2F%2Fwww.expedia.com%2FHotels-Four-Points-By-Sheraton-Hangzhou.h1774903.Hotel-Information%3Fchkin%3D2019%252F9%252F18%26chkout%3D2019%252F9%252F19%26rm1%3Da2%26hwrqCacheKey%3Dc5af0e72-ed39-4922-b542-66aefae94230HWRQ1568771097347%26cancellable%3Dfalse%26regionId%3D6084457%26vip%3Dfalse%26c%3Db998049f-391e-4789-915f-c785b2b511b7%26&candidateHmGuid=&beaconIssued=2019-09-18T01:44:58&slots=HSR_AA&position=[position]'
if 'https://travelads.koddi.com' in detail_url:
    detail_url = 'https://www.expedia.com' + detail_url.split('www.expedia.com')[-1].split('&candidateHmGuid')[0]
    print(detail_url)
    detail_url = unquote(detail_url)
    detail_url = unquote(detail_url)
    print('detail_url:', detail_url)
    regex = re.compile(r'chkin=(.*?)&chkout=(.*?)&', re.S)
    date_info = regex.findall(detail_url)
    print(date_info)