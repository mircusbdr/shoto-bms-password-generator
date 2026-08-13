# SHOTO BMS Tool Password XML Generator

A small Python utility that generates a password hash compatible with **SHOTO BMS Tool** and creates the corresponding `pwd.xml` configuration file.

## Features

- Prompts for a new password without displaying it in the terminal
- Rejects empty passwords
- Generates the password hash expected by SHOTO BMS Tool
- Creates or overwrites `pwd.xml`
- Writes the generated hash to all supported password fields
- Uses only the Python standard library
- No external dependencies are required

## Requirements

- Python 3.x
- SHOTO BMS Tool

## Usage

Run:

```bash
python shoto_password.py
```

You will be prompted for a new password:

```text
Enter the new password:
```

The password is hidden while typing.

After the password is entered, the script creates:

```text
pwd.xml
```

in the current working directory.

## Password Hash Generation

The utility follows this process:

1. Encode the password as UTF-8.
2. Calculate its MD5 hash.
3. Convert the hexadecimal MD5 result to uppercase.
4. Append the fixed value `LD|SD`.
5. Calculate a second MD5 hash.
6. Convert the final hexadecimal hash to uppercase.

Conceptually:

```text
MD5(UPPERCASE(MD5(password)) + "LD|SD")
```

> This notation is conceptual. The implementation appends the bytes `b"LD|SD"` to the UTF-8 bytes of the uppercase first MD5 hexadecimal digest.

## Generated XML

The generated `pwd.xml` contains the same hash in each supported password field:

```xml
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
```

## Installing `pwd.xml` in SHOTO BMS Tool

After generating `pwd.xml`, copy it into the **`config` folder of the SHOTO BMS Tool installation**.

Recommended procedure:

1. Close SHOTO BMS Tool.
2. Locate the SHOTO BMS Tool installation directory.
3. Open its `config` folder.
4. Back up the existing `pwd.xml`, if present.
5. Copy the newly generated `pwd.xml` into the `config` folder.
6. Replace the existing file when prompted.
7. Start SHOTO BMS Tool again.

Example:

```text
SHOTO BMS Tool/
├── ...
├── config/
│   └── pwd.xml
└── ...
```

### Backup recommendation

Before replacing the original configuration, make a backup such as:

```text
pwd.xml.backup
```

The exact SHOTO BMS Tool installation path depends on where the application was installed.

## Typical Workflow

```text
Run shoto_password.py
        |
        v
Enter the new password
        |
        v
Generate password hash
        |
        v
Create pwd.xml
        |
        v
Copy pwd.xml to:
SHOTO BMS Tool/config/
        |
        v
Replace existing pwd.xml
        |
        v
Restart SHOTO BMS Tool
```

## Repository Structure

```text
shoto-bms-password-generator/
├── shoto_password.py
├── README.md
├── LICENSE
└── .gitignore
```

The generated `pwd.xml` is excluded from Git by default.

## Security Notice

MD5 is cryptographically broken and should not be used for modern password storage or new authentication systems.

This utility implements an existing application-specific format for compatibility purposes. For new systems, use a dedicated password hashing algorithm such as Argon2, bcrypt, or scrypt.

## Disclaimer

Use this utility only on systems and equipment that you own or are authorized to configure.

Always back up the original `pwd.xml` before replacing it.

The author is not responsible for configuration loss, access issues, or unauthorized use of this software.

## License

Released under the MIT License.
