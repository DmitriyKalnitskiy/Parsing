import requests
import json
def parserMvideo():
    cookies = {
        '__lhash_': 'a89b4e7180ed06dd2a11905d33d4a386',
        'MVID_CATALOG_NEW': 'true',
        'MVID_CHAT_VERSION': '6.6.0',
        'MVID_CITY_ID': 'CityCZ_9909',
        'MVID_FAVORIT_NEW': 'true',
        'MVID_FILTER_CODES': 'true',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_KLADR_ID': '5500000100000',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_PROMO_PAGES_ON_2': 'true',
        'MVID_REGION_ID': '30',
        'MVID_REGION_SHOP': 'S935',
        'MVID_SERVICE_AVLB': 'true',
        'MVID_TIMEZONE_OFFSET': '6',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'mindboxDeviceUUID': 'bbcbbf02-77c3-40e1-95ec-1162029d8fef',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22bbcbbf02-77c3-40e1-95ec-1162029d8fef%22%7D',
        '_ym_uid': '171129471679938942',
        '_ym_d': '1711294716',
        '_ga': 'GA1.1.523099207.1711294716',
        'admitad_uid': '---autotargeting',
        'utm_term': '---autotargeting',
        '__cpatrack': 'yandex_cpc',
        '__sourceid': 'yandex',
        '__allsource': 'yandex',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'f4160055-be2e-41ea-83f6-222b47e94b03',
        'flocktory-uuid': 'bfccfde0-baec-43d2-add7-0f43635c0033-9',
        'tmr_lvid': '9ebc00bb8004cefbaf3882bf1b29a06e',
        'tmr_lvidTS': '1711294719991',
        'advcake_session_id': '57f1aace-7be3-cd31-1f66-cff80338d4b3',
        'advcake_utm_partner': 'cn%3Amg_tk_all_p_omsk%7Ccid%3A82508041',
        'advcake_click_id': '',
        'uxs_uid': '96d57e50-e9f4-11ee-b14b-89eb75781738',
        'afUserId': '63ad0423-e630-4129-88e0-e64fc4ddbc59-p',
        'AF_SYNC': '1711294721191',
        '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025D5"}',
        'adid': '171129472269163',
        'MVID_GUEST_ID': '23688133413',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'deviceType': 'desktop',
        '_ym_isad': '2',
        'MVID_GROUP_BY_QUALITY': 'true',
        'MVID_TYP_CHAT': 'true',
        'JSESSIONID': 'vdmQmGmRDmPzpBByN632SxFkhChvJwzCT6M9XJnqcpDPn1P3hj1K!-230998832',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '2953108490.20480.0000',
        'bIPs': '-1323973254',
        'CACHE_INDICATOR': 'true',
        'MVID_GTM_BROWSER_THEME': '1',
        'SMSError': '',
        'authError': '',
        '_sp_ses.d61c': '*',
        'advcake_track_id': '77928be7-3ea1-84ce-4ca4-26bffa22c7c2',
        'advcake_utm_webmaster': 'ph%3A50982827380%7Cre%3A50982827380%7Ccid%3A82508041%7Cgid%3A5424449836%7Caid%3A15981494448%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A66%7C%25D0%259E%25D0%25BC%25D1%2581%25D0%25BA',
        'BIGipServeratg-ps-prod_tcp80_clone': '2953108490.20480.0000',
        'MVID_ENVCLOUD': 'prod2',
        'MVID_AB_PERSONAL_RECOMMENDS': 'true',
        'MVID_AB_UPSALE': 'true',
        'MVID_ACCESSORIES_PDP_BY_RANK': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_CASCADE_CMN': 'true',
        'MVID_CREDIT_DIGITAL': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_DISPLAY_ACCRUED_BR': 'true',
        'MVID_DISPLAY_PERS_DISCOUNT': 'true',
        'MVID_EMPLOYEE_DISCOUNT': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_NEW_CHAT_PDP': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PODELI_PDP': 'true',
        'MVID_SERVICES': '111',
        'MVID_SINGLE_CHECKOUT': 'true',
        'MVID_SP': 'true',
        '__hash_': '9227012da978c6a57772fe8ad94e6ef9',
        '_ym_visorc': 'w',
        'session': '1',
        '__SourceTracker': 'yandex.ru__organic',
        'admitad_deduplication_cookie': 'yandex.ru__organic',
        'customer_email': 'null',
        'advcake_track_url': '%3D202403255xw3RlApgvTNq0eXCxsu5ak6UBzszqxqQdv5jR7v0mM%2BfGaLJVucWu606rn03fS7HGq0HOfYGcuPdbq9hKFj4CHYG8yX7Ca%2BX%2BGkDAZzo1cpB8V89tRWBWRP9Bzb13ot2aeaPvXIBMMwyOhH4WZiCUqKmw3N2BUt97jAGp3ELHvxlEyDHyQ%2BElLQCiwCTAP%2BDMd%2F9C%2FGwyRDbfh6RwEZ122vl%2FBM%2BJNRK5j7UWBCmoGCjtBPQGvxQ7Fi115veU390JaCvNNQ3jvxmfXLMmRp%2BHtdKNSFjAGUsQmO2LrkbPIsgvqWOxbQt4Hr%2BmvNZlZFOo5yLHx64w72U3CiseUMo7pEWJLRt8slZs2n9kWm%2BQPHduJ8bsCa6a6LZYXoU5XCN34JqfvYe0Dslt8PgHX2BXV3jgzaG0E58F62NzKkv6SEtkz1DdEyo3CUZ6zZc2uI9iWrcepVsA%2FDsGER%2FqzgOYMRDPveDeIBKM0EjQngp82CaD%2F4TuUIAJSw1r67kpGx7tyTXHf1XNHRV1o7K%2BseuMFJj52ksHg1%2FsLinqC19wj5FPr2S7X3vEQ431nxud7IHco4IvDFipkExUHe5k2zyDQHbKbTCAjCeRQWB2Zb7lWKHLX6BKRS76s%2BZU2D6wM%2FMCS9k0s7z9KQEMYTqg8v0MI8HIz%2FNmuT%2BpBvRTtqrbQqrOWVeDdiVvWWiC0eYW282%2FuNoavBelC0EIWKh89Im7cVXvzhMNBv2VeYH4D8e2Ue%2F7VZvZt2xMl4PF7HdJ9UHfnKc%2BdhXlQzaBlaJL1PS8w1vUZcd%2F9AvdiuhyooUxmqAI03AkLFQ32d0EHW%2FQtq%2F%2F2ADu2U6TPEUTzbf2tQI1%2FqK0JVGoMSsFrtn4V8Uqj2nW6%2FP7rY4BGwkHmGhf8xg6yqBQfp5GOl5FrQC36VTe5IY4vARJzZmAt0IrMQdqkSSHyyDh0ZQGJcmmzwfz4tG%2B6JuKxdnjr%2BAfhl1y0fFH6fQS3VzCoqSXY7TwGzlUUTqL1j0Xa2Ytnf2OrATMpQw%2BIc3m%2FaimfW',
        '_gp100025D5': '{"hits":9,"vc":1,"ac":1,"a6":1}',
        'tmr_detect': '0%7C1711550906510',
        '_sp_id.d61c': '8e9b640b-ef84-440d-b740-83e57ef22059.1711294715.4.1711550912.1711519438.553251db-fa55-4196-a7a8-fd6faa383403.8e36a282-77cc-4acc-9a9d-b21910528b3d.3a12c5fc-abbf-4f5b-a3bd-ce5fcdcf6b2e.1711548053470.66',
        'gsscgib-w-mvideo': 'IvKbeYZVotF9Kjm/YcaMy7vyCM7RN2SN2ma755YxGAJcl/Zp3r/+sa5dkxex7lqCy61pdkszYi4xasI3TZN7kBHd7WycY/3ljbtmMmKmY51JYdHZXsknOmS5kUZljNrmviApg3/tp7TS5F8YcDEwKc7j8GucNdPt22ZqjAK2DfGAbUn90nT/VWpicMXHO/M/9MioTZajh196h4/Wvs9sDRhkmv4RBpCWpH9VNhtEPnAgIG/UZh8Mp0p70etoJQ==',
        'gsscgib-w-mvideo': 'IvKbeYZVotF9Kjm/YcaMy7vyCM7RN2SN2ma755YxGAJcl/Zp3r/+sa5dkxex7lqCy61pdkszYi4xasI3TZN7kBHd7WycY/3ljbtmMmKmY51JYdHZXsknOmS5kUZljNrmviApg3/tp7TS5F8YcDEwKc7j8GucNdPt22ZqjAK2DfGAbUn90nT/VWpicMXHO/M/9MioTZajh196h4/Wvs9sDRhkmv4RBpCWpH9VNhtEPnAgIG/UZh8Mp0p70etoJQ==',
        'fgsscgib-w-mvideo': 'Dlkz97756e6d96f93b1ff3482e8faaa3dca82cfc',
        'fgsscgib-w-mvideo': 'Dlkz97756e6d96f93b1ff3482e8faaa3dca82cfc',
        'gsscgib-w-mvideo': 'y7OkS7m/43X+9WiPDCsDyPLOTmQ3trJOhhcXHUOFlU7DbM9RuHDE/ezLJ3/udRRmVNKNH9wnPMhFuv4hunSLVt+l43V/q3okGJzwqZMdfEN7+U8WQ7CNw6+w8V1mclXf6ZITt419GzBnwIuGzx7K/OGIaOLhmTX9tsm4W+fofmxn6hXbE5W2rP0IQorIcIiewbuLF7p1JHrs8W4y3KZGReNBCylS+AnO9vVOnVLvsWpnDWTyRn0L6gEGCH++7Q==',
        'cfidsgib-w-mvideo': 'GazzuyQbQhHNHqAobXqySHk5BO3Xrw/iXnC41ZbOvlfrbapEbKLzsqIjdSaCBscCmVgi7qR8wNmU4uQkEm/DhksRC1gnYsG8jGf6I7huwmDbRVnX2oKJJ7y2OZq0QlLWM5h3OPa6CjeN7K+m6pqmYxTzdOHb+EjKZSG6iQ==',
        '_ga_BNX5WPP3YK': 'GS1.1.1711548053.4.1.1711550956.5.0.0',
        '_ga_CFMZTSS5FM': 'GS1.1.1711548053.4.1.1711550956.0.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'baggage': 'sentry-environment=production,sentry-release=release_24_3_3(6394),sentry-public_key=ae7d267743424249bfeeaa2e347f4260,sentry-trace_id=d967f2b3cfa145fab1d976283c351dbf,sentry-sample_rate=0.5,sentry-transaction=%2F**%2F,sentry-sampled=false',
        # 'cookie': '__lhash_=a89b4e7180ed06dd2a11905d33d4a386; MVID_CATALOG_NEW=true; MVID_CHAT_VERSION=6.6.0; MVID_CITY_ID=CityCZ_9909; MVID_FAVORIT_NEW=true; MVID_FILTER_CODES=true; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_KLADR_ID=5500000100000; MVID_NEW_LK_OTP_TIMER=true; MVID_PROMO_PAGES_ON_2=true; MVID_REGION_ID=30; MVID_REGION_SHOP=S935; MVID_SERVICE_AVLB=true; MVID_TIMEZONE_OFFSET=6; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; mindboxDeviceUUID=bbcbbf02-77c3-40e1-95ec-1162029d8fef; directCrm-session=%7B%22deviceGuid%22%3A%22bbcbbf02-77c3-40e1-95ec-1162029d8fef%22%7D; _ym_uid=171129471679938942; _ym_d=1711294716; _ga=GA1.1.523099207.1711294716; admitad_uid=---autotargeting; utm_term=---autotargeting; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=f4160055-be2e-41ea-83f6-222b47e94b03; flocktory-uuid=bfccfde0-baec-43d2-add7-0f43635c0033-9; tmr_lvid=9ebc00bb8004cefbaf3882bf1b29a06e; tmr_lvidTS=1711294719991; advcake_session_id=57f1aace-7be3-cd31-1f66-cff80338d4b3; advcake_utm_partner=cn%3Amg_tk_all_p_omsk%7Ccid%3A82508041; advcake_click_id=; uxs_uid=96d57e50-e9f4-11ee-b14b-89eb75781738; afUserId=63ad0423-e630-4129-88e0-e64fc4ddbc59-p; AF_SYNC=1711294721191; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; adid=171129472269163; MVID_GUEST_ID=23688133413; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=false; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=false; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; deviceType=desktop; _ym_isad=2; MVID_GROUP_BY_QUALITY=true; MVID_TYP_CHAT=true; JSESSIONID=vdmQmGmRDmPzpBByN632SxFkhChvJwzCT6M9XJnqcpDPn1P3hj1K!-230998832; flacktory=no; BIGipServeratg-ps-prod_tcp80=2953108490.20480.0000; bIPs=-1323973254; CACHE_INDICATOR=true; MVID_GTM_BROWSER_THEME=1; SMSError=; authError=; _sp_ses.d61c=*; advcake_track_id=77928be7-3ea1-84ce-4ca4-26bffa22c7c2; advcake_utm_webmaster=ph%3A50982827380%7Cre%3A50982827380%7Ccid%3A82508041%7Cgid%3A5424449836%7Caid%3A15981494448%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A66%7C%25D0%259E%25D0%25BC%25D1%2581%25D0%25BA; BIGipServeratg-ps-prod_tcp80_clone=2953108490.20480.0000; MVID_ENVCLOUD=prod2; MVID_AB_PERSONAL_RECOMMENDS=true; MVID_AB_UPSALE=true; MVID_ACCESSORIES_PDP_BY_RANK=true; MVID_ALFA_PODELI_NEW=true; MVID_CASCADE_CMN=true; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_DISPLAY_ACCRUED_BR=true; MVID_DISPLAY_PERS_DISCOUNT=true; MVID_EMPLOYEE_DISCOUNT=true; MVID_FILTER_TOOLTIP=1; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_NEW_CHAT_PDP=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PODELI_PDP=true; MVID_SERVICES=111; MVID_SINGLE_CHECKOUT=true; MVID_SP=true; __hash_=9227012da978c6a57772fe8ad94e6ef9; _ym_visorc=w; session=1; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; customer_email=null; advcake_track_url=%3D202403255xw3RlApgvTNq0eXCxsu5ak6UBzszqxqQdv5jR7v0mM%2BfGaLJVucWu606rn03fS7HGq0HOfYGcuPdbq9hKFj4CHYG8yX7Ca%2BX%2BGkDAZzo1cpB8V89tRWBWRP9Bzb13ot2aeaPvXIBMMwyOhH4WZiCUqKmw3N2BUt97jAGp3ELHvxlEyDHyQ%2BElLQCiwCTAP%2BDMd%2F9C%2FGwyRDbfh6RwEZ122vl%2FBM%2BJNRK5j7UWBCmoGCjtBPQGvxQ7Fi115veU390JaCvNNQ3jvxmfXLMmRp%2BHtdKNSFjAGUsQmO2LrkbPIsgvqWOxbQt4Hr%2BmvNZlZFOo5yLHx64w72U3CiseUMo7pEWJLRt8slZs2n9kWm%2BQPHduJ8bsCa6a6LZYXoU5XCN34JqfvYe0Dslt8PgHX2BXV3jgzaG0E58F62NzKkv6SEtkz1DdEyo3CUZ6zZc2uI9iWrcepVsA%2FDsGER%2FqzgOYMRDPveDeIBKM0EjQngp82CaD%2F4TuUIAJSw1r67kpGx7tyTXHf1XNHRV1o7K%2BseuMFJj52ksHg1%2FsLinqC19wj5FPr2S7X3vEQ431nxud7IHco4IvDFipkExUHe5k2zyDQHbKbTCAjCeRQWB2Zb7lWKHLX6BKRS76s%2BZU2D6wM%2FMCS9k0s7z9KQEMYTqg8v0MI8HIz%2FNmuT%2BpBvRTtqrbQqrOWVeDdiVvWWiC0eYW282%2FuNoavBelC0EIWKh89Im7cVXvzhMNBv2VeYH4D8e2Ue%2F7VZvZt2xMl4PF7HdJ9UHfnKc%2BdhXlQzaBlaJL1PS8w1vUZcd%2F9AvdiuhyooUxmqAI03AkLFQ32d0EHW%2FQtq%2F%2F2ADu2U6TPEUTzbf2tQI1%2FqK0JVGoMSsFrtn4V8Uqj2nW6%2FP7rY4BGwkHmGhf8xg6yqBQfp5GOl5FrQC36VTe5IY4vARJzZmAt0IrMQdqkSSHyyDh0ZQGJcmmzwfz4tG%2B6JuKxdnjr%2BAfhl1y0fFH6fQS3VzCoqSXY7TwGzlUUTqL1j0Xa2Ytnf2OrATMpQw%2BIc3m%2FaimfW; _gp100025D5={"hits":9,"vc":1,"ac":1,"a6":1}; tmr_detect=0%7C1711550906510; _sp_id.d61c=8e9b640b-ef84-440d-b740-83e57ef22059.1711294715.4.1711550912.1711519438.553251db-fa55-4196-a7a8-fd6faa383403.8e36a282-77cc-4acc-9a9d-b21910528b3d.3a12c5fc-abbf-4f5b-a3bd-ce5fcdcf6b2e.1711548053470.66; gsscgib-w-mvideo=IvKbeYZVotF9Kjm/YcaMy7vyCM7RN2SN2ma755YxGAJcl/Zp3r/+sa5dkxex7lqCy61pdkszYi4xasI3TZN7kBHd7WycY/3ljbtmMmKmY51JYdHZXsknOmS5kUZljNrmviApg3/tp7TS5F8YcDEwKc7j8GucNdPt22ZqjAK2DfGAbUn90nT/VWpicMXHO/M/9MioTZajh196h4/Wvs9sDRhkmv4RBpCWpH9VNhtEPnAgIG/UZh8Mp0p70etoJQ==; gsscgib-w-mvideo=IvKbeYZVotF9Kjm/YcaMy7vyCM7RN2SN2ma755YxGAJcl/Zp3r/+sa5dkxex7lqCy61pdkszYi4xasI3TZN7kBHd7WycY/3ljbtmMmKmY51JYdHZXsknOmS5kUZljNrmviApg3/tp7TS5F8YcDEwKc7j8GucNdPt22ZqjAK2DfGAbUn90nT/VWpicMXHO/M/9MioTZajh196h4/Wvs9sDRhkmv4RBpCWpH9VNhtEPnAgIG/UZh8Mp0p70etoJQ==; fgsscgib-w-mvideo=Dlkz97756e6d96f93b1ff3482e8faaa3dca82cfc; fgsscgib-w-mvideo=Dlkz97756e6d96f93b1ff3482e8faaa3dca82cfc; gsscgib-w-mvideo=y7OkS7m/43X+9WiPDCsDyPLOTmQ3trJOhhcXHUOFlU7DbM9RuHDE/ezLJ3/udRRmVNKNH9wnPMhFuv4hunSLVt+l43V/q3okGJzwqZMdfEN7+U8WQ7CNw6+w8V1mclXf6ZITt419GzBnwIuGzx7K/OGIaOLhmTX9tsm4W+fofmxn6hXbE5W2rP0IQorIcIiewbuLF7p1JHrs8W4y3KZGReNBCylS+AnO9vVOnVLvsWpnDWTyRn0L6gEGCH++7Q==; cfidsgib-w-mvideo=GazzuyQbQhHNHqAobXqySHk5BO3Xrw/iXnC41ZbOvlfrbapEbKLzsqIjdSaCBscCmVgi7qR8wNmU4uQkEm/DhksRC1gnYsG8jGf6I7huwmDbRVnX2oKJJ7y2OZq0QlLWM5h3OPa6CjeN7K+m6pqmYxTzdOHb+EjKZSG6iQ==; _ga_BNX5WPP3YK=GS1.1.1711548053.4.1.1711550956.5.0.0; _ga_CFMZTSS5FM=GS1.1.1711548053.4.1.1711550956.0.0.0',
        'referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=iphone-914',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'd967f2b3cfa145fab1d976283c351dbf-80a0f4f9317d4c34-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
        'x-set-application-id': '72de9f33-22f4-4bff-98dc-32fd9ac9dd48',
    }

    params = {
        'categoryId': '205',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJjYXRlZ29yeSIsIiIsImlwaG9uZS05MTQiXQ==',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
            ],
            'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()

    productsIds = response.get('body').get('products')

    with open ('ProductsIds.json', 'w') as file:
        json.dump(productsIds, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': productsIds,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
        'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

    with open('Items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    productsIdsStr = ','.join(productsIds)

    params = {
        'productIds': productsIdsStr,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    itemsPrices = {}

    materiaPrice = response.get('body').get('materialPrices')

    for item in materiaPrice:
        itemId = item.get('price').get('productId')
        itemBasePrice = item.get('price').get('basePrice')

        itemsPrices[itemId] = {
            'itemBasePrice': itemBasePrice,
        }

    with open('ItemsPrices.json', 'w') as file:
        json.dump(itemsPrices, file, indent=4, ensure_ascii=False)
