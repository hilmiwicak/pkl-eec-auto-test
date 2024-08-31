# Skripsi Test Execution

## PKL test executions

| ID   | Description                                                     |
|------|-----------------------------------------------------------------|
| R-01 | Log in                                                          |
| R-02 | Logout                                                          |
| R-03 | Verifikasi akun                                                 |
| R-04 | Menghapus akun                                                  |
| R-05 | Mengubah password akun                                          |
| R-06 | Menampilkan daftar laporan kerja preventive maintenance teknisi |
| R-07 | Menampilkan daftar laporan kerja corrective maintenance teknisi |
| R-08 | Menampilkan detail laporan kerja preventive maintenance teknisi |
| R-09 | Menampilkan detail laporan kerja corrective maintenance teknisi |
| R-10 | Menampilkan data teknisi                                        |
| R-11 | Menambah data teknisi                                           |
| R-12 | Mengubah data teknisi                                           |
| R-13 | Menghapus data teknisi                                          |
| R-14 | Mencetak data teknisi                                           |
| R-15 | Melihat daftar radar                                            |
| R-16 | Menambah radar                                                  |
| R-17 | Menghapus radar                                                 |
| R-18 | Menampilkan distribusi tugas teknisi                            |
| R-19 | Menambah distribusi tugas teknisi                               |
| R-20 | Mengubah distribusi tugas teknisi                               |
| R-21 | Menghapus distribusi tugas teknisi                              |
| R-22 | Menampilkan stok inventaris perusahaan                          |
| R-23 | Menambah stok inventaris perusahaan                             |
| R-24 | Mengubah stok inventaris perusahaan                             |
| R-25 | Menghapus stok inventaris perusahaan                            |
| R-26 | Mencetak stok inventaris perusahaan                             |
| R-27 | Menampilkan rekomendasi inventaris perusahaan                   |
| R-28 | Menampilkan inventaris radar                                    |
| R-29 | Menambah inventaris radar                                       |
| R-30 | Mengubah inventaris radar                                       |
| R-31 | Menghapus inventaris radar                                      |
| R-32 | Mencetak inventaris radar                                       |
| R-33 | Mengirim notifikasi stok kedaluwarsa secara berkala             |

Features :

- autentikasi

    - login

        ada dua input: email dan password. email in db : string ; password in db : string.

        1. [x] email and password valid, but not with correct credentials
        2. [x] email valid, password valid but not regular string
        3. [x] valid

    - [x] logout

- kelola akun

    - [x] verif akun
    - [x] hapus akun

- ubah password admin

    3 inputs : current password, new password, confirmation password

    1. [x] different current password, different confirmation password, valid new password
    2. [x] current password, confirmation password, and new password less than 6 characters
    3. [x] empty
    4. [x] same new password, all valid
    5. [x] new password not string (special characters & some characters from other than regular chars) with trailing space
    6. [x] {ERROR} current password not string with leading / trailing space

- kelola laporan kerja teknisi

    - lihat laporan kerja teknisi

        - [x] pm
        - [x] cm

    - lihat detail laporan kerja teknisi

        - [x] pm
        - [x] cm

    - cetak laporan kerja teknisi

- kelola data teknisi

    - [x] lihat teknisi
    - tambah teknisi

        1. [x] name more than 15, nip less than 11, valid company
        2. [x] name not string (special characters & some characters from other than regular chars), expert_company not string (special characters & some characters from other than regular chars), nip not integer
        3. [x] valid name, nip more than 18 digit, valid company
        4. [x] {ERROR server} eec company nip 18 digit
        5. [x] empty
        6. [x] all valid not eec company, nip 18 digit
        7. [x] all valid eec company 11 digit
        8. [x] {ERROR server} all valid, but same nip

    - [x] ubah teknisi

        1. [x] check whether the data is the same as the one in the view all page
        2. [x] name more than 15, nip less than 11, valid company
        3. [x] name not string (special characters & some characters from other than regular chars), expert_company not string (special characters & some characters from other than regular chars), nip not integer
        4. [x] valid name, nip more than 18 digit, valid company
        5. [x] {ERROR server} eec company nip 18 digit
        6. [x] empty
        7. [x] all valid not eec company, nip 18 digit
        8. [x] all valid eec company 11 digit
        9. [x] {ERROR server} all valid, but same nip

    - [x] hapus teknisi

