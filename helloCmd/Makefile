#-
# ==========================================================================
# Copyright (c) 2011 Autodesk, Inc.
# All rights reserved.
# 
# These coded instructions, statements, and computer programs contain
# unpublished proprietary information written by Autodesk, Inc., and are
# protected by Federal copyright law. They may not be disclosed to third
# parties or copied or duplicated in any form, in whole or in part, without
# the prior written consent of Autodesk, Inc.
# ==========================================================================
#+

ifndef INCL_BUILDRULES

#
# Include platform specific build settings
#
TOP := ..
include $(TOP)/buildrules


#
# Always build the local plug-in when make is invoked from the
# directory.
#
all : plugins

endif

#
# Variable definitions
#

SRCDIR := .
DSTDIR := $(BUILDDIR)

SOURCES  := $(wildcard *.cpp) $(wildcard **/*.cpp)
OBJECTS  := $(addprefix $(OBJDIR)/,$(patsubst %.cpp, %.o, $(SOURCES)))

PLUGIN   := $(DSTDIR)/$(PROJECT_NAME).$(EXT)
MAKEFILE := $(SRCDIR)/Makefile

#
# Include the optional per-plugin Makefile.inc
#
#    The file can contain macro definitions such as:
#       {pluginName}_EXTRA_CFLAGS
#       {pluginName}_EXTRA_C++FLAGS
#       {pluginName}_EXTRA_INCLUDES
#       {pluginName}_EXTRA_LIBS
-include $(SRCDIR)/Makefile.inc


#
# Set target specific flags.
#

$(OBJECTS): CFLAGS   := $(CFLAGS)   $(EXTRA_CFLAGS)
$(OBJECTS): C++FLAGS := $(C++FLAGS) $(EXTRA_C++FLAGS)
$(OBJECTS): INCLUDES := $(INCLUDES) $(EXTRA_INCLUDES)

depend_mayaProject:     INCLUDES := $(INCLUDES) $(EXTRA_INCLUDES)

$(PLUGIN):  LFLAGS   := $(LFLAGS) $(EXTRA_LFLAGS) 
$(PLUGIN):  LIBS     := $(LIBS)   -lOpenMaya -lFoundation $(EXTRA_LIBS) 

#
# Rules definitions
#

.PHONY: depend_mayaProject clean_mayaProject Clean_mayaProject


$(PLUGIN): $(OBJECTS) 
	-rm -f $@
	$(LD) -o $@ $(LFLAGS) $^ $(LIBS) 

depend_mayaProject :
	makedepend $(INCLUDES) $(MDFLAGS) -f$(DSTDIR)/Makefile $(SOURCES)

clean_mayaProject:
	-rm -rf $(OBJBASEDIR)
	-rm -rf $(BUILDBASEDIR)

Clean_mayaProject:
	-rm -f $(MAKEFILE).bak $(OBJECTS) $(PLUGIN)


plugins: directories $(PLUGIN)
depend:	 depend_mayaProject
clean:	 clean_mayaProject
Clean:	 Clean_mayaProject

