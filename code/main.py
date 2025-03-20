import cv2
import numpy as np

# Constants (tunable parameters)
REFERENCE_IMAGE_PATH = "image1.jpg"
GOOD_MATCH_THRESHOLD = 0.6
MIN_GOOD_MATCHES = 20
RANSAC_REPROJECTION_THRESHOLD = 5.0
FLANN_TREES = 5


def detect_rotation_angle(frame, reference_image, sift, flann):
    """
    Detects the rotation angle of an object in a frame compared to a reference image.

    Args:
        frame (numpy.ndarray): The input frame from the camera.
        reference_image (numpy.ndarray): The grayscale reference image.
        sift (cv2.SIFT): SIFT feature detector object.
        flann (cv2.FlannBasedMatcher): FLANN matcher object.

    Returns:
        float: The rotation angle in degrees, or None if not enough good matches are found.
        numpy.ndarray: The image with matches drawn on it
    """

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp_grayframe, desc_grayframe = sift.detectAndCompute(grayframe, None)

    if desc_grayframe is None:
        return None, None  # No keypoints detected in the frame

    # Feature matching
    matches = flann.knnMatch(desc_image, desc_grayframe, k=2)

    # Applying the ratio test
    # List comprehension for conciseness
    good_points = [m for m, n in matches if m.distance <
                   GOOD_MATCH_THRESHOLD * n.distance]

    # Draw matches (move this outside the angle calculation for efficiency if just visualizing)
    img3 = cv2.drawMatches(reference_image, kp_img,
                           grayframe, kp_grayframe, good_points, None)

    if len(good_points) > MIN_GOOD_MATCHES:
        src_pts = np.float32(
            [kp_img[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        dst_pts = np.float32(
            [kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)

        # Estimate Transformation
        try:
            tform, mask = cv2.findHomography(
                dst_pts, src_pts, cv2.RANSAC, RANSAC_REPROJECTION_THRESHOLD)
        except:
            return None, img3
        # Angle Recovery
        thetaRecovered = np.arctan2(tform[1, 0], tform[0, 0]) * 180 / np.pi
        return thetaRecovered, img3
    else:
        return None, img3


# Initialization
img = cv2.imread(REFERENCE_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError(
        f"Reference image not found at {REFERENCE_IMAGE_PATH}")

cap = cv2.VideoCapture(0)  # Use 0 for the default camera

if not cap.isOpened():
    raise IOError("Cannot open webcam")

sift = cv2.SIFT.create()
kp_img, desc_image = sift.detectAndCompute(img, None)

if desc_image is None:
    raise ValueError(
        "No keypoints detected in the reference image.  Choose a different image.")


# FLANN = 0 is for KDTreeIndex
index_params = dict(algorithm=0, trees=FLANN_TREES)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)


while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    angle, img3 = detect_rotation_angle(frame, img, sift, flann)

    if angle is not None:
        print(f"Rotation Angle: {angle:.2f} degrees")

    cv2.imshow("Matches", img3)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
