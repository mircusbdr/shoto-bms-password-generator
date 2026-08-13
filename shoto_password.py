import hashlib
from getpass import getpass


def checksum(password: str) -> str:
    """
    Generate the password hash used by SHOTO BMS Tool.

    Steps:
    1. Validate that the password is not empty.
    2. Calculate the uppercase MD5 hash of the password.
    3. Append the fixed salt b"LD|SD".
    4. Calculate the final uppercase MD5 hash.

    Args:
        password: Password entered by the user.

    Returns:
        The final uppercase hexadecimal hash.

    Raises:
        ValueError: If the password is empty or contains only whitespace.
    """
    if not password.strip():
        raise ValueError("Password cannot be empty.")

    salt = b"LD|SD"
    md5_hash = hashlib.md5(password.encode("utf-8")).hexdigest().upper()
    final_hash = hashlib.md5(md5_hash.encode("utf-8") + salt).hexdigest().upper()
    return final_hash


def write_pwd_xml(hash_value: str, filename: str = "pwd.xml") -> None:
    """
    Create or overwrite the SHOTO BMS Tool password XML file.

    Args:
        hash_value: Hash written to all supported password fields.
        filename: Output XML filename. Defaults to "pwd.xml".
    """
    xml_content = f"""<?xml version='1.0' encoding='utf-8'?>
<PASSWORD>
  <login_pwd>{hash_value}</login_pwd>
  <parameter_pwd1>{hash_value}</parameter_pwd1>
  <parameter_pwd2>{hash_value}</parameter_pwd2>
  <config_pwd>{hash_value}</config_pwd>
  <system_pwd>{hash_value}</system_pwd>
  <system1_pwd>{hash_value}</system1_pwd>
  <theft_pwd>{hash_value}</theft_pwd>
  <general_pwd>{hash_value}</general_pwd>
  <gyro_pwd>{hash_value}</gyro_pwd>
  <comm_pwd>{hash_value}</comm_pwd>
</PASSWORD>
"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(xml_content)

    print(f"'{filename}' was generated successfully.")


def main() -> None:
    try:
        password = getpass("Enter the new password: ")
        hash_value = checksum(password)
        write_pwd_xml(hash_value)
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
