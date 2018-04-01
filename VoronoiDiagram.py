########################################################################
#                                                                           
#                                                                    
#                      Voronoi Diagram generation                                                           
#                            VoronoiDiagram.py                                      
#                                                                           
#                                MAIN                                      
#                                                                           
#                 Copyright (C) 2003 Ulrik Hoerlyk Hjort                   
#                                                                        
#  Voronoi Diagram generation is free software;  you can  redistribute it                          
#  and/or modify it under terms of the  GNU General Public License          
#  as published  by the Free Software  Foundation;  either version 2,       
#  or (at your option) any later version.                                   
#  Voronoi Diagram generation is distributed in the hope that it will be                           
#  useful, but WITHOUT ANY WARRANTY;  without even the  implied warranty    
#  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  
#  See the GNU General Public License for  more details.                    
#  You should have  received  a copy of the GNU General                     
#  Public License  distributed with Yolk.  If not, write  to  the  Free     
#  Software Foundation,  51  Franklin  Street,  Fifth  Floor, Boston,       
#  MA 02110 - 1301, USA.                                                    
########################################################################        
import random
import math
from PIL import Image
import sys 


##########################################################
#
#
#
##########################################################
def voronoiDiagram(cells,width, height, fname):

    image  = Image.new("RGB", (width, height))
    points = zip(random.sample(xrange(width), cells),random.sample(xrange(height), cells))
    rgb    = zip(random.sample(xrange(256), cells),random.sample(xrange(256), cells),random.sample(xrange(256), cells))
    color  = None

    for y in range(height):
        for x in range(width):
            d_min = math.hypot(width-1, height-1)
            for i in range(cells):
                d = math.hypot(points[i][0]-x, points[i][1]-y)
                if d < d_min:
                    d_min = d
                    color = rgb[i]          
            image.putpixel((x, y), color)
    image.save(fname+".png")
 

############################################################
#
#  M A I N
#
############################################################
if  len(sys.argv) != 5:
    print "Error: Wrong number of arguments"
    print "Usage: python VoronoiDiagram.py <cells> <image width> <image height> <filename>"
    sys.exit(1)


voronoiDiagram(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]), sys.argv[4])
