import os
import eyed3 as eyed3

#The song name must be of the format "<artist> - <song name>.mp3"
#create a directory that will store all the songs to be edited
dir_path = '/home/parth/Music/tagging'
os.chdir(dir_path)

#Enter the path where the images are stored
image_dirpath = '/home/parth/Music/CoverArt/'

for song in os.listdir(dir_path):
    song_name, song_ext = os.path.splitext(song)
    try:
        song_artist, song_title = song_name.split(' - ')
        tag_song = eyed3.load(song)
        if tag_song.tag == None:
            print('Tags not available for the song {}'.format(song_name))
        else:
            try:
                tag_song.tag.artist = unicode(song_artist, "utf-8")
                tag_song.tag.title = unicode(song_title, "utf-8")
            
            except UnicodeDecodeError:
                print("There are unrecognized characters in the file name of {}".format(song_name))
            except AttributeError:
                print("Attribute Error.")
            #Code to embed cover art in the mp3 file
            #if (tag_song.tag.images == None):
            try:
                image_name = '{}.jpg'.format(song_artist)
                print(image_name)
                image_path = image_dirpath + image_name
                print(image_path)
                cover_image = open(image_path, 'rb').read()
                tag_song.tag.images.set(3, cover_image, 'image/jpeg')
                print("***")
            except IOError:
                print("The cover art for {} not found".format(song_artist))
            tag_song.tag.save()
            os.rename(song, song_title)
    except ValueError:
        print("The file name of {} is not in proper format".format(song_name))
            
    
