import cv2
import numpy as np

# Create a synthetic image with shapes for demonstration
def create_sample_image():
    # Create a blank white image
    img = np.ones((400, 600, 3), dtype=np.uint8) * 255
    
    # Draw a triangle
    triangle = np.array([[100, 50], [50, 150], [150, 150]], np.int32)
    cv2.fillPoly(img, [triangle], (200, 100, 100))
    
    # Draw a rectangle
    cv2.rectangle(img, (200, 50), (300, 150), (100, 200, 100), -1)
    
    # Draw a pentagon
    pentagon = np.array([[400, 50], [370, 120], [400, 190], [460, 190], [490, 120]], np.int32)
    cv2.fillPoly(img, [pentagon], (100, 100, 200))
    
    # Draw a circle
    cv2.circle(img, (150, 280), 50, (200, 200, 100), -1)
    
    # Draw a hexagon
    hexagon = np.array([[300, 230], [270, 280], [300, 330], [360, 330], [390, 280], [360, 230]], np.int32)
    cv2.fillPoly(img, [hexagon], (200, 100, 200))
    
    return img

# Create sample image
image = create_sample_image()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, thres = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours
cv2.drawContours(image, contours, -1, (0, 0, 0), 2)

# Process each contour
for contour in contours:
    # Approximate the contour
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    
    # Skip small contours
    if perimeter < 100:
        continue
        
    corners = len(approx)
    
    # Determine shape based on number of corners
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        # Check if it's a square or rectangle
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            shape_name = "Square"
        else:
            shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners == 6:
        shape_name = "Hexagon"
    elif corners > 10:
        shape_name = "Circle"
    else:
        shape_name = f"Shape({corners})"
    
    # Draw the contour and label
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
    
    # Get position for text
    x = approx[0][0][0]
    y = approx[0][0][1] - 10
    
    # Put the shape name
    cv2.putText(image, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# Display the result
cv2.imshow("Shape Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()