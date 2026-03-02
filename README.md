🛡️ Cyber Security Internship – Month 2 Project

Submitted by: Shumaila Arif
Date: March 27, 2026
Organization: Arch Technologies

📌 Project Overview

This project demonstrates practical implementation of both reactive (Digital Forensics) and proactive (Machine Learning) cybersecurity techniques.

The internship tasks focus on real-world security challenges including data recovery and fraud detection.

🎯 Key Objectives

Recover deleted files using forensic tools

Understand FAT32/NTFS file system behavior

Develop a Machine Learning fraud detection model

Handle imbalanced datasets effectively

Evaluate model performance using professional metrics

🔍 Task 3: Lost Data Retrieval (Digital Forensics)
🎯 Objective

To simulate accidental file deletion from a storage device and recover the data using forensic tools.
This demonstrates that deleted files remain recoverable until overwritten.

🛠️ Tools & Environment

Operating System: Kali Linux

Storage Device: 8GB USB Flash Drive (FAT32/NTFS)

Forensic Tool: TestDisk (Open-source Data Recovery Utility)

Commands Used: rm, sudo testdisk, lsblk, mount, ls -l

⚙️ Methodology

Created a test file shumaila_report.docx on the mounted USB.

Deleted the file using the rm command.

Launched TestDisk with root privileges.

Selected the USB device and used the Undelete option.

Scanned the Master File Table (MFT).

Recovered the deleted file to /home/shumaila44.

Verified recovery using ls -l.

💡 Security Insight

Deleted files are not immediately erased from storage.

Data remains recoverable until overwritten.

Secure wiping tools are necessary to prevent data leakage.

Digital forensics plays a vital role in cybercrime investigations.

💳 Task 4: Credit Card Fraud Detection (Machine Learning)
🎯 Objective

To build a Machine Learning model capable of detecting fraudulent credit card transactions using transaction features such as:

Time

Amount

Anonymized variables (V1, V2, etc.)

🛠️ Tools & Environment

Language: Python 3

Libraries: Pandas, NumPy, Scikit-learn

Algorithm: Random Forest Classifier

📊 Dataset & Preprocessing

1,000 synthetic transaction records

0 = Legitimate

1 = Fraud

70% Training / 30% Testing split

Handled class imbalance using class_weight='balanced'

⚙️ Model Execution

The model was executed using:

python3 fraud_detection.py
📈 Evaluation Metrics

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

📊 Results Summary
Metric	Result
Accuracy	76%
Model Used	Random Forest
Legitimate Correctly Identified	228
🏁 Final Conclusion

This internship project successfully combined:

Digital Forensics

Secure Data Handling

Artificial Intelligence

Risk Analysis

The tasks strengthened practical knowledge of modern cybersecurity defense mechanisms and real-world threat detection strategies.
