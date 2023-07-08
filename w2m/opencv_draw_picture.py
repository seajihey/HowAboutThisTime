import cv2
import numpy as np


class Drawer:
    DAYS = {
        "mon": 100,
        "tue": 235,
        "wed": 370,
        "thu": 505,
        "fri": 640,
        "sat": 775,
        "sun": 910,
    }
    CLASS_TIMES = {
        1: 80,
        2: 215,
        3: 350,
        4: 485,
        5: 620,
        6: 755,
        7: 890,
        8: 1025,
        9: 1160,
        10: 1295,
        11: 1430,
        12: 1565,
        13: 1700,
        14: 1835,
        15: 1970,
    }
    COLOR_IMPOSSIBLE = (200, 200, 251)
    COLOR_ALL_POSSIBLE = (202, 77, 22)
    COLOR_ONE_IMPOSSIBLE = (255, 197, 189)
    COLOR_TWO_IMPOSSIBLE = (255, 237, 240)
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)

    @staticmethod
    def drawRectangles(img, w, h, new_dictionary, mode):
        x, y, start = 100, 80, 9
        while y + 100 < h:
            while x + 120 < w:
                color = None
                if mode == "my_page":
                    if new_dictionary[x][y]:
                        color = Drawer.COLOR_IMPOSSIBLE
                    else:
                        color = Drawer.COLOR_WHITE
                elif mode == "group":
                    if len(new_dictionary[x][y]) == 0:
                        color = Drawer.COLOR_ALL_POSSIBLE
                    elif len(new_dictionary[x][y]) == 1:
                        color = Drawer.COLOR_ONE_IMPOSSIBLE
                    elif len(new_dictionary[x][y]) == 2:
                        color = Drawer.COLOR_TWO_IMPOSSIBLE
                    else:
                        color = Drawer.COLOR_IMPOSSIBLE

                cv2.rectangle(
                    img=img,
                    pt1=(x, y),
                    pt2=(x + 120, y + 100),
                    color=color,
                    thickness=-1,
                )
                cv2.rectangle(
                    img=img,
                    pt1=(x, y),
                    pt2=(x + 120, y + 100),
                    color=Drawer.COLOR_BLACK,
                    thickness=3,
                )

                x += 135

            x = 100

            cv2.putText(
                img=img,
                text=str(start).zfill(2),
                org=(x - 50, y + 30),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=Drawer.COLOR_BLACK,
                thickness=3,
                lineType=cv2.LINE_AA,
            )

            y += 135
            start += 1

        return img

    @staticmethod
    def drawTexts(img, w):
        x, y, start = 135, 50, 0
        days = {0: "MON", 1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN"}
        while x + 120 < w:
            cv2.putText(
                img,
                days[start],
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0)
                if start not in [5, 6]
                else (255, 0, 0)
                if start == 5
                else (0, 0, 255),
                3,
                cv2.LINE_AA,
            )
            x += 135
            start += 1

        return img

    @staticmethod
    def getInitialDictionary():
        new_dictionary = dict()
        for d_value in Drawer.DAYS.values():
            new_dictionary[d_value] = dict()
            for c_value in Drawer.CLASS_TIMES.values():
                new_dictionary[d_value][c_value] = []
        return new_dictionary

    @staticmethod
    def getImageFromTimeTableDictionary(timetable_dictionary, mode):
        new_dictionary = Drawer.getInitialDictionary()

        max_class_time = 0
        for key in timetable_dictionary.keys():  # key is "mon", "tue", ...
            new_key = Drawer.DAYS[key]  # new_key is 100, 235, ...
            for class_time in timetable_dictionary[
                key
            ]:  # class_time is 1, 2, 3, 4, ...
                max_class_time = max(max_class_time, int(class_time))
                new_class_time = Drawer.CLASS_TIMES[
                    int(class_time)
                ]  # new_class_time is 80, 215, 350, ...
                new_dictionary[new_key][new_class_time] = []
                for user_id in timetable_dictionary[key][class_time]:
                    new_dictionary[new_key][new_class_time].append(user_id)

        w, h = 1080, max(1920, (max_class_time + 1) * 135)
        img = np.full((h, w, 3), 255, np.uint8)
        img = Drawer.drawTexts(img, w)
        img = Drawer.drawRectangles(img, w, h, new_dictionary, mode)

        return img
