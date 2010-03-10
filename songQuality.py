# songQuality.py
# ==============================================================================
# Michael Van Veen
# 03/11/10
# ==============================================================================
# Determining a heuristic for song quality
# ==============================================================================

# Modern personal media collections span thousands, sometimes even tens or 
# hundreds of thousands of files.  Most of these collections are automattically 
# organized by programs such as iTunes or AmaRok.  Having tried several of the 
# existing collection organization tools, I have found none satisfactory or to 
# my liking.  The need for a music collection toolset in the vain of the unix 
# desgign philosophy is clear.
# 
# Quick song quality determination is an important feature which should be 
# included within a music collection toolset.  The need for quick song quality 
# determination arises when finding and eliminating duplicate songs in a collection.
#

# Filetypes supported by project
supportedFileTypes = ["flac", "mp3", "m4a", "asf", "ogg", "wav"]

def songQuality():
	
