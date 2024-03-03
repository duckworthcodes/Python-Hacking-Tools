import hashlib

def convert_text_to_sha1(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()
    return digest

def main():
    user_sha1 = input("Enter Your SHA1 Key: ")
    cleaned_user_sha1 = user_sha1.strip().lower()
    with open("./password.txt") as f:
        for line in f:
            password = line.strip()
            converted_sha_1 = convert_text_to_sha1(password)

            if cleaned_user_sha1 == converted_sha_1:
                print(f"Password Has Been Cracked:{password}")
                return

        print("Sorry Password Is Not Found")         

if __name__ == "__main__":
    main()
