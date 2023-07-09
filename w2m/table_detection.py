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
    def getUnavailableDatetime(file_path: str, unavailable_datetimes: dict, user_id):
        import cv2

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
                    if str(i + 1) not in unavailable_datetimes[TableDetector.DATE[j]]:
                        unavailable_datetimes[TableDetector.DATE[j]][str(i + 1)] = [
                            user_id
                        ]
                    else:
                        unavailable_datetimes[TableDetector.DATE[j]][str(i + 1)].append(
                            user_id
                        )

        sorted_unavailable_datetimes = dict()

        for key in TableDetector.DATE.values():
            sorted_unavailable_datetimes[key] = dict()

        for key in TableDetector.DATE.values():  # mon, tue, wed, thu, fri, sat, sun
            sorted_keys = map(str, sorted(map(int, unavailable_datetimes[key].keys())))

            for sorted_key in sorted_keys:
                sorted_unavailable_datetimes[key][sorted_key] = unavailable_datetimes[
                    key
                ][sorted_key]

        return sorted_unavailable_datetimes
