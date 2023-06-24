import cv2

def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return
    cv2.namedWindow("Fullscreen Video", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Fullscreen Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Fullscreen Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def toi():
    answer = input("あなたはツイ廃ですか？(y/n)")
    if answer.lower() == "yes" or answer.lower() == "y":
        print("イ　ン　タ　ー　ネ　ッ　ト　さ　い　こ　う　！")
        play_video("yamero.mov")
        toi()

    elif answer.lower() == "no" or answer.lower() == "n":
        print("嘘つけ ばーか")
        toi()
    else:
        print("yかｎで入力しろアホ")
        toi()


toi()