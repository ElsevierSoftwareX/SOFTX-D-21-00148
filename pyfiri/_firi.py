import xarray as _xr
import os as _os


class _firi2018:
    data = None

    @staticmethod
    def get_data():
        if _firi2018.data is None:
            _firi2018.data = _get_firi2018_dataarray()
        return _firi2018.data.copy(deep=True)


def _get_firi2018_dataarray():
    _path = _os.path.join(_os.path.dirname(_os.path.abspath(__file__))
                          , "_ext", "_data", "firi2018ed2.nc")
    return _xr.load_dataarray(_path)
