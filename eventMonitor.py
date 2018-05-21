import appdaemon.plugins.hass.hassapi as hass

"""
Monitor events and output changes to the verbose_log. Nice for debugging purposes.
Arguments:
 - events: List of events to monitor
"""
class Monitor(hass.Hass):
    def initialize(self):
        events = self.args['events']

        for event in self.split_device_list(self.args["events"]):
            self.log('watching event "{}" for state changes'.format(event))
            self.listen_event(self.changed, event)

    def changed(self, event_name, data, kwargs):
        self.log(event_name + ': ' + str(data))