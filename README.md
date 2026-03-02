# 🛡️ Cyber Security Internship – Month 2 Project

**Submitted by:** Shumaila Arif  
**Date:** March 27, 2026  
**Organization:** Arch Technologies

---

## 📌 Project Overview
This project demonstrates the practical implementation of both **reactive** (Digital Forensics) and **proactive** (Machine Learning) cybersecurity techniques. These internship tasks focus on real-world security challenges, including data recovery and fraud detection.

### 🎯 Key Objectives
* Recover deleted files using forensic tools .
* Understand FAT32/NTFS file system behavior .
* Develop a Machine Learning fraud detection model .
* Handle imbalanced datasets effectively.
* Evaluate model performance using professional metrics .

---

## 🔍 Task 3: Lost Data Retrieval (Digital Forensics)

### 🎯 Objective
To simulate accidental file deletion from a storage device and recover the data using forensic tools [31]. This demonstrates that deleted files remain recoverable until the system marks their storage space as overwritten [32, 33].

### 🛠️ Tools & Environment
* **Operating System:** Kali Linux 
* **Storage Device:** 8GB USB Flash Drive 
* **File System:** FAT32/NTFS 
* **Forensic Tool:** TestDisk (Open-source Data Recovery Utility) 
* **Commands Used:** `rm`, `sudo testdisk`, `mount`, `ls -l`, `touch`

### ⚙️ Methodology
1. **Scenario Creation:** Created a test file `shumaila_report.docx` on the mounted USB .
2. **Deletion:** Deleted the file using the `rm` command to simulate accidental loss.
3. **Launching TestDisk:** Executed `sudo testdisk` with root privileges .
4. **Analysis:** Selected the USB device `/dev/sdb` and the correct partition table .
5. **Undelete Process:** Used the "Advanced" options and "Undelete" feature to scan the file system .
6. **Recovery:** Selected the deleted file and copied it to the destination path `/home/shumaila44`.
7. **Verification:** Verified the recovery using the `ls -l` command .

### 💡 Security Insight
* Deleted files are not immediately erased; the OS only removes the reference from the file table.
* Data remains recoverable until the physical clusters are overwritten.
* Secure wiping tools are necessary for organizations to prevent data leakage .

---

## 💳 Task 4: Credit Card Fraud Detection (Machine Learning)

### 🎯 Objective
To build a Machine Learning model capable of detecting fraudulent credit card transactions using features such as Transaction Time, Amount, and anonymized variables (V1, V2) .

### 🛠️ Tools & Environment
* **Language:** Python 3 
* **Libraries:** Pandas, NumPy, Scikit-learn 
* **Algorithm:** Random Forest Classifier 

### 📊 Dataset & Preprocessing
* **Data:** 1,000 synthetic transaction records (0 = Legitimate, 1 = Fraud) .
* **Split:** 70% Training and 30% Testing data .
* **Class Imbalance:** Handled using `class_weight='balanced'` to give importance to minority fraud cases.

### ⚙️ Model Execution
The model was executed in the Kali terminal using:
`python3 fraud_detection.py` 

### 📈 Evaluation Metrics
The model was evaluated using:
* Accuracy, Precision, and Recall .
* F1-Score and Confusion Matrix.

### 📊 Results Summary
| Metric | Result |
| :--- | :--- |
| **Overall Accuracy** | 76% |
| **Model Used** | Random Forest  |
| **Legitimate Correctly Identified** | 228  |

---

## 🏁 Final Conclusion
This Month 2 internship project successfully demonstrated the intersection of **reactive** and **proactive** cybersecurity techniques. Through these tasks, I have achieved:

**Forensic Proficiency**: Recovered deleted data using `TestDisk`, highlighting the importance of understanding file systems and data recovery mechanisms.
**Advanced Threat Detection**: Developed a Machine Learning system using **Random Forest** that successfully handled imbalanced financial data.
**Analytical Skills**: Evaluated model performance using multiple professional metrics like **Recall**, **Precision**, and **Confusion Matrices** to ensure reliability.
**Strategic Understanding**: Combined **Digital Forensics**, **Secure Data Handling**, **Artificial Intelligence**, and **Risk Analysis** to strengthen my practical knowledge of modern defense mechanisms.

The project has provided a solid foundation in real-world threat detection and forensic investigation strategies.

---

---
