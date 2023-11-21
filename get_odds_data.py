import requests


def get_game_odds_data():

    headers = {
        'Accept': 'application/json, text/plain, */*',
        # game id is last bit of url
        'Referer': 'https://www.oddsportal.com/basketball/usa/nba-2021-2022/boston-celtics-golden-state-warriors-j3bM4Y8o/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Ijd4TWxWYzF4WjF5b0d5SE5uMFJEQ3c9PSIsInZhbHVlIjoiWUlYcEgyWU9uRkljRTFEVmVleWhYRkVpa2VmeklWSEZCejYrL3BSdlEwWEhaTmFSeEpERDVCdlgxNk1QNnVuQmx1RHVIaTVoNmRsa2V0ZHh0aFNpMDZaSGZqTFVsVEd1eStjc1JqNGQyVlBMVzhrS2tpalZNc0JQaFN0S2dCMmYiLCJtYWMiOiIzNmVhYjYwODM4M2YxNmQxYTliZjdjODZlZTJlYTM4MGQyYWMyODYyMTBjODVmYjdkYjRhNjk3NzM0Zjc4YzRmIiwidGFnIjoiIn0=',
    }
    # f"1-3-{game_id}-3-1-{}.dat"
    # 3-1 at the end indicates moneyline and FT including OT
    event_name = "1-3-j3bM4Y8o-3-1-yj7d2.dat"
    response = requests.get(
        f'https://www.oddsportal.com/feed/match-event/{event_name}', headers=headers)
    return response


