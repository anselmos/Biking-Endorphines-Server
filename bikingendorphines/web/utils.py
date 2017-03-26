"""
Utils module that contains all business logic that should not be at model/view or controller level.
"""
import gpxpy

class GPXReader(object):
    """
    Class that is used for making tests with "super"
    Please refer to yt - Raymond Hettinger - Super considered super!
    """

    def __init__(self, file_name):
        """
        Constructor. Reads default information that can be read by gpx.
        """
        self.file_handle = open(file_name)
        # FIXME Check if this is best idea to leave parsing in constructor - in scope of performance
        self.gpx_handle = gpxpy.parse(self.file_handle)

        self.read_gpx_information()

    # TODO change it to individual read!
    def read_gpx_information(self):
        """
        Reads information from gpx file
        """
        # 3 loops ... o2? o3?
        for track in self.gpx_handle.tracks:
            for segment in track.segments:
                for point in segment.points:
                    print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

        for waypoint in self.gpx_handle.waypoints:
            print 'waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude)

        for route in self.gpx_handle.routes:
            print 'Route:'
            for point in route.points:
                print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)
                pass

    def get_routes(self):
        """
        Returns list of routes with it's coordinates.
        """
        return []

    def get_elevation(self, route):
        """
        Returns list of elevation per route list
        """
        return []


class EndomondoGPXReader(GPXReader):
    """
    Specific version of gps reader that is setup for endomondo gpx format.
    GPX Reading class that uses gpxpy for reading stuff like:
    - routes in gpx file (amount)
    - lowest and highest points comparing to sea level (elevation)
        # Use http://www.gpsvisualizer.com/elevation for 
        # re-establishment of elevation if not properly assembled by android -application!
    - routes that looks like some animal ?? :D crazy ideas are the best!
    """

    def __init__(self):
        """
        Constructor, will get information from mother.
        """
        pass
