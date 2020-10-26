class Solution:
    def _iou(self, box1, box2):
        b1_xmin, b1_ymin, b1_xmax, b1_ymax = box1
        b2_xmin, b2_ymin, b2_xmax, b2_ymax = box2
        int_xmin = max(b1_xmin, b2_xmin)
        int_ymin = max(b1_ymin, b2_ymin)
        int_xmax = min(b1_xmax, b2_xmax)
        int_ymax = min(b1_ymax, b2_ymax)
        w = max(0, int_xmax-int_xmin)
        h = max(0, int_ymax-int_ymin)
        int_area = w*h
        b1_area = (b1_xmax-b1_xmin)*(b1_ymax-b1_ymin)
        b2_area = (b2_xmax-b2_xmin)*(b2_ymax-b2_ymin)
        iou = int_area/(b1_area+b2_area-int_area+1e-05)
        return iou

# class Solution:
#     def _iou(self, box1, box2):
#         b1_xmin, b1_ymin, b1_xmax, b1_ymax = box1
#         b2_xmin, b2_ymin, b2_xmax, b2_ymax = box2
#         xmin = max(b1_xmin, b2_xmin)
#         ymin = max(b1_ymin, b2_ymin)
#         xmax = min(b1_xmax, b2_xmax)
#         ymax = min(b1_ymax, b2_ymax)
#
#         w = max(0, xmax-xmin)
#         h = max(0, ymax-ymin)
#         int_area = w*h
#
#         b1_area = (b1_xmax-b1_xmin)*(b1_ymax-b1_ymin)
#         b2_area = (b2_xmax-b2_xmin)*(b2_ymax-b2_ymin)
#
#         iou = int_area/(b1_area + b2_area - int_area + 1e-05)
#         return iou




# class Solution:
#     '''param box1:array of 4 values(前两个代表左上角的坐标，后两个代表右下角的坐标):[x0,y0,x1,y1]
#     '''
#     def _iou(self, box1, box2):
#         b1_x0, b1_y0, b1_x1, b1_y1 = box1
#         b2_x0, b2_y0, b2_x1, b2_y1 = box2
#         int_x0 = max(b1_x0, b2_x0)
#         int_y0 = max(b1_y0, b2_y0)
#         int_x1 = min(b1_x1, b2_x1)
#         int_y1 = min(b1_y1, b2_y1)
#
#         # int_area = (int_x1-int_x0)*(int_y1-int_y0)
#         w = max(0, (int_x1-int_x0))
#         h = max(0, (int_y1-int_y0))
#         int_area = w * h
#
#         b1_area = (b1_x1 - b1_x0)*(b1_y1 - b1_y0)
#         b2_area = (b2_x1 - b2_x0)*(b2_y1 - b2_y0)
#
#         iou = int_area/(b1_area + b2_area - int_area + 1e-05)
#         return iou


