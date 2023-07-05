class TableDetector:
    import os

    ANDROID_MODES_BY_RED = {17: "DARK", 255: "LIGHT"}
    ANDROID_LINE_COLOR = {"DARK": 49, "LIGHT": 237}
    ANDROID_BACKGROUND_COLOR = {"DARK": 17, "LIGHT": 255}
    ANDROID_PIXEL_ERROR_TOLERANCE = 5
    DATE = {0: "mon", 1: "tue", 2: "wed", 3: "thu", 4: "fri", 5: "sat", 6: "sun"}
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    BASE_PATH = BASE_PATH[: BASE_PATH.find("w2m") - 1]

    @staticmethod
    def getUnavailableDatetime(file_path_list):
        """opencv-python 설치 필요 >> pip install opencv-python"""
        """
        JSON return
        형식은 다음과 같습니다.
        
        {
        "mon": [6, 7, 8, 9],
        "tue": [1, 2, 6, 7, 11, 12, 13],
        "wed": [1, 2, 5, 6, 7], 
        "thu": [1, 2, 3, 5, 11, 12, 13],
        "fri": [1, 2, 3, 6, 7],
        "sat": [],
        "sun": []
        }
        
        """

        import cv2, json

        # 수업있는 시간대
        unavailable_datetimes = {
            "mon": set(),
            "tue": set(),
            "wed": set(),
            "thu": set(),
            "fri": set(),
            "sat": set(),
            "sun": set(),
        }

        # 이미지 읽기, 모드 검출
        for file_path in file_path_list:
            # 선분 교차 좌표
            Xs, Ys = [], []

            img = cv2.imread(TableDetector.BASE_PATH + file_path)
            mode = TableDetector.ANDROID_MODES_BY_RED[img[0][0][0]]

            # 모드별 감지 색상 지정
            LINE_COLOR = TableDetector.ANDROID_LINE_COLOR[mode]
            BACKGROUND_COLOR = TableDetector.ANDROID_BACKGROUND_COLOR[mode]

            # 가로 선 검출(행)
            for x in range(0, len(img)):
                if img[x][0][0] == LINE_COLOR:
                    if not Xs:
                        Xs.append(x)
                    elif abs(Xs[-1] - x) > TableDetector.ANDROID_PIXEL_ERROR_TOLERANCE:
                        Xs.append(x)
            Xs.pop()

            # 세로 선 검출(열)
            for y in range(0, len(img[0])):
                if img[0][y][0] == LINE_COLOR:
                    if not Ys:
                        Ys.append(y)
                    elif abs(Ys[-1] - y) > TableDetector.ANDROID_PIXEL_ERROR_TOLERANCE:
                        Ys.append(y)

            # 고정점으로부터 추정점까지의 변위
            x_gap_5 = int((Xs[1] - Xs[0]) * 0.05)
            y_gap_95 = int((Ys[1] - Ys[0]) * 0.95)

            # 추정점 셀 컬러 확인
            for j, y in enumerate(Ys):
                for i, x in enumerate(Xs):
                    search_x, search_y = x + x_gap_5, y + y_gap_95

                    # 범위 내
                    if not (
                        0 <= search_x <= img.shape[0] and 0 <= search_y <= img.shape[1]
                    ):
                        continue

                    cv2.circle(img, (search_y, search_x), 5, (255, 0, 0), 3)

                    # 공강 상태가 아니라면
                    if img[search_x][search_y][0] != BACKGROUND_COLOR:
                        unavailable_datetimes[TableDetector.DATE[j]].add(i + 1)

        for key in unavailable_datetimes.keys():
            unavailable_datetimes[key] = [*sorted(unavailable_datetimes[key])]

        return unavailable_datetimes


# # 테스트 코드(검토 후 삭제 가능)
# while True:
#     print(
#         """

#         사용 방법 : 시간표 파일 이름들을 공백으로 쭉 적어줍니다.
#         한 명이면 하나만 적어도 됩니다.

#         ex) 한 명   >> d1
#         ex) 여러명  >> d1 l3 l4 d2

#         작성 후 엔터를 입력하면 모든 사람들의 경우를 고려한 불가능한 시간대를 생성해줍니다.

#         """
#     )

#     file_names = input("파일명만 여러 개 공백으로 구분하여 입력 >> ")
#     if file_names == "exit":
#         break

#     generatePath = lambda file_name: "../src/img/detection_images/" + file_name + ".jpg"
#     print(TableDetector.getUnavailableDatetime(map(generatePath, file_names.split())))
