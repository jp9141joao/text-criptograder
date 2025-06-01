# 🔒 **Text Encryption/Decryption System** 🔓

An interactive program to encrypt and decrypt messages using multiple security levels. Based on random character substitutions, it serves as a practical demonstration of simple encryption techniques.

---

## 🚀 **Project Overview**

This project implements an interactive system for encrypting and decrypting messages using random character substitutions. It features multiple difficulty levels:

1. **Level 1 (Amateur)**: Basic character substitutions.
2. **Level 2 (Intermediate)**: More complex substitutions with varied characters.
3. **Level 3 (Military)**: Highest complexity, simulating advanced encryption patterns.

The code includes an interactive interface allowing users to choose between encrypting or decrypting messages and to specify the desired security level.

---

## 🛠️ **Key Features**

### Functionalities:

* **Encryption with multiple difficulty levels.**
  Security levels with their own substitution patterns.
* **Corresponding decryption for each level.**
  Ability to decrypt messages according to the selected level.
* **Interactive Interface with Simple Menu.**
  A clear navigation menu:

  ```
  * Option Menu *
  1- Encrypt
  2- Decrypt
  3- Exit
  ```
* **Randomized Base for Security**: Use of random patterns to make breaking the encryption more difficult.

---

## ⚙️ **Setup**

### Prerequisites

* Python 3.x must be installed on your system.

---

## ▶️ **How to Run**

1. Clone the repository to your local environment:

```bash
git clone https://github.com/jp9141joao/text-criptograder.git
```

2. Install any necessary dependencies (none required; the code does not rely on external packages).

3. Run the program with:

```bash
python your_file.py
```

---

## 🎮 **How It Works**

The basic flow is as follows:

1. Upon starting the program, the user will see a menu with options:

   ```
   * Option Menu *
   1- Encrypt
   2- Decrypt
   3- Exit
   ```

2. **Choose an Operation:**
   The user can choose to encrypt or decrypt messages.

3. **Select the difficulty level:**
   The program offers levels such as:

   * **Level 1**: Simple substitutions and basic patterns.
   * **Level 2**: Substitutions based on character variability.
   * **Level 3**: Highest level of randomness and complexity.

4. The user types the message, and the program performs the operation based on the selected level.

---

## 💬 **Technologies Used**

* **Python 3.x**: Core logic and string processing.
* System interaction with `os.system('cls')` for clean terminal updates.

---

## 💬 **Usage Example**

After starting the program, you will see the menu:

```
* Option Menu *
1- Encrypt
2- Decrypt
3- Exit
R: 1
Select the Encryption Level:
1- Amateur
2- Intermediate
3- Military
R: 1
Enter the string you want to encrypt: Test
Message successfully encrypted!
Your encrypted phrase is "Z$K8GDV7Â...etc"
```

---

## ⚙️ **Level Support**

The levels modify the complexity of encryption/decryption. The user selects the desired level from the menu:

1. **Level 1:** Simple substitutions and basic rules.
2. **Level 2:** More advanced substitutions.
3. **Level 3:** Complex substitutions, simulating advanced encryption levels.

---

Now you're ready to use and test this amazing encryption/decryption system! Good luck! 🔒✨
