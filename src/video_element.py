import pygame
import random
import os
import cv2
import config.const 

class VideoElement:
    def __init__(self,video_folder):
        self.video_folder=video_folder
        


    def get_random_video(self):
        """Select a random video file from the given folder"""
        video_files= [f for f in os.listdir(config.const.VYDEO_FOLDER) if f.endswith((".mp4"))]


       
        if not video_files:
            print("Error: No video files found in the folder.")
            return None
        random_video = random.choice(video_files)
        video_path = os.path.join(self.video_folder, random_video)
        
        # Extract the name of the video without the extension
        video_name_without_extension = os.path.splitext(random_video)[0]
        convert_int=int(video_name_without_extension)
        print(f"Random video selected: {convert_int}")  # Video name without extension
        
        return video_path

   
    def play_video(self, window, video_path, fps=30):

        """Play the selected video."""
         # Ensure video_path is a string (valid file path)
        if not isinstance(video_path, str):
            print("Error: video_path should be a string representing the file path.")
            return
        
        if not os.path.exists(video_path):
            print(f"Error: Video file does not exist at {video_path}")
            return

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error: Failed to open video {video_path}")
            return True

        clock=pygame.time.Clock()
        should_continue=True

        while cap.isOpened():
            ret,frame =cap.read()
            if not ret:
                break #video is finished

            frame= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame= pygame.surfarray.make_surface(frame.swapaxes(0,1))

            window.blit(frame, (0, 0))
            pygame.display.update()
            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cap.release()
                    should_continue=False
                    break
            
            if not should_continue:
             break  # Exit video loop early if quitting




        cap.release()
        return should_continue  # Return the flag to indicate if the video was played successfully



