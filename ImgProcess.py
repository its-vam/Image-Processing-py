import cv2

def load_image(image_path):
    # Load an image from the specified path
    image = cv2.imread(image_path)
    return image

def resize_image(image, width, height):
    # Resize the image to the specified dimensions
    resized_image = cv2.resize(image, (width, height))
    return resized_image

def crop_image(image, x, y, width, height):
    # Crop a region of interest from the image
    cropped_image = image[y:y+height, x:x+width]
    return cropped_image

def apply_filter(image, filter_type):
    # Apply basic image filters (e.g., blur, sharpen)
    if filter_type == 'blur':
        processed_image = cv2.GaussianBlur(image, (5, 5), 0)
    elif filter_type == 'sharpen':
        kernel = numpy.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        processed_image = cv2.filter2D(image, -1, kernel)
    return processed_image

def save_image(image, output_path):
    # Save the processed image to the specified output path
    cv2.imwrite(output_path, image)

if __name__ == "__main__":
    # User interaction and CLI
    image_path = input("Enter the path of the image: ")
    image = load_image(image_path)
    
    print("Select an operation:")
    print("1. Resize Image")
    print("2. Crop Image")
    print("3. Apply Filter")
    
    operation = int(input("Enter the operation number: "))
    
    if operation == 1:
        width = int(input("Enter the new width: "))
        height = int(input("Enter the new height: "))
        processed_image = resize_image(image, width, height)
    elif operation == 2:
        x = int(input("Enter x-coordinate: "))
        y = int(input("Enter y-coordinate: "))
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        processed_image = crop_image(image, x, y, width, height)
    elif operation == 3:
        filter_type = input("Enter filter type (blur or sharpen): ")
        processed_image = apply_filter(image, filter_type)
    
    output_path = input("Enter the path to save the processed image: ")
    save_image(processed_image, output_path)
