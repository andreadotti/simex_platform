""" Module holding the AbstractPhotonPropagator abstract class."""
##########################################################################
#                                                                        #
# Copyright (C) 2015-2017 Carsten Fortmann-Grote                         #
# Contact: Carsten Fortmann-Grote <carsten.grote@xfel.eu>                #
#                                                                        #
# This file is part of simex_platform.                                   #
# simex_platform is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# simex_platform is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#                                                                        #
##########################################################################

from abc import ABCMeta
from abc import abstractmethod

from SimEx.Calculators.AbstractBaseCalculator import AbstractBaseCalculator
from SimEx.Utilities.EntityChecks import checkAndSetInstance

class AbstractPhotonPropagator(AbstractBaseCalculator):
    """
    Class representing an abstract photon propagator, serving as API for actual photon propagation calculators.
    """

    # Make this class an abstract base class.
    __metaclass__  = ABCMeta

    # Abstract constructor.
    @abstractmethod
    def __init__(self, parameters=None, input_path=None, output_path=None):
        """

        :param parameters: Parameters of the calculation (not data).
        :type parameters: dict || AbstractCalculatorParameters

        :param input_path: Path to hdf5 file holding the input data.
        :type input_path: str

        :param output_path: Path to hdf5 file for output.
        :type output_path: str
        """

        # Check input path. Set to default if none given.
        input_path = checkAndSetInstance(str, input_path, 'source')
        # Check output path. Set default if none given.
        output_path = checkAndSetInstance(str, output_path, 'prop')

        # Initialize base class.
        super(AbstractPhotonPropagator, self).__init__(parameters, input_path, output_path)

        # Setup expected data groups and sets.
        self.__expected_data = ['/data/arrEhor',
                                '/data/arrEver',
                                '/params/Mesh/nSlices',
                                '/params/Mesh/nx',
                                '/params/Mesh/ny',
                                '/params/Mesh/sliceMax',
                                '/params/Mesh/sliceMin',
                                '/params/Mesh/xMax',
                                '/params/Mesh/xMin',
                                '/params/Mesh/yMax',
                                '/params/Mesh/yMin',
                                '/params/Mesh/zCoord',
                                '/params/Rx',
                                '/params/Ry',
                                '/params/dRx',
                                '/params/dRy',
                                '/params/nval',
                                '/params/photonEnergy',
                                '/params/wDomain',
                                '/params/wEFieldUnit',
                                '/params/wFloatType',
                                '/params/wSpace',
                                '/params/xCentre',
                                '/params/yCentre',
                                '/history/parent/info/data_description',
                                '/history/parent/info/package_version',
                                '/history/parent/misc/FAST2XY.DAT',
                                '/history/parent/misc/angular_distribution',
                                '/history/parent/misc/spot_size',
                                '/history/parent/misc/gain_curve',
                                '/history/parent/misc/nzc',
                                '/history/parent/misc/temporal_struct',
                                '/version',
                                ]

        # Setup provided data groups and sets.
        self.__provided_data = [
                                '/data/arrEhor',
                                '/data/arrEver',
                                '/params/Mesh/nSlices',
                                '/params/Mesh/nx',
                                '/params/Mesh/ny',
                                '/params/Mesh/qxMax',
                                '/params/Mesh/qxMin',
                                '/params/Mesh/qyMax',
                                '/params/Mesh/qyMin',
                                '/params/Mesh/sliceMax',
                                '/params/Mesh/sliceMin',
                                '/params/Mesh/xMax',
                                '/params/xMin',
                                '/params/yMax',
                                '/params/yMin',
                                '/params/zCoord',
                                '/params/beamline/printout',
                                '/params/Rx',
                                '/params/Ry',
                                '/params/dRx',
                                '/params/dRy',
                                '/params/nval',
                                '/params/photonEnergy',
                                '/params/wDomain',
                                '/params/wEFieldUnit',
                                '/params/wFloatType',
                                '/params/wSpace',
                                '/params/xCentre',
                                '/params/yCentre',
                                '/info/package_version',
                                '/info/contact',
                                '/info/data_description',
                                '/info/method_description',
                                '/misc/xFWHM',
                                '/misc/yFWHM',
                                '/version',
                                ]

    def expectedData(self):
        """
        Return the list of expected data sets with full paths.

        :return: List of strings, e.g. ['/data/data1', '/params/params1']
        """
        return self.__expected_data

    def providedData(self):
        """
        Return the list of provided data sets with full paths.

        :return: List of strings, e.g. [/data/data1, /params/params1']
        """
        return self.__provided_data

def checkAndSetPhotonPropagator(var=None, default=None):
    """
    Check if passed object is an AbstractPhotonPropagator instance. If non is given, set to given default.

    :param var: The object to check
    :param default: The default to use
    :return: The checked photon source object
    :raise RuntimeError: if no valid PhotonPropagator was given.
    """

    return checkAndSetInstance(AbstractPhotonPropagator, var, default)
