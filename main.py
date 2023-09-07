try:
    from colorama import init, Fore
    import requests
    import uuid
    import random
    import json
    import os
    import time
    import subprocess
    import sys
    import threading
    import json
except ImportError as e:
    print('Some Library Not Instaled, Please run this command "pip install -r requirements.txt"')


class ProxyManager:
    def __init__(self):
        self.urls = [
            self.newProxy()
        ]

        self.all_proxies = []
        for url_proxies in self.urls:
            self.all_proxies.extend(url_proxies)
        self.total = len(self.all_proxies)
        self.all_proxies = random.sample(self.all_proxies, self.total)

    def __iter__(self):
        return iter(self.all_proxies)

    def newProxy(self):
        url = f"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text.split('\n')
            return data
        else:
            print("New Proxy Gabisa diambil")


def rand_domain():
    arraymail = ['yahoo.com', 'yahoo.co.id', 'gmail.com',
                 'yahoo.co.id', 'icloud.com', 'hotmail.com']
    return random.choice(arraymail)


def random_user(ua):
    url = "http://ninjaname.horseridersupply.com/indonesian_name.php"
    param = "number_generate=1&gender_type=male&submit=Generate"
    headers = {
        'Content-Length': str(len(param)),
        'User-Agent': ua,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(url, headers=headers, data=param)
    data = response.text.split('&bull;')[1]
    return data.split('<br/>')[0]


def random_useragent():
    browser = ['Mozilla', 'Firefox', 'Explorer']
    ua_browser = random.choice(browser)

    android_version = ['4.0', '4.4', '5.0', '6.0',
                       '5.5', '7.0', '8', '9', '10', '11', '12', '13']
    ua_android_version = random.choice(android_version)

    os = ['Windows', 'Linux']
    ua_os = random.choice(os)

    mobile = ''.join(random.choices(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=7))
    chrome_version = f"{random.randint(11, 99)}.{random.randint(1, 9)}.{random.randint(1111, 9999)}.{random.randint(10, 99)}"
    safari_version = f"{random.randint(111, 999)}.{random.randint(11, 99)}"
    browser_version = f"{random.randint(1, 9)}.{random.randint(0, 9)}"

    ua = f"{ua_browser}/{browser_version} ({ua_os}; Android {ua_android_version}; {mobile}) AppleWebKit/{safari_version} (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/{safari_version}"
    return ua


def session_id():
    return str(uuid.uuid4())


def unique_id():
    return '{:08x}{:08x}{:08x}{:08x}'.format(
        random.randint(0, 0xffffffff),
        random.randint(0, 0xffffffff),
        random.randint(0, 0xffffffff),
        random.randint(0, 0xffffffff)
    )


def fungsi_register(email, password):
    headers = {
        "X-Api-Platform": "app-android",
        "X-Api-Auth": "laZOmogezono5ogekaso5oz4Mezimew1",
        "User-Agent": userAgent_vidio,
        "X-Api-App-Info": xApiInfo_vidio,
        "Accept-Language": "id",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip"
    }

    url = "https://www.vidio.com/api/register"
    param = {
        "email": email,
        "password": password
    }

    response = requests.post(url, headers=headers, data=param)
    if response.status_code != 200:
        print(Fore.RED + f"{email} | {password} Register failed!")
        return None
    else:
        print(Fore.GREEN + f"{email} | {password} Register Succesfully!")
        return response.json()


def getAuth(partner, proxy):
    headers = {
        "X-Api-Platform": "tv-android",
        "X-Api-Auth": "laZOmogezono5ogekaso5oz4Mezimew1",
        "User-Agent": userAgent_vidio,
        "X-Api-App-Info": xApiInfo_vidio,
        "Accept-Language": "id",
        "Accept-Encoding": "gzip"
    }

    url = "https://www.vidio.com/api/partner/auth"
    param = {
        "partner_agent": partner
    }
    proxies = {"http": proxy, "https": proxy}
    if (partner == "changhong"):
        param["unique_id"] = generate_SN("G92DVB0CHOD0213", 4)
    elif (partner == "akari"):
        param["unique_id"] = generate_SN("F230101870A0", 4)
    try:
        response = requests.post(url, headers=headers,
                                 data=param, proxies=proxies, timeout=5)
        if response.status_code == 200:
            saveAuth.append(response.json())
        elif response.status_code >= 400:
            pass
    except requests.exceptions.RequestException as e:
        pass


def fungsiAuth(partner):
    totalThread = 100

    with open("config.json", "r") as file:
        data = json.load(file)
    proxyPrivate = data["proxy_private"]

    if (proxyPrivate == ""):
        proxy = ProxyManager()
        proxy_fixed = list(proxy)
        num_proxy = min(len(proxy_fixed), totalThread)

    print(Fore.YELLOW +
          f"Mohon tunggu beberapa waktu, sedang mencari SN dari {partner}!\n")
    while len(saveAuth) <= 0:
        threads = []
        if proxyPrivate == "":
            for proxy in proxy_fixed[:num_proxy]:
                thread = threading.Thread(
                    target=getAuth, args=(partner, proxy,))
                threads.append(thread)
                proxy_fixed.remove(proxy)
        else:
            for _ in range(totalThread):
                thread = threading.Thread(
                    target=getAuth, args=(partner, proxyPrivate,))
                threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    if len(saveAuth) > 0:
        print(Fore.GREEN + "Ketemu serial Number!")
        authResponse = saveAuth[0]
        saveAuth.pop(0)
        return authResponse
    else:
        print(Fore.RED+"auth Response has invalid or proxy habis")
        return None


def fungsi_login(email, password, user_token=None, user_auth_email=None):
    headers = {
        "X-Api-Platform": "tv-android",
        "X-Api-Auth": "laZOmogezono5ogekaso5oz4Mezimew1",
        "User-Agent": userAgent_vidio,
        "X-Api-App-Info": xApiInfo_vidio,
        "Accept-Language": "en",
        "X-Visitor-Id": session_id(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip"
    }

    if (user_token and user_auth_email) is not None:
        headers["X-User-Email"] = user_auth_email
        headers["X-User-Token"] = user_token

    url = "https://www.vidio.com/api/login"
    param = {
        "login": email,
        "password": password
    }
    response = requests.post(url, headers=headers, data=param)
    if response.status_code != 200:
        if (user_token and user_auth_email):
            print(Fore.RED+"The Auth login failed!\n")
        else:
            print(Fore.RED+"Login failed!\n")
        return None
    return response


def fungsi_get_subs(user_token, email):
    headers = {
        "X-Api-Platform": "tv-android",
        "X-Api-Auth": "laZOmogezono5ogekaso5oz4Mezimew1",
        "User-Agent": userAgent_vidio,
        "X-Api-App-Info": xApiInfo_vidio,
        "Accept-Language": "id",
        "X-User-Email": email,
        "X-User-Token": user_token,
        "Accept-Encoding": "gzip"
    }

    url = "https://api.vidio.com/api/users/subscriptions"

    response = requests.get(url, headers=headers)
    try:
        product_catalog = response.json(
        )['subscriptions'][0]["product_catalog"]["code"]
        return product_catalog
    except (KeyError, IndexError):
        return None


def fungsi_ambil(partner, email, password):
    login_response = fungsi_login(email, password)
    if (login_response is None):
        return None

    auth_response = fungsiAuth(partner)
    if (auth_response is None):
        return None

    authentication_token = auth_response['auth']['authentication_token']
    auth_email = auth_response["auth"]["email"]

    login_response = fungsi_login(
        email, password, authentication_token, auth_email)
    if (auth_response is None):
        return None

    subs_response = fungsi_get_subs(
        login_response.json()["auth"]["authentication_token"], email)

    if subs_response:
        print(Fore.GREEN+f"\n{email} | {password} | {subs_response}")
    else:
        print(
            Fore.RED+f"\n{email} | {password} | Subscription not Activated.")

    return subs_response


def generate_code(partner):
    auth_response = fungsiAuth(partner)
    if auth_response is None:
        return None

    authentication_token = auth_response['auth']['authentication_token']
    auth_email = auth_response["auth"]["email"]

    headers_tv = {
        "X-Api-Platform": "tv-android",
        "X-Api-Auth": "laZOmogezono5ogekaso5oz4Mezimew1",
        "User-Agent": userAgent_vidio,
        "X-Api-App-Info": xApiInfo_vidio,
        "Accept-Language": "id",
        "Accept-Encoding": "gzip"
    }

    url = "https://api.vidio.com/api/tv/code"

    response_tv = requests.get(url, headers=headers_tv)
    code = response_tv.json()["code"]

    print(Fore.GREEN+"\nCode: "+str(code))

    session = session_id()

    url_verify = "https://api.vidio.com/api/tv/verify_code"

    headers_verify = {
        "X-Api-Platform": "tv-android",
        "X-Api-Auth": "laZOmogezono5ogekaso5oz4Mezimew1",
        "User-Agent": userAgent_vidio,
        "X-Api-App-Info": xApiInfo_vidio,
        "Accept-Language": "id",
        "X-User-Email": auth_email,
        "X-User-Token": authentication_token,
        "Accept-Encoding": "gzip",
        "x-visitor-id": session
    }

    param = {
        "code": code
    }

    while True:
        response = requests.post(
            url=url_verify, headers=headers_verify, data=param)
        json_data = response.json()
        if ("error" not in json_data):
            print(Fore.GREEN+"Berhasil Masuk Cek Subscription")
            break
        print(Fore.GREEN+"Masukin Code nya...\nCode: "+str(code))
        time.sleep(10)


def generate_SN(prefix, length):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return f'{prefix}{random_numbers}'


def saveToFile(email, password, hasil):
    if not os.path.exists("akun.txt"):
        with open("akun.txt", 'w') as file:
            file.write(f"{email}"+f" | {password} | {hasil}")
        print(Fore.GREEN+f"File akun.txt' berhasil dibuat.")
    else:
        with open("akun.txt", 'r') as file:
            lines = file.readlines()
        if not lines:
            with open("akun.txt", 'a') as file:
                file.write(f"{email} | {password} | {hasil}")
        else:
            with open("akun.txt", 'a') as file:
                file.write(f"\n{email} | {password} | {hasil}")
    print(Fore.GREEN+"Berhasil Membuat log di Akun.txt")


def bulk(filename, partner, menu):
    updated_lines = []
    save = False
    with open(filename, "r") as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        data = line.strip().split("|")
        if len(data) >= 2:
            email, password = data[0].strip(), data[1].strip()
            print(f"{email} | {password}")
            if (menu == 5):
                hasil = fungsi_ambil(
                    partner, email, password)
                save = True
                print(Fore.GREEN+f"Berhasil diperbarui")
            if save:
                if hasil is None:
                    updated_lines.append(line)
                    continue
                elif hasil is not None:
                    saveToFile(email, password, hasil)
        else:
            print(
                Fore.RED+f"Line {line_number} Format harus email | password\n")
            updated_lines.append(line)

    with open(filename, "w") as file:
        file.writelines(updated_lines)


def main():
    try:
        with open("config.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("file config.json tidak ditemukan.")

    partner = data["partner"]
    password = data["password"]

    menu = int(input(
        "\n1. Buat Akun (Not Verified email)\n2. Generator Code TV\n3. Bulk (Buat akun bf)\n4. Copy akun.txt ke Download\nPilih : "))

    if (menu == 1):
        total = int(input("\n ϟ Berapa akun : "))
        if (total > 20):
            print(
                Fore.RED + f"Total {total} tidak diizinkan, sebaiknya jangan gegabah")
            sys.exit()
        for _ in range(total):
            print("================================================================")
            ua = random_useragent()
            username = random_user(ua)
            domain = rand_domain()
            uname = username.replace(' ', '')
            email = f"{uname.lower()}{random.randint(1, 999)}@{domain}"

            register_response = fungsi_register(email, password)
            if (register_response is None):
                continue
            hasil = fungsi_ambil(partner, email, password)
            if (hasil is None):
                continue
            else:
                saveToFile(email, password, hasil)
    elif menu == 2:
        generate_code(partner)
    elif menu == 3:
        filename = "bulk.txt"
        bulk(filename, partner, menu=5)
    elif menu == 4:
        destination_path = '/sdcard/Download/'
        command = ['cp', "./akun.txt", destination_path]
        try:
            subprocess.run(command, check=True)
            print(Fore.GREEN+f'File berhasil dicopy ke {destination_path}')
        except subprocess.CalledProcessError as e:
            print(Fore.RED + 'Terjadi Kesalahan')
    else:
        print(Fore.RED+"Gak ada Menunya Bangke!!!")


print('       _     _ _       \n      (_)   | (_)      \n__   ___  __| |_  ___  \n\ \ / / |/ _` | |/ _ \ \n \ V /| | (_| | | (_) |\n  \_/ |_|\__,_|_|\___/ ')
userAgent_vidio = "tv-android/1.92.1 (437)"
xApiInfo_vidio = "tv-android/13/1.92.1-437"
saveAuth = []

init(autoreset=True)
print("Dont sell this script, no more update for this script!")
print("My Tele CH: MaterIsCar")
main()
