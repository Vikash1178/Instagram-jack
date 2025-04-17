import requests

def report_account(username):
    url = f'https://www.instagram.com/{username}/?__a=1'
    response = requests.get(url)
    if response.status_code == 200:
        user_id = response.json()['graphql']['user']['id']
        headers = {
            'user-agent': 'Instagram 155.0.0.37.107 Android (29/10; 320dpi; 720x1544; HUAWEI; STK-LX1; HWSTK-H)',
            'cookie': 'sessionid=YOUR_SESSION_ID; csrftoken=YOUR_CSRF_TOKEN;',
            'x-csrftoken': 'YOUR_CSRF_TOKEN',
            'x-instagram-ajax': 'YOUR_CSRF_TOKEN',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
            'source_name': '',
            'reason_id': '1',  # Select the reason for reporting (1 for spam, 2 for inappropriate content, etc.)
            'frx_context': '',
            'frx_tier_section_context': '',
            'is_not_shop': '',
            'is_more_like_this': 'false',
            'object_type': 'user',
            'object_id': user_id,
            'content