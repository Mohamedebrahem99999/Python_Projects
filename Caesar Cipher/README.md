# Caesar Cipher Tool 🔐

A simple yet effective Python implementation of the classic **Caesar Cipher** algorithm for encrypting and decrypting text.

## 📝 Description
This tool allows users to encrypt or decrypt messages by shifting letters in the alphabet by a fixed number. It handles:
- Uppercase and Lowercase letters.
- Symbols, spaces, and numbers (remains unchanged).
- Input validation for shift values.

---
### بالعربية 🇪🇬
أداة بسيطة بلغة بايثون لتشفير وفك تشفير النصوص باستخدام **شفرة القيصر**.
- تدعم الحروف الكبيرة والصغيرة.
- تحافظ على الرموز والمسافات كما هي.
- تحتوي على نظام للتحقق من صحة المدخلات.

## 🚀 How to use
1. Make sure you have **Python 3.x** installed.
2. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/caesar-cipher-python.git](https://github.com/YOUR_USERNAME/caesar-cipher-python.git)
3. Run the script: Caesar Cipher.py
4. Follow the on-screen instructions to enter your message and shift value

🛠️ Logic Used
Alphabet Mapping: Using Python's string.ascii_lowercase and a dictionary for faster lookup (O(1) complexity).

Modulo Arithmetic: The core formula used is: (index + shift) % 26. This ensures the shift stays within the 26 letters of the alphabet.

Reusability: The decrypt function is a simple wrapper that calls the encrypt function with a negative shift, making the code cleaner and easier to maintain.

## 📜 License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
