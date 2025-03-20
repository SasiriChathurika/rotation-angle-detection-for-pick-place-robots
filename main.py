import cv2
import numpy as np
#import matplotlib.pyplot as plt

# Addition of sources
img = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)
cap = cv2.VideoCapture(0)

# Feature points of the template
# Detecting key points
sift = cv2.SIFT.create()
kp_img, desc_image = sift.detectAndCompute(img, None)

# Feature matcher
index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)

while True:
    _, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp_grayframe, desc_grayframe = sift.detectAndCompute(grayframe, None)
    # Feature matching
    matches = flann.knnMatch(desc_image, desc_grayframe, k=2)
    good_points = []

    # Applying the ratio test

    for m, n in matches:
        if m.distance < 0.6 * n.distance:
            good_points.append(m)

    img3 = cv2.drawMatches(img, kp_img, grayframe, kp_grayframe, good_points, grayframe)

    # Homogrphy
    # if len(good_points) > 20:
    #     query_pts = np.float32([kp_img[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
    #     train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
    #     matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
    #     matches_mask = mask.ravel().tolist()
    #
    #     # Perspective Transform
    #     h, w = img.shape
    #     pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
    #     dst = cv2.perspectiveTransform(pts, matrix)
    #
    #     homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)
    #     cv2.imshow("Homography", homography)

    if len(good_points) > 20:
        src_pts = np.float32([kp_img[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)

        # Estimate Transformation
        tform, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        # Angle Recovery for rotation angle detection
        # scaleRecovered = np.sqrt(tform[1, 0] ** 2 + tform[0, 0] ** 2)
        thetaRecovered = np.arctan2(tform[1, 0], tform[0, 0]) * 180 / np.pi

        print(thetaRecovered)

    cv2.imshow("img3", img3)
    # print(good_points)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
