###############################################################################
# -*- python -*-
#
#       amlPy function definition 
#
#       Copyright or (C) or Copr. 2006 INRIA - CIRAD - INRA  
#
#       File author(s): Christophe Pradal <christophe.prada@cirad.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################

__doc__="""
amlPy function definition
"""

__license__= "Cecill-C"
__revision__=" $Id$ "

from openalea.core.external import *

def define_factory(package):
    """ Define factories for arithmetics nodes """

    nf = Factory( name= "MTG", 
                  description= "MTG file creation", 
                  category = "MTG", 
                  nodemodule = "py_mtg",
                  nodeclass = "MTG",
                  )

    package.add_factory( nf )

    nf = Factory( name= "VtxList", 
                  description= "Array of vertices contained in a MTG", 
                  category = "MTG", 
                  nodemodule = "py_mtg",
                  nodeclass = "VtxList",
                  )

    package.add_factory( nf )

    nf = Factory( name= "VtxFunction", 
                  description= "Common function on  MTG", 
                  category = "MTG", 
                  nodemodule = "py_mtg",
                  nodeclass = "VtxFunction",
                  )

    package.add_factory( nf )

    nf = Factory( name= "TopoFunction", 
                  description= "Common function on  MTG", 
                  category = "MTG", 
                  nodemodule = "py_mtg",
                  nodeclass = "TopoFunction",
                  )

    package.add_factory( nf )

    nf = Factory( name= "Complex", 
                  description= "Complex of a vertex.", 
                  category = "MTG", 
                  nodemodule = "py_mtg",
                  nodeclass = "Complex",
                  )

    package.add_factory( nf )

    nf = Factory( name= "Components", 
                  description= "Set of components of a vertex.", 
                  category = "MTG", 
                  nodemodule = "py_mtg",
                  nodeclass = "Components",
                  )

    package.add_factory( nf )

    nf = Factory( name= "Plot", 
                  description= "Plot aml objects.", 
                  category = "MTG", 
                  nodemodule = "py_mtg",
                  nodeclass = "Plot",
                  )
    package.add_factory( nf )

    nf = Factory( name= "PlantFrame", 
                  description= "Constructs a geometric interpretation of a MTG.", 
                  category = "MTG", 
                  nodemodule = "py_mtg",
                  nodeclass = "PlantFrame",
                  )
    package.add_factory( nf )

