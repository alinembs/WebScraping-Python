#!/usr/bin/env python
import PySimpleGUI as sg
import os

'''
    Simple Image Browser 
    
    This is an early demo program, so perhaps not quite as sophisticated as later ones.
    
    Copyright 2021 PySimpleGUI
'''


def main():

    # Get the folder containing the images from the user
    folder = sg.popup_get_folder('Image folder to open')
    if folder is None:
        sg.popup_cancel('Cancelling')
        return

    # get list of PNG files in folder
    png_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith('.png')]
    filenames_only = [f for f in os.listdir(folder) if f.lower().endswith('.png')]
    print(os.getcwd())

    if len(png_files) == 0:
        sg.popup('No PNG images in folder')
        return

main()