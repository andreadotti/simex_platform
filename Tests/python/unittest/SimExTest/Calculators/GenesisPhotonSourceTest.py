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

""" Test module for the GenesisPhotonSource.

    @author : CFG
    @institution : XFEL
    @creation 20170215

"""
import paths
import unittest

import numpy
import h5py
import os

# Import the class to test.
from SimEx.Calculators.AbstractPhotonSource import AbstractPhotonSource
from SimEx.Calculators.GenesisPhotonSource import GenesisPhotonSource
from TestUtilities import TestUtilities

class GenesisPhotonSourceTest(unittest.TestCase):
    """
    Test class for the GenesisPhotonSource class.
    """

    @classmethod
    def setUpClass(cls):
        """ Setting up the test class. """
        pass

    @classmethod
    def tearDownClass(cls):
        """ Tearing down the test class. """

    def setUp(self):
        """ Setting up a test. """
        self.__files_to_remove = []
        self.__dirs_to_remove = []

    def tearDown(self):
        """ Tearing down a test. """
        for f in self.__files_to_remove:
            if os.path.isfile(f):
                os.remove(f)
        for d in self.__dirs_to_remove:
            if os.path.isdir(d):
                shutil.rmtree(d)

    def testConstructionNativeBeamFile(self):
        """ Testing the construction of the class with a native genesis beam file."""

        # Construct the object.
        xfel_source = GenesisPhotonSource(parameters=None, input_path=TestUtilities.generateTestFilePath('genesis_beam.dat'))

        self.assertIsInstance(xfel_source, AbstractPhotonSource)
        self.assertIsInstance(xfel_source, GenesisPhotonSource)

    def testConstructionPicH5(self):
        """ Testing the construction of the class with a given PIC snapshot. """

        # Construct the object.
        xfel_source = GenesisPhotonSource(parameters=None, input_path=TestUtilities.generateTestFilePath('simData_8000.h5'))

        self.assertIsInstance(xfel_source, AbstractPhotonSource)
        self.assertIsInstance(xfel_source, GenesisPhotonSource)

    def testReadH5(self):
        """ Testing the read function and conversion of openpmd input to native beam file."""

        # Construct the object.
        xfel_source = GenesisPhotonSource(parameters=None, input_path=TestUtilities.generateTestFilePath('simData_8000.h5'), output_path='FELsource_out.h5')

        xfel_source._readH5()
        self.assertTrue( hasattr( xfel_source, '_GenesisPhotonSource__input_data' ) )

    def testPrepareRun(self):
        """ Tests the method that sets up input files and directories for a genesis run. """

        # Ensure proper cleanup.
        self.__files_to_remove.append("beam.dist")

        # Construct the object.
        xfel_source = GenesisPhotonSource(parameters=None, input_path=TestUtilities.generateTestFilePath('simData_8000.h5'), output_path='FELsource_out.h5')

        # Read the input distribution.
        xfel_source._readH5()

        # Prepare the run.
        xfel_source._prepareGenesisRun()

        # Check input files were written.
        genesis_dist_file = "beam.dist"
        self.assertIn( genesis_dist_file, os.listdir(os.getcwd()) )

        # Check distribution file header.
        with open(genesis_dist_file) as dist_file:
            header = dist_file.readlines()[:4]
            self.assertEqual("? VERSION = 1.0\n", header[0])
            self.assertIn("? SIZE = ", header[1])
            self.assertIn("? CHARGE = ", header[2])
            self.assertEqual("? COLUMNS X XPRIME Y YPRIME T P\n", header[3])

    def testBackengine(self):
        """ Testing the read function and conversion of openpmd input to native beam file."""

        # Ensure proper cleanup.
        self.__files_to_remove.append("beam.dist")

        # Construct the object.
        xfel_source = GenesisPhotonSource(parameters=None, input_path=TestUtilities.generateTestFilePath('simData_8000.h5'), output_path='FELsource_out.h5')

        xfel_source._readH5()

        xfel_source.backengine()

        self.assertTrue( os.path.isfile( 'beam.dat' ) )


if __name__ == '__main__':
    unittest.main()

