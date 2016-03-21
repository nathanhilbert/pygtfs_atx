from pygtfs import Schedule
from pygtfs import append_feed, delete_feed, overwrite_feed, list_feeds

class GTFSSmallSetup(object):
    def __init__(self):
        self.schedule = Schedule(":memory:")
        append_feed(self.schedule, "test/data/atx_small" )


# class GTFSATXSetup(object):
#     def __init__(self):
#         self.schedule = Schedule(":memory:")
#         append_feed(self.schedule, "test/data/atx_small" )