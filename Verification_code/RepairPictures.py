from PIL import Image

"""
修复 big.png 
"""

class RepairPictures:
    def change_pic(self):
        # 打开图像文件
        image = Image.open("./Verification_pic/big.png")

        # 获取图像的宽度和高度
        width, height = image.size

        # 计算切割后每个小图像的大小
        tile_width = width // 6  # 切割成6列

        # 切割图像并存储在一个列表中
        tiles = ['','','','','','']
        order = [2,6,5,3,1,4]
        page = 0
        for x in order:
            left = page * tile_width
            page+=1
            right = left + tile_width
            tile = image.crop((left, 0, right, height))
            tiles[x-1] = tile

        # 创建一个新的空白图像，用于重组图像
        new_image = Image.new("RGB", (width, height))

        # 重组图像
        for i, tile in enumerate(tiles):
            left = i * tile_width
            right = left + tile_width
            new_image.paste(tile, (left, 0, right, height))

        # 保存重组后的图像
        new_image.save("./Verification_pic/bigger.png")
