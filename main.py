import pygame
from pygame import mixer
from tkinter import *
import os

def playsong(song_path):
    mixer.music.load(song_path)
    songstatus.set("Playing")
    mixer.music.play()

def play_song_from_selection():
    current_index = playlist.curselection()
    if current_index:
        current_song_index = current_index[0]
        song_path = os.path.join(os.getcwd(), playlist.get(current_song_index))
        playsong(song_path)

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

def load_playlist(folder_path):
    os.chdir(folder_path)
    songs = os.listdir()
    for s in songs:
        playlist.insert(END, s)
    return songs

current_song_index = 0

def nextsong():
    global current_song_index
    if current_song_index  < playlist.size() - 1:
        current_song_index += 1
        playlist.selection_clear(0, END)
        playlist.selection_set(current_song_index)
        next_song_path = os.path.join(os.getcwd(), playlist.get(current_song_index))
        playsong(next_song_path)


def prevsong():
    global current_song_index
    if current_song_index > 0:
        current_song_index -= 1
        playlist.selection_clear(0, END)
        playlist.selection_set(current_song_index)
        prev_song_path = os.path.join(os.getcwd(), playlist.get(current_song_index))
        playsong(prev_song_path)


def searchsong():
    global search_entry, current_song_index, songs
    search_text = search_entry.get().lower()
    matching_indices = [i for i, song in enumerate(songs) if search_text in song.lower()]
    if matching_indices:
        next_occurrence = next((i for i  in matching_indices if i > current_song_index), None)
        if  next_occurrence is not None:
            current_song_index = next_occurrence
        else:
            current_song_index = matching_indices[0]
        playlist.selection_clear(0, END)
        playlist.selection_set(current_song_index)
        play_song_from_selection()
    
def set_end_event():
    mixer.music.set_endevent(pygame.USEREVENT + 1)

def handle_end_event(event):
    if event.type == pygame.USEREVENT + 1:
        nextsong()

pygame.init()

root=Tk()
root.title('Music player')

mixer.init()
songstatus=StringVar()
songstatus.set("Choosing")

#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="White",fg="Black",font=('Arvo',10),width=40)
playlist.grid(columnspan=30)

songs = load_playlist(r'C:\Users\ELITEBOOK\Music')

playbtn=Button(root,text="play",command=playsong(os.path.join(os.getcwd(), playlist.get(ACTIVE))))
playbtn.config(font=('Segoe Print',20),bg="Black",fg="white",padx=32,pady=2)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('Segoe Print',20),bg="Black",fg="white",padx=32,pady=2)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('Segoe Print',20),bg="Black",fg="white",padx=7,pady=7)
stopbtn.grid(row=2,column=1,columnspan=1)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('Segoe Print',20),bg="Black",fg="white",padx=30,pady=2)
Resumebtn.grid(row=1,column=2)

nextbtn=Button(root,text="Next",command=nextsong)
nextbtn.config(font=('Segoe Print',20),bg="Black",fg="white",padx=7,pady=7)
nextbtn.grid(row=2,column=2)

prevbtn = Button(root, text="Previous", command=prevsong)
prevbtn.config(font=('Segoe Print',20),bg="Black",fg="white",padx=7,pady=7)
prevbtn.grid(row=2, column=0,columnspan=1)

search_entry = Entry(root, width=30, font=('Segoe Print', 15))
search_entry.grid(row=3, column=0, columnspan=4, pady=10)

searchbtn = Button(root, text="Search", command=searchsong)
searchbtn.config(font=('Segoe Print', 15),bg="Black",fg="white",padx=7, pady=7)
searchbtn.grid(row=2,column=3, columnspan=1)

set_end_event()
pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

pygame.event.set_allowed(pygame.USEREVENT + 1)
pygame.event

root.mainloop()