def get_game_data():

    cookies = {
        'op_user_logout': '0',
        '_ga_5YY4JY41P1': 'GS1.1.1699589640.4.1.1699589766.60.0.0',
        '_sg_b_v': '8%3B68039%3B1699589641',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Nov+09+2023+20%3A14%3A57+GMT-0800+(Pacific+Standard+Time)&version=202309.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=265c2db0-d4f9-496e-8b12-ecbd04f5ec06&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CBG114%3A1&AwaitingReconsent=false&geolocation=US%3BCA',
        '_ga': 'GA1.1.1175153109.1699519884',
        'XSRF-TOKEN': 'eyJpdiI6ImJEaW42K0JyTEx2Wk9BeG9jZUQzTGc9PSIsInZhbHVlIjoiT2RWN1h3VXBJSTgvU3d3YWl5dlVTM0ZxaENZM3RiNk1RVWdXVzRSOUowaEp1RURwSmNPNnN2KzJJdndQbjZLeThLbzU4REpEWFdsOU1OMytNTlc3MXBrTWlJVVZhQzFEUmRMSVdmbDdUU0hKdU83aGc4QzNBM2JNMTFzUDk4L3YiLCJtYWMiOiIyYmRjOTAyZGU4MzMxNDYwODQxNDllOTMwZTMxNDE4ZmQ0MWM5N2YwMDM5ZDhjNjRiZDE2ZWMyMjM0OWY0N2ZhIiwidGFnIjoiIn0%3D',
        '_sg_b_p': '%2Fbasketball%2Fusa%2Fnba-2022-2023%2Fresults%2F%2C%2Fbasketball%2Fusa%2Fnba-2020-2021%2Fresults%2F%2C%2Fbasketball%2Fusa%2Fnba-2020-2021%2Fmilwaukee-bucks-phoenix-suns-ULD28jPK%2F%2C%2Fbasketball%2Fusa%2Fnba-2021-2022%2Fresults%2F%2C%2Fbasketball%2Fusa%2Fnba-2021-2022%2Fboston-celtics-golden-state-warriors-j3bM4Y8o%2F',
        'oddsportalcom_session': 'eyJpdiI6Ik45VXFGZ1grS1NXb0F4QzE2bDFRaGc9PSIsInZhbHVlIjoiQTc4NWQ2UjNIT2hUU3daYThCU3YxQ09PVUxDdktUOERBeUhheUVIU0dBd0VsaFNwdkdnRm0wU0Q1WC8vZmZmRjh3bW1tc202eTdrVlk2M1NXMjhncWFWa0ErQW1SRThYRXdXYUZDRjFUcll6Zjl3aVNNUlhtbW1pMlN0SmRhTVkiLCJtYWMiOiIxN2ZhYmQxNjhlYzI4M2QzMjUwNzkwNWMyZTRjMGFlNDQ5OWU4M2I0ODBkYmUwYzA5MGU2NDUwMTk4OGYzYTg2IiwidGFnIjoiIn0%3D',
        'op_user_cookie': '6515016553',
        'op_user_hash': 'e9bb1614178fb08bad6e9160faac8e7f',
        'op_user_time': '1699583061',
        'op_user_full_time_zone': '5',
        'op_user_login_hash': 'c7b1e093a493457f240e0cafb9ee3ad4',
        'op_user_login_id': '462563',
        'op_user_time_zone': '-8',
        'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6IjVDSmhyTjhFWlVFVnBEamcyeUV3U3c9PSIsInZhbHVlIjoia1dZd2xMUWlhZGtwR3FrckNRWC8yaEIvbDBkemZVRFRtTE5YVmVFaXVpOXdVTGdQMnpmcmJXT1JpeE5mVXVJN043NXpGb1NzS1duY2VHa0w5d3pkalhzSWpUUkhVanZIWk5xT3RldDBlTzFsVHMvZkh3KzhZWHlnakZzcU9zZXFTRENFdWRWUU12RHo3TzZrVERHNWRBPT0iLCJtYWMiOiIyZTU4YjZhY2Q5ZTQ0YjI0MjI2NmVkNjE3NDhlMDM4NzcwZmZiYzNmNTAxNThlNjljY2ZmOWYzMjJiYmQ2NzM3IiwidGFnIjoiIn0%3D',
        'OptanonAlertBoxClosed': '2023-11-10T01:05:20.005Z',
        '_sg_b_n': '1699519884977',
        'op_cookie-test': 'ok',
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'en-US,en;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Mode': 'cors',
        'Host': 'www.oddsportal.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
        'Referer': 'https://www.oddsportal.com/basketball/usa/nba-2021-2022/results/',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        # 'Cookie': 'op_user_logout=0; _ga_5YY4JY41P1=GS1.1.1699589640.4.1.1699589766.60.0.0; _sg_b_v=8%3B68039%3B1699589641; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Nov+09+2023+20%3A14%3A57+GMT-0800+(Pacific+Standard+Time)&version=202309.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=265c2db0-d4f9-496e-8b12-ecbd04f5ec06&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CBG114%3A1&AwaitingReconsent=false&geolocation=US%3BCA; _ga=GA1.1.1175153109.1699519884; XSRF-TOKEN=eyJpdiI6ImJEaW42K0JyTEx2Wk9BeG9jZUQzTGc9PSIsInZhbHVlIjoiT2RWN1h3VXBJSTgvU3d3YWl5dlVTM0ZxaENZM3RiNk1RVWdXVzRSOUowaEp1RURwSmNPNnN2KzJJdndQbjZLeThLbzU4REpEWFdsOU1OMytNTlc3MXBrTWlJVVZhQzFEUmRMSVdmbDdUU0hKdU83aGc4QzNBM2JNMTFzUDk4L3YiLCJtYWMiOiIyYmRjOTAyZGU4MzMxNDYwODQxNDllOTMwZTMxNDE4ZmQ0MWM5N2YwMDM5ZDhjNjRiZDE2ZWMyMjM0OWY0N2ZhIiwidGFnIjoiIn0%3D; _sg_b_p=%2Fbasketball%2Fusa%2Fnba-2022-2023%2Fresults%2F%2C%2Fbasketball%2Fusa%2Fnba-2020-2021%2Fresults%2F%2C%2Fbasketball%2Fusa%2Fnba-2020-2021%2Fmilwaukee-bucks-phoenix-suns-ULD28jPK%2F%2C%2Fbasketball%2Fusa%2Fnba-2021-2022%2Fresults%2F%2C%2Fbasketball%2Fusa%2Fnba-2021-2022%2Fboston-celtics-golden-state-warriors-j3bM4Y8o%2F; oddsportalcom_session=eyJpdiI6Ik45VXFGZ1grS1NXb0F4QzE2bDFRaGc9PSIsInZhbHVlIjoiQTc4NWQ2UjNIT2hUU3daYThCU3YxQ09PVUxDdktUOERBeUhheUVIU0dBd0VsaFNwdkdnRm0wU0Q1WC8vZmZmRjh3bW1tc202eTdrVlk2M1NXMjhncWFWa0ErQW1SRThYRXdXYUZDRjFUcll6Zjl3aVNNUlhtbW1pMlN0SmRhTVkiLCJtYWMiOiIxN2ZhYmQxNjhlYzI4M2QzMjUwNzkwNWMyZTRjMGFlNDQ5OWU4M2I0ODBkYmUwYzA5MGU2NDUwMTk4OGYzYTg2IiwidGFnIjoiIn0%3D; op_user_cookie=6515016553; op_user_hash=e9bb1614178fb08bad6e9160faac8e7f; op_user_time=1699583061; op_user_full_time_zone=5; op_user_login_hash=c7b1e093a493457f240e0cafb9ee3ad4; op_user_login_id=462563; op_user_time_zone=-8; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjVDSmhyTjhFWlVFVnBEamcyeUV3U3c9PSIsInZhbHVlIjoia1dZd2xMUWlhZGtwR3FrckNRWC8yaEIvbDBkemZVRFRtTE5YVmVFaXVpOXdVTGdQMnpmcmJXT1JpeE5mVXVJN043NXpGb1NzS1duY2VHa0w5d3pkalhzSWpUUkhVanZIWk5xT3RldDBlTzFsVHMvZkh3KzhZWHlnakZzcU9zZXFTRENFdWRWUU12RHo3TzZrVERHNWRBPT0iLCJtYWMiOiIyZTU4YjZhY2Q5ZTQ0YjI0MjI2NmVkNjE3NDhlMDM4NzcwZmZiYzNmNTAxNThlNjljY2ZmOWYzMjJiYmQ2NzM3IiwidGFnIjoiIn0%3D; OptanonAlertBoxClosed=2023-11-10T01:05:20.005Z; _sg_b_n=1699519884977; op_cookie-test=ok',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6ImJEaW42K0JyTEx2Wk9BeG9jZUQzTGc9PSIsInZhbHVlIjoiT2RWN1h3VXBJSTgvU3d3YWl5dlVTM0ZxaENZM3RiNk1RVWdXVzRSOUowaEp1RURwSmNPNnN2KzJJdndQbjZLeThLbzU4REpEWFdsOU1OMytNTlc3MXBrTWlJVVZhQzFEUmRMSVdmbDdUU0hKdU83aGc4QzNBM2JNMTFzUDk4L3YiLCJtYWMiOiIyYmRjOTAyZGU4MzMxNDYwODQxNDllOTMwZTMxNDE4ZmQ0MWM5N2YwMDM5ZDhjNjRiZDE2ZWMyMjM0OWY0N2ZhIiwidGFnIjoiIn0=',
    }

    params = {
        '_': '1699589768425',  # epoch time
    }

    response = requests.get(
        # 'https://www.oddsportal.com/ajax-sport-country-tournament-archive_/3/tpisHrh3/X220577834X24584X65536X0X134217728X0X0X0X0X0X0X0X10485760X134217729X512X1048578X0X0X1024X18464X131584X2304/1/0/',
        "https://www.oddsportal.com/basketball/usa/nba-2021-2022/results/",
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response.text
    # return response.json()
    


with open("game_data_test.html", "w") as f:
    f.write(get_game_data())
