from core import EventManager
from core import Log

import json

class Module:
    def __init__(self):
        EventManager.bind('security_alert', self.__event_security_alert)

    def __event_security_alert(self, data):

        if 'level' in data and data['level'] in [
            'crash',
            'critical',
            'debug',
            'error',
            'info',
            'warning'
        ]:
            handle = getattr(Log, data['level'])

        else:
            handle = Log.error

        if not 'message' in data:
            data['message'] = 'Unknown'

        if not 'tags' in data:
            data['tags'] = []

        handle(
            'Security alert: %s (raw: %s)' % (
                data['message'],
                json.dumps(data)
            ),
            data['tags']
        )

