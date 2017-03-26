"""
Utils module that contains all business logic that should not be at model/view or controller level.
"""

class GPXReader(object):
    """
    GPX Reading class that uses gpxpy for reading stuff like:
    - routes in gpx file (amount)
    - lowest and highest points comparing to sea level (elevation)
        # Use http://www.gpsvisualizer.com/elevation for re-establishment of elevation if not properly assembled by android -application!
    - routes that looks like some animal ?? :D crazy ideas are the best!
    """
    pass
