import os
import re
import math

#REQUIREMENT: Dictionary
#REQUIREMENT: List
#REQUIREMENT: Keyword Search
#REQUIREMENT: Add One (or more) Objects
#REQUIREMENT: One (or more) Modules
#REQIUREMENT: Instance Data Methods & Members (like static fields)


#Tracing input file steps from instructions, note: this is not copying, right? ;3
fin = open( './/base.pov', 'r+' )
sdl = fin.read() #read the entire file into a string
fin.close() #POV source code stored as string sdl

#ANINATION PART I
#2piR/time to create animation length (loop counter)
locationVector = re.compile(r'location\s*<[^>]*>')
count = 0
while count < 10:
    # Camera Math - Radius, Cosin, Sin - R x Sin = Y vaule | R x Cosin = X value
    R = 5
    vX = R * math.cos(10) + count /2
    vY = R * math.sin(10) + count /2
    vZ = count /2
    #REQUIREMENT: Tuple
    new_string = 'location<{0},{1},{2}>'.format(vX, vY, vZ)
    # replace the results for the camera line in the code
    sdl = locationVector.sub(new_string, sdl)
    #output the new file, append numeric incrimentation
    outfile = 'tmp' + str(count) + '.pov'
    fout = open( outfile, 'w' )
    fout.write( sdl )
    fout.close()
    count +=1

#Export to movie maker
print('Encoding Movie')
os.system('ffmpeg -start_number 0 -i tmp%01d.png -c:v libx264 -r 30 -pix_fmt yuv420p movie.avi' )

#ANIMATION PART II
#Duplicate the cone, move its x axis slowly to make the percption of dilation
# coneVector = re.compile(r'cone.*\n.*\n.*')
# count2 = 0
# while count2 < 50:
#     vx1 = vx1 + 0.01
#     vy1 = vy1 + 0.01
#     vz1 = vz1 + 0.01
#     vx2 = vx2 + 0.01
#     vy2 = vy2 + 0.01
#     vz2 = vz2 + 0.01
#     other_string = 'cone <{0}, {1}. {2}>, 0 <{3}, {4}, {5}>, 0.5'.format(vx1, vy1, vz1, vx2, vy2, vz2)
#     sdl = coneVector.sub(other_string, sdl)
#     #output the new file, append numeric incrimentation
#     outfile = 'tmp' + str(count2) + '.pov'
#     fout = open( outfile, 'w' )
#     fout.write( sdl )
#     fout.close()
#     count +=1
#
# while count2 > 50 < 100:
#     vx1 -= 0.01
#     vy1 -= 0.01
#     vz1 -= 0.01
#     vx2 -= 0.01
#     vy2 -= 0.01
#     vz2 -= 0.01
#     other_string = 'cone <{0}, {1}. {2}>, 0 <{3}, {4}, {5}>, 0.5'.format(vx1, vy1, vz1, vx2, vy2, vz2)
#     sdl = coneVector.sub(other_string, sdl)
#     #output the new file, append numeric incrimentation
#     outfile = 'tmp' + str(count2) + '.pov'
#     fout = open( outfile, 'w' )
#     fout.write( sdl )
#     fout.close()
#     count +=1
