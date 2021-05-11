from pyfiri._firi import _firi2018


class firi2018:
    def __init__(self):
        self._firi_data = _firi2018.get_data()

    @staticmethod
    def license():
        """
        :return: the license notice the package is distributed under.
        """
        return """
        Copyright (c) 2021 Oleg Zolotov
           
        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        You may obtain a copy of the License at
           
        http://www.apache.org/licenses/LICENSE-2.0

        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.
        """

    def asDataArray(self):
        """
        'asDataArray' method removes two extra added DOY's (-15, 380)
        and provides the resulting DataArray back to the user.
        Extra DOYs were added (copied from DOYs 350, and 15) to the original
        data-values by O.Z. to make the standard interpolation (DataArray method
        interp) work correctly with DOYs prior to DOY=15 and exceeding DOY=350.
        :return: xarray.DataArray holding the FIRI-2018 electron density
                 (tabulated) values as presented in the original paper
                 by Friedrich et al.(2018), doi.org/10.1029/2018JA025437
        """
        return self._firi_data.sel(doy=slice(15., 350.))

    def get_profile(self, doy, chi, lat, f10_7):
        """
        Method 'get_profile' returns altitudinal electron density (m**-3) variation
        (vertical profile) for a given latitude and specified conditions.
        The profile is either one from tabulated (pre-calculated) values
        or is obtained via interpolation. __NO__ extrapolation is performed.
        :param doy: (int) or (1D array_like int); Julian Day Number (day of year, 0 - 365)
        :param chi: (float) or (1D array_like float); Solar zenith angle, [deg.]
        :param lat: (float) or (1D array_like float); latitude, [deg.]
        :param f10_7: (float) or (1D array_like float); Solar F10.7 index, [s.f.u.]
        :return: xarray.ArrayData; vertical electron density values, [el./(m**3)], with associated metadata
        """
        # pack single floats, when given, into lists
        if isinstance(doy, float) or isinstance(doy, int):
            doy = [float(doy)]
        if isinstance(chi, float) or isinstance(chi, int):
            chi = [float(chi)]
        if isinstance(lat, float) or isinstance(lat, int):
            lat = [float(lat)]
        if isinstance(f10_7, float) or isinstance(f10_7, int):
            f10_7 = [float(f10_7)]

        # Check for input parameters' ranges
        # ? doy is in 0 - 365 range
        for _ in doy:
            if (_ > 365) or (_ < 1):
                raise ValueError("Accepted Julian Day Number should be in [1-365]; "
                                 "The value {value} is given."
                                 .format(value=_))

        # ? Solar Zenith Angle is in 0 - 130 range
        for _ in chi:
            if (_ > 130) or (_ < 0):
                raise ValueError("Accepted Solar Zenith Angle should be in [0-130] range."
                                 "The value {value} is given."
                                 "If required, extrapolation should be perfomed by the user."
                                 .format(value=_))

        # ? latitude is in 0 - 360 range
        for _ in lat:
            if (_ > 360) or (_ < 0):
                raise ValueError("Latitude should be in [0-360] range."
                                 "A user should fit input values into [0-360] range if required."
                                 "The value {value} is given."
                                 .format(value=_))

        # ? Solar F10.7 index is in 75 - 200 range
        for _ in f10_7:
            if (_ > 200.) or (_ < 75.):
                raise ValueError("Accepted f10.7 index values should be in [75-200] range."
                                 "If required, extrapolation should be perfomed by the user."
                                 "The value {value} is given."
                                 .format(value=_))
        # end of input parameters' range validation

        return self._firi_data.interp(doy=doy, chi=chi, lat=lat, f10_7=f10_7
                                      , method='linear'
                                      , assume_sorted=True)

    def interp(self, *args, **kwargs):
        """
        Method 'interp' is a non-wrapped (unsafe, i.e., direct) proxy
                to the interp method of the underlying xarray.DataArray
                (model tabulated values).
        :param args: positional arguments to pass
        :param kwargs: key-value arguments to pass
        :return: DataArray with interpolated values
               according to args & kwargs passed
        """
        return self._firi_data.interp(*args, **kwargs)
