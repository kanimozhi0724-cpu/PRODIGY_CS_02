Task 02 – Pixel Manipulation for Image Encryption (Overview)

Objective:
Develop a simple image encryption and decryption program using pixel manipulation techniques in Python. The program should modify the pixel values of an image so that the original image becomes unreadable, and then restore it back using the same key.

Concept

Digital images are made up of pixels, where each pixel contains color values (Red, Green, Blue). By performing mathematical operations on these values, we can encrypt the image.

Common operations include:

Addition: new_pixel = old_pixel + key
Subtraction: new_pixel = encrypted_pixel - key
Bitwise XOR: new_pixel = old_pixel XOR key

The same key used for encryption is required for decryption.

Working Procedure
Encryption
Read the input image.
Ask the user to enter an encryption key.
Traverse through each pixel of the image.
Modify the RGB values using the chosen operation (e.g., addition modulo 256).
Save the encrypted image.
Decryption
Read the encrypted image.
Enter the same key used during encryption.
Reverse the pixel manipulation operation.
Save the decrypted image.
The output image should match the original image.
Tools Used
Programming Language: Python
Libraries:
Pillow (PIL) – for image processing
NumPy (optional) – for efficient pixel operations
Algorithm

Encryption:

Input image and key
Open the image
For each pixel:
    pixel = (pixel + key) mod 256
Save encrypted image

Decryption:

Input encrypted image and key
Open the encrypted image
For each pixel:
    pixel = (pixel - key) mod 256
Save decrypted image
Applications
Basic understanding of image encryption techniques.
Learning how pixel-level manipulation works.
Demonstrating the principles of symmetric key cryptography.
Educational projects in cybersecurity and digital image processing.
Limitations
This method provides basic security and is not suitable for protecting highly sensitive data.
If an attacker knows the algorithm and key, the image can be decrypted easily.
Advanced encryption standards are required for real-world security applications.
Conclusion

This task demonstrates how image data can be secured by manipulating pixel values using a secret key. It helps in understanding the fundamentals of encryption, image processing, and Python programming through a practical implementation of a simple symmetric encryption technique.
