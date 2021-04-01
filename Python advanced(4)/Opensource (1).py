"""
png to gif, pil image

정적 이미지 -> GIF
"""

import glob
# 내 디렉토리에 있는 파일들을 한번에 가져와 리스트로 변환

from PIL import Image
# PIL: python image library

# image 생성 경로
path_in = '../project/images/*.png' # glob 덕분에, 확장자를 정한 후 다 가져올 수 있게된다.
path_out = '../project/image_out/result.gif'

# 첫 번째 이미지 와 모든 이미지 리스트 패킹

# img, *images = [Image.open(f) for f in sorted(glob.glob(path_in))]

# 잘 들어왔는지 확인
# print(img)
# print(images)

# resize 필요한 경우
img, *images = [Image.open(f).resize((320,240), Image.ANTIALIAS) for f in sorted(glob.glob(path_in))] # ANITALIAS: 여백 방지


# 이미지 저장
img.save(
    fp=path_out, # fp: filename -> save() 메소드에 정의되어 있다.
    format='GIF',
    append_images=images,
    save_all=True,
    duration=300,
    loop=0
)


