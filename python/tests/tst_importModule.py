# This file is part of the KD Chart library.
#
# SPDX-FileCopyrightText: 2021 Klarälvdalens Datakonsult AB, a KDAB Group company <info@kdab.com>
#
# SPDX-License-Identifier: MIT
#

''' Test loading some KDChart classes '''

# pylint: disable=missing-function-docstring,missing-class-docstring

import unittest
import importlib
import inspect

from config import TstConfig


class TestImportModules(unittest.TestCase):
    def test_importModules(self):
        m = importlib.import_module(TstConfig.bindingsNamespace + '.KDGantt')
        moduleSymbols = []
        for t in inspect.getmembers(m):
            moduleSymbols.append(t[0])

        symbols = ['AbstractGrid', 'AbstractRowController', 'Constraint',
                   'ConstraintGraphicsItem', 'ConstraintModel', 'ConstraintProxy',
                   'DateTimeGrid', 'DateTimeScaleFormatter', 'ForwardingProxyModel',
                   'GraphicsScene', 'GraphicsView', 'ItemDataRole', 'ItemDelegate',
                   'ItemType', 'Legend', 'ListViewRowController', 'ProxyModel',
                   'Span', 'StyleOptionGanttItem', 'View']
        for symbol in symbols:
            self.assertIn(symbol, moduleSymbols)


if __name__ == '__main__':
    TstConfig.initLibraryPath()
    unittest.main()
