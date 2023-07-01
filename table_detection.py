def getUnavailableDatetime(file_path):

    """opencv-python 설치 필요"""
    """pip install opencv-python"""
    
    import cv2, json
    
    
    # 상수 딕셔너리
    MODES = {17: "DARK", 255: "LIGHT"}
    DATE = {0: "mon", 1: "tue", 2: "wed", 3: "thu", 4: "fri", 5: "sat", 6: "sun"}
    
    # 선분 교차 좌표
    Xs, Ys = [], []
    
    
    # 수업있는 시간대
    unavailable_datetimes = {"mon": [], "tue": [], "wed": [], "thu": [], "fri": [], "sat": [], "sun": []}
    
    
    # 이미지 읽기, 모드 검출
    img = cv2.imread(file_path)
    mode = MODES[img[0][0][0]]
    
    
    # 모드별 감지 색상 지정
    LINE_COLOR = 49 if mode == 'DARK' else 237
    BACKGROUND_COLOR = 17 if mode == 'DARK' else 255
    
    
    # 가로 선 검출(행)
    for x in range(0, len(img)):
        if img[x][0][0] == LINE_COLOR:
            if not Xs: Xs.append(x)
            elif abs(Xs[-1] - x) > 5: Xs.append(x)
    Xs.pop()
    
    # 세로 선 검출(열)
    for y in range(0, len(img[0])):
        if img[0][y][0] == LINE_COLOR:
            if not Ys: Ys.append(y)
            elif abs(Ys[-1] - y) > 5: Ys.append(y)

    
    
    # 고정점으로부터 추정점까지의 변위(x: 거의 아랫쪽(95%), y: 중간(50%))
    x_gap_95 = int((Xs[1] - Xs[0]) * 0.95)
    y_gap_50 = int((Ys[1] - Ys[0]) * 0.5)
    
    
    # 추정점 셀 컬러 확인
    for j, y in enumerate(Ys):
        for i, x in enumerate(Xs):
            search_x, search_y = x+x_gap_95, y+y_gap_50
            
            # 범위 내
            if not (0 <= search_x <= img.shape[0] and 0 <= search_y <= img.shape[1]):
                continue
                    
            # 공강 상태가 아니라면
            if img[search_x][search_y][0] != BACKGROUND_COLOR:
                unavailable_datetimes[DATE[j]].append(i+1)

    
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
    return json.dumps(unavailable_datetimes)


# 테스트 코드(검토 후 삭제 가능)
for file_name in ['d1', 'd2', 'd3', 'd4', 'l1', 'l2', 'l3', 'l4', 'omg']:
    print(getUnavailableDatetime("src/img/detection_images/" + file_name + ".jpg"))