- kelola radar

    - [x] lihat radar(?)
    - tambah radar

        requirement nya harus ada stock atau ngga?

        1. [x] {ERROR image no error input and no invalid stock} radar name not regular string, site location not regular string, image not image, stock select on but not selecting

            INCONSISTENT. sometimes the stock is showing error, sometimes it doesn't.

        2. [x] {ERROR no invalid stock} empty input, stock not selecting

            {ERROR} harusnya gak ada site yang terbuat

        3. [x] valid input stock select on but not selecting

            {ERROR} harusnya gak ada site yang terbuat

        4. [x] valid input with stock not selecting
        5. [x] valid input with 1 stock
        6. [x] valid input with 3 stock

    - [x] hapus radar

- kelola distribusi tugas teknisi

    - lihat tugas

        1. [x] tabel tugas ada atau tidak
        2. [x] yang ada di list sama dengan yang ada di detail

    - tambah tugas

        1. [x] check whether the name in view is not on the add form
        2. [x] empty
        3. [x] valid

    - ubah tugas

        1. [x] checking wheter the name in the view is not on the detail
        2. [x] empty
        3. [x] valid

    - [x] hapus tugas

- kelola stok inventaris

    - [x] lihat stok inventaris

        is it okay to have 0 stocks?

    - tambah stok inventaris

        1. [x] not regular chars nama barang, not regular character group, not regular character part number, not regular character ref des, EXPIRED DATE < TGL MASUK, JUMLAH UNIT NOT INTEGER, keterangan not regular character
        2. [x] empty input
        3. [x] valid

    - ubah stok inventaris

        1. [x] {SOMETIMES ERROR in keterangan} checking whether the data in the list view is the same as in the edit form
        2. [x] not regular chars nama barang, not regular character group, not regular character part number, not regular character ref des, EXPIRED DATE < TGL MASUK, JUMLAH UNIT NOT INTEGER, keterangan not regular character
        3. [x] empty input
        4. [x] valid

    - [x] hapus stok inventaris
    - cetak stok inventaris
    - [x] lihat rekomendasi inventaris

- kelola inventaris radar

    cara kerja inventaris radar :

    setelah nambah inventaris radar, jumlah unit dari inventaris stok akan berkurang. tapi apakah untuk jumlah unit yang 0 masih ditampilkan?

    > setelah di test, ternyata tidak ditampilkan. which is as expected. berarti harus di check juga di inventaris stok.

    berarti cuma perlu dicek aja bagian add_site_stock. apakah yang 0 itu ada atau ngga?

    tapi ini udah di luar scope skripsi. jadi gak usah di uji

    - [x] lihat inventaris radar
    - tambah inventaris radar

        1. [x] select on but not selecting
        2. [x] delete input
        3. [x] valid inputs, input 1 stock
        4. [x] valid inputs, input 3 stock

    - ubah inventaris radar

        1. [x] {ERROR} checking whether the list is the same at edit form
        2. [x] not regular chars nama barang, not regular character group, not regular character part number, not regular character ref des, EXPIRED DATE < TGL MASUK, JUMLAH UNIT NOT INTEGER
        3. [x] empty input
        4. [x] valid

    - [x] hapus inventaris radar
    - cetak inventaris radar

- notif expired stock

## Execution of Login (test case 1 and 2) and Logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

----------------------------------------------------------------------
Ran 2 tests in 28.953s

OK
```

## Execution of Login (test case 3) and Logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

----------------------------------------------------------------------
Ran 2 tests in 27.702s

OK
```

