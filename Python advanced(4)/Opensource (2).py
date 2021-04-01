import glob
from PIL import Image


class GifConverter:
    def __init__(self, path_in=None, path_out=None, resize=(320, 240)):
        """
        opensource는 이렇게 설명을 해주는게 좋다.
        :param path_in:
        :param path_out:
        :param resize:

        이전의 내용을 클래스 형태로 만드는 과정
        """

        self.path_in = path_in or './*.png'
        self.path_out = path_out or './output.gif'
        self.resize = resize

    def convert_gif(self):
        img, *images = \
            [Image.open(f).resize(self.resize, Image.ANTIALIAS) for f in
             sorted(glob.glob(self.path_in))]  # ANITALIAS: 여백 방지

        try:
            img.save(
                fp=self.path_out,
                format="GIF",
                append_images=images,
                save_all=True,
                duration=500,
                loop=0
            )
        except IOError:
            print('Cannot covert!', img)

# 배포 했을 때 아래 if조건이 없으면, 우리가 테스트 한 코드가 그대로 사용되기에, \
# __name__ == '__main__' 조건을 달아준다.


# if __name__ == '__main__':
#     # 클래스
#     c = GifConverter('../project/images/*.png', '../project/image_out/result.gif', (320, 240))
#     c.convert_gif()
#


search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''


import re
regex = '\d{2~3}[- ]?\d{3~4}[- ]?\d{4}[- ]'

result = re.findall(regex, search_target)
print(result)

