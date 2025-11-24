# Invisible Cloak using OpenCV
A fun OpenCV project inspired by the Harry Potter invisibility cloak. This script detects a specific color (in this case sky blue), masks it out, and replaces it with the background to create an invisible-object illusion.

## How it works
### 1. Capture Background:
  &nbsp;&nbsp;&nbsp;&nbsp;The script takes a few frames at the start as your background.
### 2. Convert to HSV:
  &nbsp;&nbsp;&nbsp;&nbsp;The frame is converted from BGR → HSV because HSV makes color detection easier.
### 3. Create Mask:
  &nbsp;&nbsp;&nbsp;&nbsp;We detect the chosen color using lower/upper HSV ranges.
### 4. Refine Mask:
  &nbsp;&nbsp;&nbsp;&nbsp;Use dilation + opening to remove noise.
### 5. Replace Region:
  &nbsp;&nbsp;&nbsp;&nbsp;Wherever the mask finds the cloak, we replace that area with the background.

## Tech Stack
- Python
- Numpy
- OpenCV

## Installation
```bash
git clone https://https://github.com/shashwat2645/OpenCV-Projects
cd invisible-cloak
pip install opencv-python numpy
```

## How to run
```python
python bg.py
python cloak.py
```

## Adjusting Cloak Color
Open your code and tweak HSV ranges:
```bash
lb = np.array([0, 120, 70])
ub = np.array([10, 255, 255])
```