## 1 Execution of Login, test_verify_account, test_delete_account, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_verify_account (__main__.AccountManagement) ... ok
test_delete_account (__main__.AccountManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

----------------------------------------------------------------------
Ran 4 tests in 61.306s

OK
```

## 2 Execution of Login, test_verify_account, test_delete_account, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_verify_account (__main__.AccountManagement) ... FAIL
test_delete_account (__main__.AccountManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
FAIL: test_verify_account (__main__.AccountManagement)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 58, in test_verify_account
    self.assertEqual(message, "User Approved")
AssertionError: '' != 'User Approved'
+ User Approved

----------------------------------------------------------------------
Ran 4 tests in 48.723s

FAILED (failures=1)
```

## 1 Execution of Login, test_edit_password, Logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_edit_password (__main__.PasswordEdit) ... test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
ERROR: test_edit_password (__main__.PasswordEdit) [6. current password not regular string]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 126, in test_edit_password
    message = profile_page.get_message()
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\pages\base_page.py", line 34, in get_message
    return self.driver.find_element(
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 861, in find_element
    return self.execute(Command.FIND_ELEMENT, {"using": by, "value": value})["value"]
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 444, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 249, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"span[data-notify='message']"}
  (Session info: chrome=109.0.5414.0)
Stacktrace:
Backtrace:
        (No symbol) [0x00E36643]
        (No symbol) [0x00DCBE21]
        (No symbol) [0x00CCDA9D]
        (No symbol) [0x00D01342]
        (No symbol) [0x00D0147B]
        (No symbol) [0x00D38DC2]
        (No symbol) [0x00D1FDC4]
        (No symbol) [0x00D36B09]
        (No symbol) [0x00D1FB76]
        (No symbol) [0x00CF49C1]
        (No symbol) [0x00CF5E5D]
        GetHandleVerifier [0x010AA142+2497106]
        GetHandleVerifier [0x010D85D3+2686691]
        GetHandleVerifier [0x010DBB9C+2700460]
        GetHandleVerifier [0x00EE3B10+635936]
        (No symbol) [0x00DD4A1F]
        (No symbol) [0x00DDA418]
        (No symbol) [0x00DDA505]
        (No symbol) [0x00DE508B]
        BaseThreadInitThunk [0x75EC7BA9+25]
        RtlInitializeExceptionChain [0x773FC10B+107]
        RtlClearBits [0x773FC08F+191]


----------------------------------------------------------------------
Ran 3 tests in 96.711s

FAILED (errors=1)
```

## 2 Execution of Login, test_edit_password, Logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_edit_password (__main__.PasswordEdit) ... test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
ERROR: test_edit_password (__main__.PasswordEdit) [6. current password not regular string]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 126, in test_edit_password
    message = profile_page.get_message()
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\pages\base_page.py", line 34, in get_message
    return self.driver.find_element(
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 861, in find_element
    return self.execute(Command.FIND_ELEMENT, {"using": by, "value": value})["value"]
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 444, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 249, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"span[data-notify='message']"}
  (Session info: chrome=109.0.5414.0)
Stacktrace:
Backtrace:
        (No symbol) [0x00E36643]
        (No symbol) [0x00DCBE21]
        (No symbol) [0x00CCDA9D]
        (No symbol) [0x00D01342]
        (No symbol) [0x00D0147B]
        (No symbol) [0x00D38DC2]
        (No symbol) [0x00D1FDC4]
        (No symbol) [0x00D36B09]
        (No symbol) [0x00D1FB76]
        (No symbol) [0x00CF49C1]
        (No symbol) [0x00CF5E5D]
        GetHandleVerifier [0x010AA142+2497106]
        GetHandleVerifier [0x010D85D3+2686691]
        GetHandleVerifier [0x010DBB9C+2700460]
        GetHandleVerifier [0x00EE3B10+635936]
        (No symbol) [0x00DD4A1F]
        (No symbol) [0x00DDA418]
        (No symbol) [0x00DDA505]
        (No symbol) [0x00DE508B]
        BaseThreadInitThunk [0x75EC7BA9+25]
        RtlInitializeExceptionChain [0x773FC10B+107]
        RtlClearBits [0x773FC08F+191]


----------------------------------------------------------------------
Ran 3 tests in 90.574s

FAILED (errors=1)
```

## 1 Execution of Login, test_view_cm, test_view_pm, test_view_cm, test_view_detail_pm, test_view_detail_cm, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_pm (__main__.MaintenanceManagement) ... ok
test_view_cm (__main__.MaintenanceManagement) ... ok
test_view_detail_pm (__main__.MaintenanceManagement) ... ok
test_view_detail_cm (__main__.MaintenanceManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

----------------------------------------------------------------------
Ran 6 tests in 91.164s

OK
```

## 1 Execution of Login, test_view_expert, test_add_expert, test_edit_expert, test_delete_expert, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_expert (__main__.ExpertManagement) ... ok
test_add_expert (__main__.ExpertManagement) ... test_edit_expert (__main__.ExpertManagement) ... test_delete_expert (__main__.ExpertManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
ERROR: test_edit_expert (__main__.ExpertManagement) [7. correct inputs, not eec expert]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 330, in test_edit_expert
    message = expert_page.get_message()
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\pages\base_page.py", line 34, in get_message
    return self.driver.find_element(
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 861, in find_element
    return self.execute(Command.FIND_ELEMENT, {"using": by, "value": value})["value"]
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 444, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 249, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"span[data-notify='message']"}
  (Session info: chrome=109.0.5414.0)
Stacktrace:
Backtrace:
        (No symbol) [0x00E36643]
        (No symbol) [0x00DCBE21]
        (No symbol) [0x00CCDA9D]
        (No symbol) [0x00D01342]
        (No symbol) [0x00D0147B]
        (No symbol) [0x00D38DC2]
        (No symbol) [0x00D1FDC4]
        (No symbol) [0x00D36B09]
        (No symbol) [0x00D1FB76]
        (No symbol) [0x00CF49C1]
        (No symbol) [0x00CF5E5D]
        GetHandleVerifier [0x010AA142+2497106]
        GetHandleVerifier [0x010D85D3+2686691]
        GetHandleVerifier [0x010DBB9C+2700460]
        GetHandleVerifier [0x00EE3B10+635936]
        (No symbol) [0x00DD4A1F]
        (No symbol) [0x00DDA418]
        (No symbol) [0x00DDA505]
        (No symbol) [0x00DE508B]
        BaseThreadInitThunk [0x75EC7BA9+25]
        RtlInitializeExceptionChain [0x773FC10B+107]
        RtlClearBits [0x773FC08F+191]


======================================================================
ERROR: test_edit_expert (__main__.ExpertManagement) [8. correct inputs, eec expert]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 336, in test_edit_expert
    message = expert_page.get_message()
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\pages\base_page.py", line 34, in get_message
    return self.driver.find_element(
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 861, in find_element
    return self.execute(Command.FIND_ELEMENT, {"using": by, "value": value})["value"]
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 444, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 249, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"span[data-notify='message']"}
  (Session info: chrome=109.0.5414.0)
Stacktrace:
Backtrace:
        (No symbol) [0x00E36643]
        (No symbol) [0x00DCBE21]
        (No symbol) [0x00CCDA9D]
        (No symbol) [0x00D01342]
        (No symbol) [0x00D0147B]
        (No symbol) [0x00D38DC2]
        (No symbol) [0x00D1FDC4]
        (No symbol) [0x00D36B09]
        (No symbol) [0x00D1FB76]
        (No symbol) [0x00CF49C1]
        (No symbol) [0x00CF5E5D]
        GetHandleVerifier [0x010AA142+2497106]
        GetHandleVerifier [0x010D85D3+2686691]
        GetHandleVerifier [0x010DBB9C+2700460]
        GetHandleVerifier [0x00EE3B10+635936]
        (No symbol) [0x00DD4A1F]
        (No symbol) [0x00DDA418]
        (No symbol) [0x00DDA505]
        (No symbol) [0x00DE508B]
        BaseThreadInitThunk [0x75EC7BA9+25]
        RtlInitializeExceptionChain [0x773FC10B+107]
        RtlClearBits [0x773FC08F+191]


======================================================================
FAIL: test_add_expert (__main__.ExpertManagement) [4. correct name, correct eec company, nip 18 digit]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 219, in test_add_expert
    self.assertEqual(message_nip, "EEC Expert must have 11 digits.")
AssertionError: '' != 'EEC Expert must have 11 digits.'
+ EEC Expert must have 11 digits.

======================================================================
FAIL: test_add_expert (__main__.ExpertManagement) [8. same name, same nip, eec expert]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 254, in test_add_expert
    self.assertEqual(message_nip, "The nip has already been taken.")
AssertionError: '' != 'The nip has already been taken.'
+ The nip has already been taken.

======================================================================
FAIL: test_edit_expert (__main__.ExpertManagement) [5. correct name, correct eec company, nip 18 digit]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 312, in test_edit_expert
    self.assertEqual(message_nip, "EEC Expert must have 11 digits.")
AssertionError: '' != 'EEC Expert must have 11 digits.'
+ EEC Expert must have 11 digits.

======================================================================
FAIL: test_edit_expert (__main__.ExpertManagement) [9. same name, same nip, eec expert]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 347, in test_edit_expert
    self.assertEqual(message_nip, "The nip has already been taken.")
AssertionError: '' != 'The nip has already been taken.'
+ The nip has already been taken.

----------------------------------------------------------------------
Ran 6 tests in 351.962s

FAILED (failures=4, errors=2)
```

## 2 Execution of Login, test_view_expert, test_add_expert, test_edit_expert, test_delete_expert, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_expert (__main__.ExpertManagement) ... ok
test_add_expert (__main__.ExpertManagement) ... test_edit_expert (__main__.ExpertManagement) ... test_delete_expert (__main__.ExpertManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
ERROR: test_edit_expert (__main__.ExpertManagement) [7. correct inputs, not eec expert]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 330, in test_edit_expert
    message = expert_page.get_message()
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\pages\base_page.py", line 34, in get_message
    return self.driver.find_element(
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 861, in find_element
    return self.execute(Command.FIND_ELEMENT, {"using": by, "value": value})["value"]
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 444, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 249, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"span[data-notify='message']"}
  (Session info: chrome=109.0.5414.0)
Stacktrace:
Backtrace:
        (No symbol) [0x00E36643]
        (No symbol) [0x00DCBE21]
        (No symbol) [0x00CCDA9D]
        (No symbol) [0x00D01342]
        (No symbol) [0x00D0147B]
        (No symbol) [0x00D38DC2]
        (No symbol) [0x00D1FDC4]
        (No symbol) [0x00D36B09]
        (No symbol) [0x00D1FB76]
        (No symbol) [0x00CF49C1]
        (No symbol) [0x00CF5E5D]
        GetHandleVerifier [0x010AA142+2497106]
        GetHandleVerifier [0x010D85D3+2686691]
        GetHandleVerifier [0x010DBB9C+2700460]
        GetHandleVerifier [0x00EE3B10+635936]
        (No symbol) [0x00DD4A1F]
        (No symbol) [0x00DDA418]
        (No symbol) [0x00DDA505]
        (No symbol) [0x00DE508B]
        BaseThreadInitThunk [0x75EC7BA9+25]
        RtlInitializeExceptionChain [0x773FC10B+107]
        RtlClearBits [0x773FC08F+191]


======================================================================
ERROR: test_edit_expert (__main__.ExpertManagement) [8. correct inputs, eec expert]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 336, in test_edit_expert
    message = expert_page.get_message()
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\pages\base_page.py", line 34, in get_message
    return self.driver.find_element(
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 861, in find_element
    return self.execute(Command.FIND_ELEMENT, {"using": by, "value": value})["value"]
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 444, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 249, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"span[data-notify='message']"}
  (Session info: chrome=109.0.5414.0)
Stacktrace:
Backtrace:
        (No symbol) [0x00E36643]
        (No symbol) [0x00DCBE21]
        (No symbol) [0x00CCDA9D]
        (No symbol) [0x00D01342]
        (No symbol) [0x00D0147B]
        (No symbol) [0x00D38DC2]
        (No symbol) [0x00D1FDC4]
        (No symbol) [0x00D36B09]
        (No symbol) [0x00D1FB76]
        (No symbol) [0x00CF49C1]
        (No symbol) [0x00CF5E5D]
        GetHandleVerifier [0x010AA142+2497106]
        GetHandleVerifier [0x010D85D3+2686691]
        GetHandleVerifier [0x010DBB9C+2700460]
        GetHandleVerifier [0x00EE3B10+635936]
        (No symbol) [0x00DD4A1F]
        (No symbol) [0x00DDA418]
        (No symbol) [0x00DDA505]
        (No symbol) [0x00DE508B]
        BaseThreadInitThunk [0x75EC7BA9+25]
        RtlInitializeExceptionChain [0x773FC10B+107]
        RtlClearBits [0x773FC08F+191]


======================================================================
FAIL: test_add_expert (__main__.ExpertManagement) [4. correct name, correct eec company, nip 18 digit]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 219, in test_add_expert
    self.assertEqual(message_nip, "EEC Expert must have 11 digits.")
AssertionError: '' != 'EEC Expert must have 11 digits.'
+ EEC Expert must have 11 digits.

======================================================================
FAIL: test_add_expert (__main__.ExpertManagement) [8. same name, same nip, eec expert]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 254, in test_add_expert
    self.assertEqual(message_nip, "The nip has already been taken.")
AssertionError: '' != 'The nip has already been taken.'
+ The nip has already been taken.

======================================================================
FAIL: test_edit_expert (__main__.ExpertManagement) [5. correct name, correct eec company, nip 18 digit]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 312, in test_edit_expert
    self.assertEqual(message_nip, "EEC Expert must have 11 digits.")
AssertionError: '' != 'EEC Expert must have 11 digits.'
+ EEC Expert must have 11 digits.

======================================================================
FAIL: test_edit_expert (__main__.ExpertManagement) [9. same name, same nip, eec expert]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 347, in test_edit_expert
    self.assertEqual(message_nip, "The nip has already been taken.")
AssertionError: '' != 'The nip has already been taken.'
+ The nip has already been taken.

----------------------------------------------------------------------
Ran 6 tests in 356.676s

FAILED (failures=4, errors=2)
```

## 1 Execution of login, test_view_site, test_add_site, test_delete_site, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_site (__main__.SiteRadarManagement) ... ok
test_add_site (__main__.SiteRadarManagement) ... test_delete_site (__main__.SiteRadarManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
FAIL: test_add_site (__main__.SiteRadarManagement) [1. radar name not regular string, site location not regular string, image not image, stock select on but not selecting]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 382, in test_add_site
    self.assertEqual(message_stock, "This field is required")
AssertionError: '' != 'This field is required'
+ This field is required

======================================================================
FAIL: test_add_site (__main__.SiteRadarManagement) [2. empty inputs, not selecting stocks]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 397, in test_add_site
    self.assertEqual(message_stock, "This field is required")
AssertionError: '' != 'This field is required'
+ This field is required

----------------------------------------------------------------------
Ran 5 tests in 181.793s

FAILED (failures=2)
```

## 2 Execution of login, test_view_site, test_add_site, test_delete_site, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_site (__main__.SiteRadarManagement) ... ok
test_add_site (__main__.SiteRadarManagement) ... test_delete_site (__main__.SiteRadarManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
FAIL: test_add_site (__main__.SiteRadarManagement) [1. radar name not regular string, site location not regular string, image not image, stock select on but not selecting]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 382, in test_add_site
    self.assertEqual(message_stock, "This field is required")
AssertionError: '' != 'This field is required'
+ This field is required

======================================================================
FAIL: test_add_site (__main__.SiteRadarManagement) [2. empty inputs, not selecting stocks]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 397, in test_add_site
    self.assertEqual(message_stock, "This field is required")
AssertionError: '' != 'This field is required'
+ This field is required

======================================================================
FAIL: test_add_site (__main__.SiteRadarManagement) [6. correct inputs with 3 stocks]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 438, in test_add_site
    self.assertEqual(message, "Data Created!")
AssertionError: '' != 'Data Created!'
+ Data Created!

----------------------------------------------------------------------
Ran 5 tests in 170.743s

FAILED (failures=3)
```

## 1 Execution of login, test_view_distribution, test_add_distribution, test_edit_distribution, test_delete_distribution, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_distribution (__main__.DistributionManagement) ... ok
test_add_distribution (__main__.DistributionManagement) ... ok
test_edit_distribution (__main__.DistributionManagement) ... ok
test_delete_distribution (__main__.DistributionManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

----------------------------------------------------------------------
Ran 6 tests in 140.849s

OK
```

## 2 Execution of login, test_view_distribution, test_add_distribution, test_edit_distribution, test_delete_distribution, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_distribution (__main__.DistributionManagement) ... ok
test_add_distribution (__main__.DistributionManagement) ... ok
test_edit_distribution (__main__.DistributionManagement) ... ok
test_delete_distribution (__main__.DistributionManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

----------------------------------------------------------------------
Ran 6 tests in 139.536s

OK
```

## 1 Execution of login, test_view_stock, test_add_stock, test_edit_stock, test_delete_stock, test_view_stock_recommendation, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_stock (__main__.StockManagement) ... ok
test_add_stock (__main__.StockManagement) ... ok
test_edit_stock (__main__.StockManagement) ... test_delete_stock (__main__.StockManagement) ... ok
test_view_stock_recommendation (__main__.StockManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
FAIL: test_edit_stock (__main__.StockManagement) [1. checking whether the data in the list view is the same as in the edit form]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 647, in test_edit_stock
    self.assertEqual(stock_view["keterangan"], stock_edit["keterangan"])
AssertionError: 'Retr[237 chars]logi. Eksakta induk glositas fitofogus gongsen[157 chars]pal.' != 'Retr[237 chars]logi.Eksakta induk glositas fitofogus gongseng[156 chars]pal.'
- Retromandibuler protaktinium gonjing bromida lucup seliri adika kemik dewan. Kokurikuler bunduk jeding neraca tembus kuriositas. Tunu megrek-megrek profase biosida kuadratika kupu-kupu kawih. Modul leuca inovasi ulang-alik maserasi fitososiologi. Eksakta induk glositas fitofogus gongseng kalah. Ektohormon knot bekel mahadewi eskalasi troli serunai mujbir barung-barung. Cabe janggelan labuh pramuwisata sungu. Asor neptunus watermantel noja opal.
?                                                                                                                                                                                                                                                       -
+ Retromandibuler protaktinium gonjing bromida lucup seliri adika kemik dewan. Kokurikuler bunduk jeding neraca tembus kuriositas. Tunu megrek-megrek profase biosida kuadratika kupu-kupu kawih. Modul leuca inovasi ulang-alik maserasi fitososiologi.Eksakta induk glositas fitofogus gongseng kalah. Ektohormon knot bekel mahadewi eskalasi troli serunai mujbir barung-barung. Cabe janggelan labuh pramuwisata sungu. Asor neptunus watermantel noja opal.


----------------------------------------------------------------------
Ran 7 tests in 260.231s

FAILED (failures=1)
```

## 2 Execution of login, test_view_stock, test_add_stock, test_edit_stock, test_delete_stock, test_view_stock_recommendation, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_stock (__main__.StockManagement) ... ok
test_add_stock (__main__.StockManagement) ... ok
test_edit_stock (__main__.StockManagement) ... test_delete_stock (__main__.StockManagement) ... ok
test_view_stock_recommendation (__main__.StockManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
FAIL: test_edit_stock (__main__.StockManagement) [1. checking whether the data in the list view is the same as in the edit form]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 647, in test_edit_stock
    self.assertEqual(stock_view["keterangan"], stock_edit["keterangan"])
AssertionError: 'Muta[153 chars]plin. Asonansi jompak faedah kerobek hodometer[203 chars]yek.' != 'Muta[153 chars]plin.Asonansi jompak faedah kerobek hodometer [202 chars]yek.'
- Mutasawif anakrus julab leukoderma hidropati pancabicara komuni. Setirman anofeles perawis autarki iblis plumbum opini berembang. Khurafat angan anadrom disiplin. Asonansi jompak faedah kerobek hodometer antoi konsekrasi puyeng. Rekurs pentahedron geligi spastik antidiuretik kerentam curiah cahar. Terjun debung tulup secina cicit ranai kuis urologi arun. Adidaya over ayum raraha ajnas corob filial rempeyek.
?
-
+ Mutasawif anakrus julab leukoderma hidropati pancabicara komuni. Setirman anofeles perawis autarki iblis plumbum opini berembang. Khurafat angan anadrom disiplin.Asonansi jompak faedah kerobek hodometer antoi konsekrasi puyeng. Rekurs pentahedron geligi spastik antidiuretik kerentam curiah cahar. Terjun debung tulup secina cicit ranai kuis urologi arun. Adidaya over ayum raraha ajnas corob filial rempeyek.


----------------------------------------------------------------------
Ran 7 tests in 260.502s

FAILED (failures=1)
```

## 1 Execution of login, test_view_site_stock, test_add_site_stock, test_edit_site_stock, test_delete_site_stock, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_site_stock (__main__.SiteRadarStockManagement) ... ok
test_add_site_stock (__main__.SiteRadarStockManagement) ... ok
test_edit_site_stock (__main__.SiteRadarStockManagement) ... test_delete_site_stock (__main__.SiteRadarStockManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
FAIL: test_edit_site_stock (__main__.SiteRadarStockManagement) [1. check whether the data is the same as the one in the view all page]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 808, in test_edit_site_stock
    self.assertEqual(ref_des_view, ref_des_detail)
AssertionError: '7r442' != ''
- 7r442
+


----------------------------------------------------------------------
Ran 6 tests in 205.967s

FAILED (failures=1)
```

## 2 Execution of login, test_view_site_stock, test_add_site_stock, test_edit_site_stock, test_delete_site_stock, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_site_stock (__main__.SiteRadarStockManagement) ... ok
test_add_site_stock (__main__.SiteRadarStockManagement) ... ok
test_edit_site_stock (__main__.SiteRadarStockManagement) ... test_delete_site_stock (__main__.SiteRadarStockManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
FAIL: test_edit_site_stock (__main__.SiteRadarStockManagement) [1. check whether the data is the same as the one in the view all page]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 808, in test_edit_site_stock
    self.assertEqual(ref_des_view, ref_des_detail)
AssertionError: '7r442' != ''
- 7r442
+


----------------------------------------------------------------------
Ran 6 tests in 210.731s

FAILED (failures=1)
```

## Execution time

calculate the sum all of these lines 

28.953s
\+ 27.702s = 56.655s
\+ 61.306s = 117.961s
\+ 48.723s = 166.684s
\+ 96.711s = 263.395s
\+ 90.574s = 353.969s
\+ 91.164s = 445.133s
\+ 351.962s = 797.095s
\+ 356.676s = 1153.771s
\+ 181.793s = 1335.564s
\+ 170.743s = 1506.307s
\+ 140.849s = 1647.156s
\+ 139.536s = 1786.692s
\+ 260.231s = 2046.923s
\+ 260.502s = 2307.425s
\+ 205.967s = 2513.392s
\+ 210.731s = 2724.123s

convert 2724.123s to minutes : 45.40205 minutes
