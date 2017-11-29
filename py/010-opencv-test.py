import cv2


def test_camera(url):
    cap = cv2.VideoCapture(url)
    print(cap.isOpened())
    while True:
        frame = cap.grab()
        print(frame.cols, frame.rows)


if __name__ == '__main__':
    test_camera('rtsp://admin:admin123@10.168.1.38:554/Streaming/Channels/102')
