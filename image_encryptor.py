from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)

    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):

            r, g, b = pixels[i, j]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[i, j] = (r, g, b)

    img.save("encrypted_image.png")

    print("Encrypted image saved as encrypted_image.png")


def decrypt_image(image_path, key):
    img = Image.open(image_path)

    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):

            r, g, b = pixels[i, j]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[i, j] = (r, g, b)

    img.save("decrypted_image.png")

    print("Decrypted image saved as decrypted_image.png")


while True:

    print("\n===== Image Encryption Tool =====")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':

        path = input("Enter image path: ")
        key = int(input("Enter key value: "))

        encrypt_image(path, key)

    elif choice == '2':

        path = input("Enter encrypted image path: ")
        key = int(input("Enter key value: "))

        decrypt_image(path, key)

    elif choice == '3':

        print("Program Ended.")
        break

    else:

        print("Invalid Choice")