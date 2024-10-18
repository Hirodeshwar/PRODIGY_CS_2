from PIL import Image


def encrypt_image(image_path, shift_value):
    img = Image.open(image_path)  
    pixels = img.load()  
    
    for i in range(img.size[0]):  
        for j in range(img.size[1]): 
            r, g, b = pixels[i, j]  
            
            pixels[i, j] = ((r + shift_value) % 256, (g + shift_value) % 256, (b + shift_value) % 256)
    
    img.save("encrypted_image.png") 
    print("Encryption complete. Saved as 'encrypted_image.png'.")


def decrypt_image(image_path, shift_value):
    img = Image.open(image_path)  
    pixels = img.load()  
    
    for i in range(img.size[0]):  
        for j in range(img.size[1]):  
            r, g, b = pixels[i, j]  
          
            pixels[i, j] = ((r - shift_value) % 256, (g - shift_value) % 256, (b - shift_value) % 256)
    
    img.save("decrypted_image.png")  
    print("Decryption complete. Saved as 'decrypted_image.png'.")


choice = input("Do you want to (E)ncrypt or (D)ecrypt the image?: ").lower()

if choice == 'e':
    image_path = input("Enter the image path: ").strip()  
    shift_value = int(input("Enter shift value for encryption: "))
    encrypt_image(image_path, shift_value)

elif choice == 'd':
    image_path = input("Enter the image path: ").strip()
    shift_value = int(input("Enter shift value for decryption: "))
    decrypt_image(image_path, shift_value)

else:
    print("Invalid choice!")
