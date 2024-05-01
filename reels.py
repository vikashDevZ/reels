from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

video_clip = VideoFileClip("21.mp4")
image_clip = ImageClip("Freak.png")

x_pos = (video_clip.w - image_clip.w)
y_pos = (video_clip.h - image_clip.h)

image_clip = image_clip.resize(width=new_width, height=new_height)

image_clip = image_clip.set_position((x_pos, y_pos))

final_clip = CompositeVideoClip([video_clip, image_clip])

final_clip = final_clip.set_duration(video_clip.duration)

final_clip.write_videofile("output_video.mp4", fps=video_clip.fps)
