# 🚀 คู่มือการติดตั้ง Streamlit สำหรับผู้เริ่มต้น
> เริ่มต้นสร้าง Web Application ด้วย **Python + Streamlit**

---

# Streamlit คืออะไร

**Streamlit** เป็น Framework สำหรับสร้าง **Web Application** ด้วยภาษา **Python** โดยไม่จำเป็นต้องมีความรู้ด้าน Frontend มาก่อน

เหมาะสำหรับ

- 📊 Data Science
- 🤖 AI / Machine Learning
- 📈 Dashboard
- 📝 CRUD Web Application
- 🎓 ใช้ประกอบการเรียนการสอน Python

---

# ✨ ข้อดีของ Streamlit

- ✅ ไม่ต้องเขียน HTML
- ✅ ไม่ต้องเขียน CSS
- ✅ ไม่ต้องเขียน JavaScript
- ✅ ใช้ Python เพียงภาษาเดียว
- ✅ เขียนโปรแกรมได้รวดเร็ว
- ✅ เหมาะสำหรับผู้เริ่มต้น
- ✅ เรียนรู้ได้ง่าย
- ✅ มี Community ขนาดใหญ่

---

# ขั้นตอนที่ 1 ติดตั้ง Python

## 1.1 ตรวจสอบว่า Python ติดตั้งแล้วหรือไม่

เปิด **Command Prompt** หรือ **PowerShell**

```bash
python --version
```

หรือ

```bash
python3 --version
```

ตัวอย่างผลลัพธ์

```text
Python 3.13.5
```

---

## 1.2 หากยังไม่ได้ติดตั้ง Python

สำหรับ Windows (แนะนำ)

```bash
winget install Python.Python.3 --scope machine
```

> ต้องเปิด PowerShell ด้วยสิทธิ์ Administrator

---

## 1.3 ตรวจสอบตำแหน่งที่ติดตั้ง

```bash
where python
```

ตัวอย่าง

```text
C:\Program Files\Python313\python.exe
```

---

# ขั้นตอนที่ 2 อัปเดต pip

`pip` คือโปรแกรมสำหรับติดตั้ง Library ของ Python

อัปเดตเป็นเวอร์ชันล่าสุด

```bash
python -m pip install --upgrade pip
```

ตรวจสอบเวอร์ชัน

```bash
pip --version
```

ตัวอย่าง

```text
pip 25.1.1 from ...
```

---

# 🐍 ขั้นตอนการสร้าง Virtual Environment (venv)
Virtual Environment (venv) คือสภาพแวดล้อมแยกสำหรับแต่ละโปรเจกต์ Python ทำให้สามารถติดตั้งไลบรารีเฉพาะโปรเจกต์ได้ โดยไม่กระทบกับ Python หลักของเครื่อง
ข้อดีของ Virtual Environment

- ✅ แยกไลบรารีของแต่ละโปรเจกต์
- ✅ ป้องกันปัญหาเวอร์ชันของไลบรารีชนกัน
- ✅ แชร์โปรเจกต์ให้ผู้อื่นได้ง่าย
- ✅ ใช้งานร่วมกับ GitHub ได้สะดวก
- ✅ เป็นมาตรฐานในการพัฒนาโปรแกรม Python

มีขั้นตอนดังนี้

- A. เปิดโฟลเดอร์โปรเจกต์
- B. เปิด Terminal ภายในโฟลเดอร์
- C. สร้าง Virtual Environment

Windows
```
python -m venv .venv
```

หรือ

```
py -m venv .venv
```

macOS
```
python3 -m venv .venv
```

Linux
```
python3 -m venv .venv
```

D. เปิดใช้งาน Virtual Environment

Windows (PowerShell)
```
.venv\Scripts\Activate.ps1
```

Windows (Command Prompt)
```
.venv\Scripts\activate.bat
```

macOS
```
source .venv/bin/activate
```

Linux
```
source .venv/bin/activate
```


ก่อนไปต่อ ตรวจสอบ Terminal 

- เห็น (.venv) หน้าบรรทัดคำสั่งแล้ว  ทำงานต่อได้
- ไม่เห็น (.venv) หน้าบรรทัดคำสั่ง ให้กลับไปที่ D. เปิดใช้งาน Virtual Environment



# ขั้นตอนที่ 3 ติดตั้ง Streamlit

สามารถติดตั้งได้ 2 วิธี

### วิธีที่ 1

```bash
pip install streamlit
```

### วิธีที่ 2 (แนะนำ)

