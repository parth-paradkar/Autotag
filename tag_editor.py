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
        if (tag_song.tag == None):
            tag_song.tag.artist = unicode(song_artist, "utf-8")
            tag_song.tag.title = unicode(song_title, "utf-8")
        if (tag_song.images == None):
            try:
                image_name = '{}.jpg'.format(song_artist)
                image_path = image_dirpath + image_name
                cover_image = open(image_path, 'rb').read()
                tag_song.tag.images.set(3, cover_image, 'image/jpeg')
            except IOError:
                print("The cover art for {} not found".format(artist_name))
        tag_song.tag.save()
        os.rename(song, song_title)
    except ValueError:
        print("The song {} name is not in the proper format".format(song_name))
    except UnicodeDecodeError:
        print("There are unrecognized characters in the file name of {}".format(song_name))
    
