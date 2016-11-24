import bltk.utils as bl_utils
import glob

for f in glob.glob('*.dcm'):
    bl_utils.dicom_to_video(f, '%s.mp4' % f,crop_cone_area=True)
