import json

input = """
{
    "shares": {
        "public": {
            "C0T8SE4AU": [
                {
                    "reply_users": [
                        "U061F7AUR"
                    ],
                    "reply_users_count": 1,
                    "reply_count": 1,
                    "ts": "1531763348.000001",
                    "thread_ts": "1531763273.000015",
                    "latest_reply": "1531763348.000001",
                    "channel_name": "cars",
                    "team_id": "T061EG9R6"
                }
            ]
        }
    },
    "channels": [
        "C0T8SE4AU"
    ],
    "groups": [],
    "ims": [],
    "has_rich_preview": false
}
"""

channel = "C0T8SE4AU"
channels = [channel]

def extract_ts_tuple(json_input, _channels):
    for _channel in _channels:
        print(_channel)
        shares = json_input['shares']['public'][_channel]

        #we're only intested in the message in #cars
        cars_share_ts = [share_info['ts'] for share_info in shares if share_info['channel_name'] == 'cars']

        if len(cars_share_ts) == 1:
            return _channel, cars_share_ts[0]
        else:
            return _channel, None


def test_enumerate():
    tesT_channels = [('mychannel1', '23133232.2123'), ('mychannel2', '23123123.1111111')]

    for idx, channel_id in enumerate(tesT_channels):
        print(idx)
        print(channel_id)
        print('::::::::::::::::::::;')
        channel, ts = channel_id
        print(channel)
        print(ts)




if __name__ == '__main__':

    json_input = json.loads(input)
    test_enumerate()
    # print(extract_ts_tuple(json_input, channels))


