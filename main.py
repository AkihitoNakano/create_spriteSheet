from PIL import Image
from glob import glob

target_dir = '/Users/resonant/Desktop/photos'

imgs = glob(target_dir + "/*.png")


class sprite_sheet:
    def __init__(self, imgs, col):
        self.col = col
        self.imgs = imgs
        self.imgs.sort()
        print(self.imgs)

        self.create_img()
        self.create_sheet()
        
    def create_img(self):
        self.img_list = []
        for img in self.imgs:
            self.i = Image.open(img)
            self.img_list.append(self.i)
            
    def create_sheet(self):
        width, height = self.img_list[0].size
        row = -(-len(self.img_list) // self.col)
        bg = Image.new('RGB', (width * self.col, height * row))
        for i , img in enumerate(self.img_list):
            col_n = i % self.col
            row_n = i // self.col
            bg.paste(img, (col_n*width, row_n* height))

        bg.save(target_dir + '/integrated.png')

if __name__ == "__main__":
    while True:
        col = int(input('行の数値を入力して下さい(最小値１)'))
        if col:
            break
        else:
            print('エラーが発生しました。もう一度入力し直して下さい')
            
    sprite_sheet(imgs, col)
