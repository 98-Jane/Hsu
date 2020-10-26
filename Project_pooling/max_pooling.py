import numpy as np
import cv2


# # 池化操作，缩放图像
# def pooling(data, m, n, key='mean'):
#     h, w, c = data.shape
#     img_new = []
#     for i in range(0, h, m):
#         line = []
#         for j in range(0, w, n):
#             x = data[i:i + m, j:j + n]  # 选取池化区域
#             if key == 'mean':  # 平均池化
#                 line.append([np.sum(x[:, :, 0] / (n * m)), np.sum(x[:, :, 1] / (n * m)), np.sum(x[:, :, 2] / (n * m))])
#             elif key == 'max':  # 均值池化
#                 line.append([np.max(x[:, :, 0]), np.max(x[:, :, 1]), np.max(x[:, :, 2])])
#             else:
#                 return data
#         img_new.append(line)
#     return np.array(img_new, dtype='uint8')


# 池化操作，缩放图像
def pooling_step(data, m, n, stride, key='mean'):
    h, w, c = data.shape
    img_new = []
    for i in range(0, h, stride):
        line = []
        for j in range(0, w, stride):
            x = data[i:i + m, j:j + n]  # 选取池化区域
            if key == 'mean':  # 平均池化
                line.append([np.sum(x[:, :, 0] / (n * m)), np.sum(x[:, :, 1] / (n * m)), np.sum(x[:, :, 2] / (n * m))])
            elif key == 'max':  # 均值池化
                line.append([np.max(x[:, :, 0]), np.max(x[:, :, 1]), np.max(x[:, :, 2])])
            else:
                return data
        img_new.append(line)
    return np.array(img_new, dtype='uint8')

if __name__ == '__main__':
    img = cv2.imread('lena.jpg')

    img_new_5 = pooling_step(img, 5, 5, stride=1, )
    img_new_9 = pooling_step(img, 9, 9, stride=1, )
    img_new_13 = pooling_step(img, 13, 13, stride=1,)

    # img_new_5 = pooling(img, 5, 5, 'max')
    # img_new_9 = pooling(img, 9, 9, 'max')
    # img_new_13 = pooling(img, 13, 13, 'max')

    cv2.imwrite('/home/xujiaqian/桌面/Conv_Project/pooling_5.jpg', img_new_5)
    cv2.imwrite('/home/xujiaqian/桌面/Conv_Project/pooling_9.jpg', img_new_9)
    cv2.imwrite('/home/xujiaqian/桌面/Conv_Project/pooling_13.jpg', img_new_13)

    cv2.imshow('ori', img)
    cv2.imshow('pooling_5', img_new_5)
    cv2.imshow('pooling_9', img_new_9)
    cv2.imshow('pooling_13', img_new_13)
    cv2.waitKey(0)