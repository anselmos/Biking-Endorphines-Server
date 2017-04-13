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
        #pylint: disable=fixme
        # FIXME Check if this is best idea to leave parsing in constructor - in scope of performance
        # for now there is no better way I can find out.
        # This will go to issues.
        self.__file_handle = self.set_file_handle(file_name)
        self.__gpx_handle = self.parse_file()
        self.__tracks = self.__gpx_handle.tracks
        self.__routes = self.__gpx_handle.routes
        self.__waypoints = self.__gpx_handle.waypoints

    def get_gpx_handle(self):
        """
        Returns gpx handle
        """
        return self.__gpx_handle

    def set_file_handle(self, file_name):
        """
        Returns file handle
        """
        self.__file_handle = open(file_name)

    def get_file_handle(self):
        """
        Returns file handle
        """
        return self.__file_handle

    def set_gpx_handle(self, gpx_handle):
        """
        Sets gpx handle
        """
        self.__gpx_handle = gpx_handle

    def parse_file(self):
        """
        Parses file name into gpx handle
        """
        self.set_file_handle(gpxpy.parse(self.get_file_handle()))

    def get_track_points(self, item_nb=0):
        """
        Returns only first track points
        """
        points = []
        if len(self.__tracks) > 0 and len(self.__tracks) >= item_nb:
            for point in self.__tracks[item_nb].walk():
                points.append(point)
        return points

    def get_route_points(self, item_nb=0):
        """
        Returns route points
        """
        points = []
        if len(self.__routes) > 0 and len(self.__routes) >= item_nb:
            for point in self.__routes[item_nb].walk():
                points.append(point)
        return points

    def get_way_points(self, item_nb=0):
        """
        Returns way points
        """
        points = []
        if len(self.__waypoints) > 0 and len(self.__waypoints) >= item_nb:
            for point in self.__waypoints[item_nb].walk():
                points.append(point)
        return points

    def get_points(self, item_nb=0):
        """
        Returns Points from either route/track or waypoints.
        If there is more then one type then uses Track's as a default.

        Make assumption that there will be only one of each data_type
        i.e. only one track/route/waypoint.
        """
        if len(self.__tracks) > 0 and self.__tracks[item_nb].get_points_no() > 0:
            return self.get_track_points()
        elif len(self.__routes) > 0 and self.__routes[item_nb].get_points_no() > 0:
            return self.get_route_points()
        elif len(self.__waypoints) > 0 and self.__waypoints[item_nb].get_points_no() > 0:
            return self.get_way_points()
        else:
            return []

    def get_elevations(self):
        """
        Returns list of elevation per route list
        """
        elevations = []
        for point in self.get_points():
            #pylint: disable=fixme
            # TODO - not sure if this will work, but let's check:
            # This will check only first element from tupple that is a GPXTrackPoint,
            # But what if it's not TrackPoint but a WayPoint ??
            # will it be first element or second/third  ??
            elevations.append(point[0].elevation)

        return elevations

    def get_lowest_elevation(self):
        """
        Returns information about lowest elevation from route
        Returns None if not found any elevations!
        """
        return NotImplementedError()


    def animal_figure_route(self):
        """
        Uses Points to compare route with animal shapes.
        Returns information if this route looks similar to some animal or not.
        Returns Name of animal from enumeration or None if none animal found.
        """
        return NotImplementedError()


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
    pass