```bash
python -m pip install streamlit
```

---

# ขั้นตอนที่ 4 ตรวจสอบการติดตั้ง

ตรวจสอบเวอร์ชัน

```bash
streamlit version
```

หรือ

```bash
streamlit --version
```

ตัวอย่าง

```text
Streamlit, version 1.xx.x
```

---


# ขั้นตอนที่ 5 ทดสอบว่าใช้งานได้
- สร้าง โฟลเดอร์  
 ```
labhello

```

- สร้างไฟล์ ในโฟลเดอร์ labhello ชื่อ  (ในขั้นนี้ ต้องเชื่อมต่อกับ Editor ที่ใช้ก่อน เช่น VS Code หรือ PyCharm แล้วสร้าง Project ก่อนสร้างไฟล์)

```
hello.py
```

ใส่โค้ด

```python
import streamlit as st

st.title("Hello Streamlit 👋")
st.write("Welcome to Streamlit")
```

---

รันโปรแกรม ด้วย Terminal 

```bash
streamlit run hello.py
```

เมื่อรันสำเร็จ จะปรากฏข้อความลักษณะนี้

```text
Local URL: http://localhost:8501
```

เปิด Browser ไปที่

```
http://localhost:8501
```

จะเห็นหน้า Web App

---

# โครงสร้างโปรเจกต์ตัวอย่าง

```
MyProject/
│
├── hello.py
├── requirements.txt
└── README.md
```

---

# การสร้างไฟล์ requirements.txt

สำหรับเก็บรายการ Library ของโปรเจกต์

```bash
pip freeze > requirements.txt
```

ตัวอย่าง

```text
streamlit==1.46.1
pandas==2.3.1
numpy==2.3.1
```

ติดตั้งจากไฟล์

```bash
pip install -r requirements.txt
```

---

# คำสั่งที่ใช้บ่อย

| คำสั่ง | ความหมาย |
|---------|-----------|
| `python --version` | ตรวจสอบเวอร์ชัน Python |
| `where python` | ดูตำแหน่ง Python |
| `pip --version` | ตรวจสอบ pip |
| `python -m pip install streamlit` | ติดตั้ง Streamlit |
| `streamlit run hello.py` | รันโปรแกรม |
| `streamlit --version` | ตรวจสอบเวอร์ชัน Streamlit |
| `pip freeze` | แสดง Library ที่ติดตั้ง |
| `pip freeze > requirements.txt` | สร้าง requirements |
| `pip install -r requirements.txt` | ติดตั้ง Library ทั้งหมด |

---

# หากพบปัญหา

## streamlit ไม่พบคำสั่ง

```
'streamlit' is not recognized...
```

ให้ใช้

```bash
python -m streamlit run hello.py
```

---

## python ไม่พบคำสั่ง

```
Python was not found...
```

ตรวจสอบ

```bash
where python
```

หากไม่พบ

- ติดตั้ง Python ใหม่
- เปิดใช้งาน PATH
- หรือใช้คำสั่ง

```bash
winget install Python.Python.3
```

---

## pip ไม่พบคำสั่ง

ให้ใช้

```bash
python -m pip install --upgrade pip
```

---

# สรุปขั้นตอนทั้งหมด

```text
ติดตั้ง Python
        │
        ▼
ตรวจสอบ python --version
        │
        ▼
อัปเดต pip
        │
        ▼
ติดตั้ง Streamlit
        │
        ▼
สร้าง hello.py
        │
        ▼
streamlit run hello.py
        │
        ▼
เปิด Browser
http://localhost:8501
```

---

# 🎯 เป้าหมายหลังจากบทเรียนนี้

เมื่อเรียนจบบทนี้ นักศึกษาจะสามารถ

- ติดตั้ง Python ได้
- ติดตั้ง Streamlit ได้
- สร้างโปรเจกต์แรกด้วย Streamlit
- รัน Web Application ได้
- เข้าใจโครงสร้างของโปรเจกต์เบื้องต้น
- พร้อมสำหรับการพัฒนา Web App ด้วย Python

---

## 📚 บทถัดไป

ในบทถัดไปจะได้เรียนรู้

- การสร้างหน้า Web ด้วย Streamlit
- การใช้ `st.title()`, `st.header()`, `st.write()`
- การรับข้อมูลจากผู้ใช้ (Input Widgets)
- การสร้างปุ่มและโต้ตอบกับผู้ใช้
- การเชื่อมต่อฐานข้อมูล SQLite
- การพัฒนา CRUD Web Application ด้วย Streamlit


