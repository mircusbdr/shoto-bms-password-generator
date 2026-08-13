SHOTO BMS Tool Password XML Generator

A small Python utility for generating a password hash compatible with SHOTO BMS Tool and creating the corresponding pwd.xml configuration file.

Features
Accepts a new password from the user
Validates that the password is not empty
Generates the password hash required by SHOTO BMS Tool
Creates a pwd.xml file automatically
Writes the generated hash to all supported password fields
Uses only the Python standard library
No external dependencies required
Requirements
Python 3.x
SHOTO BMS Tool

No additional Python packages are required.

Usage

Run the script from a terminal:

python shoto_password.py

You will be prompted to enter a new password:

Introdu noua parolă:

After entering the password, the script generates:

pwd.xml

in the current working directory.

Password Hash Generation

The password is processed using the following steps:

The password is encoded using UTF-8.
An MD5 hash of the password is generated.
The hexadecimal MD5 result is converted to uppercase.
The fixed value LD|SD is appended.
A second MD5 hash is generated.
The final hexadecimal hash is converted to uppercase.

Conceptually:

MD5(UPPERCASE(MD5(password)) + "LD|SD")

The resulting hash is used in the generated XML configuration.

Generated XML

The generated pwd.xml file has the following structure:

<?xml version='1.0' encoding='utf-8'?>
<PASSWORD>
  <login_pwd>HASH</login_pwd>
  <parameter_pwd1>HASH</parameter_pwd1>
  <parameter_pwd2>HASH</parameter_pwd2>
  <config_pwd>HASH</config_pwd>
  <system_pwd>HASH</system_pwd>
  <system1_pwd>HASH</system1_pwd>
  <theft_pwd>HASH</theft_pwd>
  <general_pwd>HASH</general_pwd>
  <gyro_pwd>HASH</gyro_pwd>
  <comm_pwd>HASH</comm_pwd>
</PASSWORD>

The same generated hash is written to all password fields.

Installing pwd.xml in SHOTO BMS Tool

After generating the file, it must be copied into the config directory of the SHOTO BMS Tool installation.

Steps
Close SHOTO BMS Tool if it is running.
Locate the SHOTO BMS Tool installation folder.
Open the config directory.
Back up the existing pwd.xml file if one is present.
Copy the newly generated pwd.xml into the config directory.
Replace the existing file when prompted.
Start SHOTO BMS Tool again.

The directory structure should look similar to:

SHOTO BMS Tool/
├── ...
├── config/
│   └── pwd.xml
└── ...
Backup Recommendation

Before replacing the existing configuration file, it is recommended to create a backup.

For example:

pwd.xml
↓
pwd.xml.backup

This allows the previous configuration to be restored if necessary.

The exact installation directory may vary depending on where SHOTO BMS Tool was installed.

Typical Workflow
Run shoto_password.py
        │
        ▼
Enter the new password
        │
        ▼
Generate password hash
        │
        ▼
Create pwd.xml
        │
        ▼
Copy pwd.xml to
SHOTO BMS Tool/config/
        │
        ▼
Replace existing pwd.xml
        │
        ▼
Restart SHOTO BMS Tool
Functions
checksum(password: str) -> str

Generates the password hash.

Parameter

password — Password entered by the user.

Returns

The final uppercase hexadecimal hash.

Raises

ValueError if the supplied password is empty or contains only whitespace.
write_pwd_xml(hash_value: str, filename: str = "pwd.xml")

Creates or overwrites the XML password configuration file.

Parameters

hash_value — Hash to write to the XML fields.
filename — Output filename. Defaults to pwd.xml.
Recommended Repository Structure
shoto-bms-password-generator/
├── shoto_password.py
├── README.md
├── LICENSE
└── .gitignore

The generated pwd.xml should normally not be committed to the repository.

.gitignore

Recommended .gitignore:

# Generated password configuration
pwd.xml

# Python
__pycache__/
*.py[cod]

# Virtual environments
.venv/
venv/

# IDE / editor files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
Security Notice

MD5 is cryptographically broken and should not be used for modern password storage or authentication systems.
This project implements the hashing format expected by the target application for compatibility purposes only.
Do not use this hashing method when designing new authentication systems. Modern password storage should use dedicated password hashing algorithms such as Argon2, bcrypt, or scrypt.

Disclaimer

Use this utility only with systems and equipment that you own or are authorized to configure.
Always create a backup of the original configuration before replacing pwd.xml.
The author is not responsible for configuration loss, system access issues, or unauthorized use of this software.
