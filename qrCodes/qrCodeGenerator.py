import qrcode
from datetime import datetime
img = qrcode.make('''
https://www.google.com/maps/dir/Chippewa+Campground,+Ontario+11,+Atikokan,+ON/Kakabeka+Falls,+Oliver+Paipoonge,+ON/Terry+Fox+Monument+And+Statue,+Ontario+11,+Thunder+Bay,+ON/Hattie+Cove+Campground,+Hattie+Cove+Campground,+Heron+Bay,+ON/@48.348004,-86.6698791,7.96z/data=!4m26!4m25!1m5!1m1!1s0x52a6b3996eb8f3cf:0xc2565aaad8bb35a2!2m2!1d-91.1339928!2d48.6668016!1m5!1m1!1s0x4d58c02957112e29:0xcd2060549b297187!2m2!1d-89.6256961!2d48.4026834!1m5!1m1!1s0x4d59237034ada2b1:0x26b3d14923af6f44!2m2!1d-89.1680472!2d48.4843708!1m5!1m1!1s0x4d4477fed4131d2f:0xf61de17376e4069b!2m2!1d-86.2936243!2d48.5919138!3e0?entry=ttu&g_ep=EgoyMDI1MDIxOS4xIKXMDSoASAFQAw%3D%3D''')
type(img)
img.save("qrCodes/codes/" + str(datetime.now()) + "some_file.png")