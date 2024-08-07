# Algorithm
# Step 1: Import necessary modules.
# Step 2: Define the file path and name for saving the screenshot.
# Step 3: Capture the full screen using pyscreenshot.grab()
# Step 4: Display the captured image using image.show() (optional).
# Step 5: Save the captured image using image.save() with the specified file path.
# Step 6: Define the bounding box coordinates for the area to capture (in the format (x1, y1, x2, y2)).
# Step 7: Capture the specified area using pyscreenshot.grab(bbox=(x1, y1, x2, y2)).
# Step 8: Display the captured image using image.show() (optional).
# Step 9: Save the captured image using image.save() with the specified file path.
# Step 10: Retrieve the current working directory using os.getcwd().
# Step 11: Construct and print the full path to the saved screenshot file.

# Step 1: Import necessary modules
import pyscreenshot
import os

# Step 2: Define the file path and name for saving the screenshot
filename = "screenshot.png"  # You can customize the file name
filepath = os.path.join(os.getcwd(), filename)


# # Step 3: Capture the full screen
# image = pyscreenshot.grab()

# # Step 4: Display the captured image (optional)
# image.show()

# # Step 5: Save the captured image
# image.save(filepath)

# Step 6: Define the bounding box coordinates for partial screen capture
bbox = (10, 10, 500, 500)  # Customize these coordinates as needed

# Step 7: Capture the specified area of the screen
partial_image = pyscreenshot.grab(bbox=bbox)

# Step 8: Display the captured partial image (optional)
partial_image.show()

# Step 9: Save the captured partial image
partial_filepath = os.path.join(os.getcwd(), "partial_" + filename)
partial_image.save(partial_filepath)

# Step 10: Retrieve the current working directory
cwd = os.getcwd()

# # Step 11: Print the full path to the saved screenshot files
# print(f"Full screenshot saved at: {filepath}")
# print(f"Partial screenshot saved at: {partial_filepath}")


