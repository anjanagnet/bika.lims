# This file is part of Bika LIMS
#
# Copyright 2011-2016 by it's authors.
# Some rights reserved. See LICENSE.txt, AUTHORS.txt.

from Products.Archetypes.Widget import SelectionWidget as _s
from Products.Archetypes.Registry import registerWidget

from AccessControl import ClassSecurityInfo

class SelectionWidget(_s):
    _properties = _s._properties.copy()
    _properties.update({
        'macro': "bika_widgets/selection",
    })

    security = ClassSecurityInfo()

registerWidget(SelectionWidget)
