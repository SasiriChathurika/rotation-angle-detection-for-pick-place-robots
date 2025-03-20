# Rotation Angle Detection for Pick&Place Robots in Conveyor Belts or Fixed Locations

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/SasiriChathurika/rotation-angle-detection-for-pick-place-robots/blob/main/CONTRIBUTING.md)

**This code was solely developed by Sasiri Chathurika.**

This system employs computer vision techniques to accurately determine the rotation angle of objects on a static or moving conveyor belt or in fixed locations.  By providing precise orientation information, this system contributes to the field of robotics by enabling more efficient and flexible automated pick-and-place operations. This allows robots to adapt to varying object orientations without requiring precise pre-alignment. The system is designed for seamless integration with pick-and-place robotic systems, enabling automated object handling and reducing the need for manual intervention. It utilizes OpenCV, NumPy, and feature matching (SIFT, FLANN) to achieve robust and reliable angle detection.  The system offers cost-effective and easily deployable solutions to automate pick and place tasks by improving the flexibility and efficiency of robotic arm operations.

**Note:** This version does *not* include camera calibration. Accuracy may be affected by lens distortion.

## Table of Contents

*   [Features](#features)
*   [Installation](#installation)
*   [Usage](#usage)
    *   [Basic Usage](#basic-usage)
    *   [Advanced Usage: Tuning Parameters](#advanced-usage-tuning-parameters)
*   [Data Format](#data-format)
*   [Contributing](#contributing)
*   [License](#license)
*   [Acknowledgments](#acknowledgments)

## Features

*   **Rotation Angle Detection:** Accurately determines the rotation angle of objects, enabling robots to grasp objects regardless of their orientation. This is a direct improvement in pick and place applications compared to traditional approaches which requires complex pre-alignment systems.
*   **Real-Time Processing:** Processes video frames in real-time for timely angle updates, allowing for responsive robot control in dynamic environments.
*   **Feature-Based Matching:** Utilizes SIFT features and FLANN matching for robust object recognition, improving reliability compared to systems relying on template matching.
*   **Homography Estimation:** Employs homography estimation with RANSAC for accurate transformation calculation, enabling precise robot movements even with imperfect image data.
*   **Pick-and-Place Integration:** Designed for easy integration with pick-and-place robotic systems, simplifying the deployment of automated solutions in manufacturing and logistics.  This offers improved adaptability to changing object positions and orientations.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/SasiriChathurika/rotation-angle-detection-for-pick-place-robots.git
    cd rotation-angle-detection-for-pick-place-robots
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Basic Usage

1.  **Prepare the reference image:** Ensure your reference image (in my case `image1.jpg`) is located in the `data/` directory.  Ensure this image is well lit and with a high resolution for better results.

2.  **Run the main script:**

    ```bash
    python code/main.py
    ```

    This will open a window displaying the live camera feed with feature matching and the calculated rotation angle printed to the console.  Press `Esc` to exit.

### Advanced Usage: Tuning Parameters

The performance of the system can be improved by adjusting the parameters used for feature matching and homography estimation. Key parameters include:

*   **Ratio Test Threshold:** The threshold used in the ratio test to filter good matches (currently set to 0.6). Lowering this value will result in fewer matches being accepted, but potentially more accurate matches.
*   **Minimum Good Points:** The minimum number of good matches required to estimate the homography (currently set to 20). Increasing this value will make the system more robust to noise, but may also reduce the number of frames where a rotation angle is detected.
*   **RANSAC Threshold:** The threshold used in the RANSAC algorithm for homography estimation (currently set to 5.0). Lowering this value will make the algorithm more sensitive to outliers, while increasing it will make it more robust.

These parameters can be adjusted directly in the `code/main.py` script. Experimenting with different values may improve the accuracy and robustness of the system for your specific application.

## Data Format

*   **`data/image1.jpg`:** The reference image used for feature matching.  Ensure this image is clear, well-lit, and representative of the objects you are trying to detect.

## Contributing

We welcome contributions to this project!  Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute. This includes:

*   Reporting bugs
*   Suggesting new features
*   Submitting pull requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This system was solely developed by **Sasiri Chathurika**.

*   This project utilizes the OpenCV library: [https://opencv.org/](https://opencv.org/)
*   The FLANN library is used for efficient feature matching: [https://www.cs.ubc.ca/research/flann/](https://www.cs.ubc.ca/research/flann/)
*   Thank you to the open-source community for providing valuable resources and tools.
