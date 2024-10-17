import psutil
import os

import gphoto2 as gp

class CustomCamera():

    def __init__(self):
        self.quiet = True

    # Kill gphoto2 Process that startes when we connect the camera
    def killgphoto2process(self):
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == 'gvfsd-gphoto2':
                print('Process found! Killing it now..')
                proc.kill()

    def init_camera(self, camera):
        self.killgphoto2process()
        camera.init()

    def create_target_folder(self, path):
        try:
            print("Making folder: " + path)
            os.makedirs(path)
        except:
            print('Failed to create the new directory.')

    def capture_and_download_image(self, camera, target):
        # Capturing Photo
        if not self.quiet:
            print('Capturing image')
        file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
        if not self.quiet:
            print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))

        # Copying Image to target
        if not self.quiet:
            print('Copying image to', target)
        camera_file = camera.file_get(
            file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
        camera_file.save(target)






