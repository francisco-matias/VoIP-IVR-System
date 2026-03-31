# VoIP Interactive Voice Response System (Asterisk PBX)

This project consists of the design and implementation of a complete Voice over IP (VoIP) system featuring an Interactive Voice Response (IVR) application, built on top of an Asterisk PBX server.

Rather than being a standalone application, this project represents a **fully integrated communication system**, where configuration files, scripts, and network protocols work together to deliver real-time voice services.

---

## 📄 Overview

The system simulates a real-world VoIP infrastructure in which multiple users connect through softphones and interact with an automated voice service.

It combines:

- Low-level network protocols (SIP, RTP)
- PBX system configuration (Asterisk)
- Application logic (IVR menu)
- External service integration (Python via AGI)

Each component alone has limited utility, but together they form a **functional end-to-end telecommunication system**.

---

## 🏗️ System Architecture

The system is composed of three main layers:

### 1. Communication Layer
- **SIP (Session Initiation Protocol)** for signaling (registration, call setup, teardown)
- **RTP (Real-Time Transport Protocol)** for audio streaming
- **UDP transport** for low-latency communication

### 2. Core System (Asterisk PBX)
- Acts as a **SIP server, registrar, and proxy**
- Manages call routing and session control
- Executes IVR logic through the dialplan

### 3. Application Layer
- IVR menu logic implemented in Asterisk
- External Python script (AGI) for dynamic data retrieval
- Text-to-speech integration for audio generation

---

## 🔄 How the System Works

1. Users register on the Asterisk server using SIP (configured in `sip.conf`)
2. A call is placed to the IVR extension
3. Asterisk processes the call using the dialplan defined in `extensions.conf`
4. Audio is transmitted using RTP between client and server
5. The user interacts with the system using DTMF tones
6. Based on input, the system executes different services, including external scripts

---

## 📞 IVR Functionality

The IVR system provides an interactive voice menu:

- **1 – Day of the Week**
  - Converts the current day into NATO phonetic format
  - Demonstrates dynamic audio generation

- **2 – Mastermind Game**
  - Fully interactive game implemented in the dialplan
  - Handles user input, validation, and multiple attempts

- **3 – Totoloto Key**
  - Intended to retrieve the latest lottery key dynamically via Python (AGI)

- **0 – Exit**
  - Gracefully terminates the call

The menu loops continuously, allowing persistent interaction.

---

## ⚙️ Key Components and Their Role

### 📁 `sip.conf`
Defines the VoIP network:
- User accounts (extensions)
- Authentication credentials
- SIP registration parameters

👉 Without this file, users cannot connect to the system.

---

### 📁 `extensions.conf`
Defines the **core logic of the system (dialplan)**:
- Call routing
- IVR menu structure
- DTMF input handling
- Execution of actions (play audio, run scripts, loop menus)

👉 This is the “brain” of the IVR system.

---

### 🐍 `totoloto_agi.py`
Python script integrated via **Asterisk Gateway Interface (AGI)**:

- Connects to an external website
- Scrapes the latest Totoloto results using `requests` and `BeautifulSoup`
- Returns the result to Asterisk via environment variables

👉 This demonstrates how Asterisk can be extended beyond static logic into **dynamic, data-driven services**

⚠️ Note: Although the script works independently, full integration with Asterisk presented challenges, and a fallback static response was used in the IVR.

---

## 🔗 Why This System Matters

Individually:
- The Python script only fetches data
- The configuration files only define behavior
- The IVR logic alone cannot communicate externally

Together:
- They form a **real-time, interactive VoIP service**
- Capable of handling users, calls, and dynamic content

This project demonstrates how **network protocols, system configuration, and application logic must be integrated** to build functional communication systems.

---

## 🛠️ Technologies Used

- Asterisk PBX
- SIP / RTP / UDP
- Python (AGI scripting)
- Linux
- Linphone (VoIP client)
- BeautifulSoup (web scraping)

