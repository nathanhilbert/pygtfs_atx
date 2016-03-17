from pygtfs import Schedule
from pygtfs import append_feed, delete_feed, overwrite_feed, list_feeds
from .base import GTFSSetup



class TestLoadingAbility(GTFSSmallSetup):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_routes( self ):
        self.assertEqual( self.schedule.routes[0].route_id, "20" )

    def test_services( self ):
        assert "4985f2fd-e65f-401a-be65-ed8bd2a9acdd" in self.schedule.services

    def test_stops( self ):
        assert "3281" in self.schedule.stops
        assert len(self.schedule.stops) == 409


        # def test_route_trips( self ):
        #   self.assertEqual( [tr.trip_id for tr in self.schedule.routes[0].trips],
        #     [u'AB1', u'AB2'] )

        # def test_trip_stop_times( self ):
        #   self.assertEqual( [(st.arrival_time if st.arrival_time else None,
        #                       st.departure_time if st.departure_time else None) for st in self.schedule.routes[0].trips[0].stop_times],
        #                       [(datetime.timedelta(0, 28800), datetime.timedelta(0, 28800)),
        #                        (datetime.timedelta(0, 29400), datetime.timedelta(0, 29700))])

        # def test_service_trips( self ):
        #   self.assertEqual([tr.trip_id for tr in self.schedule.services[1].trips],
        #                    [u'AAMV1', u'AAMV2', u'AAMV3', u'AAMV4'])

        # def test_stop_stop_times( self ):
        #   self.assertEqual([(st.arrival_time,st.departure_time) for st in self.schedule.stops[0].stop_times],
        #                    [(datetime.timedelta(0, 33600), datetime.timedelta(0, 33600)),
        #                     (datetime.timedelta(0, 39600), datetime.timedelta(0, 39600))])

        # def test_agencies( self ):
        #   self.assertEqual( [ag.agency_id for ag in self.schedule.agencies],
        #     [u'DTA'] )

        # def test_agency_routes( self ):
        #   self.assertEqual([rt.route_id for rt in self.schedule.agencies[0].routes],
        #                    [u'AAMV', u'AB', u'BFC', u'CITY', u'STBA'])

        # def test_trips_bikes_allowed(self):
        #   for t in self.schedule.trips:
        #     self.assertIsNone(t.bikes_allowed)
        #   t = self.schedule.trips[0]
        #   t.bikes_allowed = 0
        #   t.bikes_allowed = 1
        #   t.bikes_allowed = 2
        #   with self.assertRaises(AssertionError):
        #     t.bikes_allowed = 3
        #   with self.assertRaises(AssertionError):
        #     t.bikes_allowed = -1
        #   self.assertEqual(t.bikes_allowed, 2)
