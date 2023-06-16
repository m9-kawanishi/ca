import os
# opencvをインポートする前にこの処理を加えると起動が早くなる
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2, sys

cap = cv2.VideoCapture(0)
# 画像サイズを設定
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
# FPSを設定
cap.set(cv2.CAP_PROP_FPS, 60)
# オートフォーカスをオフ
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
# フォーカス値を設定
cap.set(cv2.CAP_PROP_FOCUS, 0)
cv2.namedWindow("manual_focus", cv2.WINDOW_NORMAL)

# 表示用に画像サイズを変更
edt_h = int(480)
edt_w = int(640)
cv2.resizeWindow("manual_focus", edt_w, edt_h) 
print("終了したいときには「q」を押してね")

# 映像を表示
while cap.isOpened():
    _, img = cap.read()
    cv2.imshow("manual_focus", img)
    key = cv2.waitKey(1)
    # qキーを押すと終了
    if key == ord('q'):
        break
    if key == ord('f'):
        focus = int(input("フォーカス値を入力して(0~1000)"))
        cap.set(cv2.CAP_PROP_FOCUS, focus)
cv2.destroyAllWindows()
cap.release()
