# ADB Brute Force

## 📌 About
This script is an **Android PIN brute force tool** that uses **ADB (Android Debug Bridge)** to attempt unlocking an Android phone by trying different PIN combinations.

⚠️ **Disclaimer:** This tool is intended for educational and legal purposes only. Do not use it on devices you do not own or have explicit permission to access.

---

## 🚀 Features
✅ Supports **4-digit, 6-digit, and 8-digit PINs**
✅ Works on **PC (Windows/Linux) & Termux (Android)**
✅ **Randomized delays** to prevent easy detection
✅ **Automatic unlock detection** to stop when the PIN is found
✅ **Saves the correct PIN** to `found_password.txt`
✅ **Automatic ADB installation** (for Termux)

---

## 🖥️ Installation

### **For PC (Windows/Linux)**
1. **Install ADB**
   - **Windows:** [Download ADB](https://developer.android.com/studio/releases/platform-tools)
   - **Linux (Debian-based):**
     ```sh
     sudo apt update && sudo apt install adb -y
     ```
2. **Clone this repository:**
   ```sh
   git clone https://github.com/YOUR_USERNAME/ADB-Brute-Force.git
   cd ADB-Brute-Force
   ```
3. **Run the script:**
   ```sh
   python adb_brute_force.py -l 4
   ```
   *(Replace `4` with `6` or `8` for different PIN lengths)*

---

### **For Termux (Android)**
1. **Install ADB in Termux:**
   ```sh
   pkg update && pkg upgrade -y
   pkg install android-tools -y
   ```
2. **Clone this repository:**
   ```sh
   git clone https://github.com/YOUR_USERNAME/ADB-Brute-Force.git
   cd ADB-Brute-Force
   ```
3. **Run the script:**
   ```sh
   python adb_brute_force.py -l 4
   ```

---

## 🔍 How It Works
1. Connect the locked Android phone to your **PC or Termux**.
2. Enable **USB Debugging** (if not enabled, this method won’t work).
3. Run the script with the **desired PIN length**.
4. The script will try different PINs automatically.
5. If the correct PIN is found, it will be **displayed and saved**.

---

## ⚠️ Legal Warning
This tool should **only** be used on devices you own or have explicit permission to access. Unauthorized access to someone else’s device is **illegal** and punishable by law. The developer is not responsible for any misuse.

---

## 📜 License
MIT License - Free to use and modify with proper attribution.

---

## 🤝 Contributing
Feel free to fork this repository and submit pull requests to improve the tool!

---

## 🔗 Credits
Created by: **Zin**

