import pyautogui
import pytesseract
import time

# Optional: configure tesseract path if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(5)  # Time to switch to the browser

# Take screenshot of the Monkeytype words (adjust region)
# screenshot = pyautogui.screenshot(region=(130, 460, 1700, 190))
# screenshot = 'Screenshot.png'
# screenshot.show()
# text = pytesseract.image_to_string(screenshot)
# print(text)
# Clean and split text
# words = text.strip().split()
# print(words)
# Type the words
# for word in words:
#     pyautogui.typewrite(word + ' ', interval=0.05)

# words.remove('@')
# words.remove('english')
# words.remove('©')
# print(words)
count = 0
for i in range(10):
    screenshot = pyautogui.screenshot(region=(130, 460, 1700, 190))
    text = pytesseract.image_to_string(screenshot)
    print(text)
    words = text.strip().split()
    print(words)
    while count > 0 :
        onsc = pyautogui.screenshot(region=(130, 515, 1700, 95))
        text = pytesseract.image_to_string(onsc)
        print(text)
        words = text.strip().split()
        break
    for word in words:
        pyautogui.typewrite(word + ' ', interval=0.01) 
        count = count + 1
