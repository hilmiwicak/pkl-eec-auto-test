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
| R-08 | Menampilkan detail laporan kerja corrective maintenance teknisi |
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

        - [x] invalid
        - [x] valid

    - [x] logout

- kelola akun

    - [x] verif akun
    - [x] hapus akun

- kelola laporan kerja teknisi

    - lihat laporan kerja teknisi

        - [x] pm
        - [x] cm

    - lihat detail laporan kerja teknisi

        - [x] pm
        - [x] cm

    - cetak laporan kerja teknisi

- ubah password admin

    3 inputs : current password, new password, confirmation password

    1. [x] different current password, different confirmation password, valid new password
    2. [x] current password, confirmation password, and new password less than 6 characters
    3. [x] empty
    4. [x] same new password, all valid
    5. [x] new password not string (special characters & some characters from other than regular chars) with trailing space
    6. [x] {ERROR} current password not string with leading / trailing space

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

## Execution of Login and Logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

----------------------------------------------------------------------
Ran 2 tests in 34.190s

OK

Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 35
Milliseconds      : 469
Ticks             : 354691245
TotalDays         : 0.000410522274305556
TotalHours        : 0.00985253458333333
TotalMinutes      : 0.591152075
TotalSeconds      : 35.4691245
TotalMilliseconds : 35469.1245
```

## Execution of login, logout but already logged in

```
test_login (__main__.AuthenticationLogin) ... test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
ERROR: test_login (__main__.AuthenticationLogin) [valid email and password]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 30, in test_login
    login_page.login(constant.EMAIL, constant.PASSWORD)
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\pages\login.py", line 7, in login
    self.driver.find_element(
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 861, in find_element
    return self.execute(Command.FIND_ELEMENT, {"using": by, "value": value})["value"]
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 444, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\.win-venv\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 249, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"input.form-control[type='email']"}
  (Session info: chrome=109.0.5414.0)
Stacktrace:
Backtrace:
        (No symbol) [0x00796643]
        (No symbol) [0x0072BE21]
        (No symbol) [0x0062DA9D]
        (No symbol) [0x00661342]
        (No symbol) [0x0066147B]
        (No symbol) [0x00698DC2]
        (No symbol) [0x0067FDC4]
        (No symbol) [0x00696B09]
        (No symbol) [0x0067FB76]
        (No symbol) [0x006549C1]
        (No symbol) [0x00655E5D]
        GetHandleVerifier [0x00A0A142+2497106]
        GetHandleVerifier [0x00A385D3+2686691]
        GetHandleVerifier [0x00A3BB9C+2700460]
        GetHandleVerifier [0x00843B10+635936]
        (No symbol) [0x00734A1F]
        (No symbol) [0x0073A418]
        (No symbol) [0x0073A505]
        (No symbol) [0x0074508B]
        BaseThreadInitThunk [0x767A7BA9+25]
        RtlInitializeExceptionChain [0x774ABE3B+107]
        RtlClearBits [0x774ABDBF+191]


----------------------------------------------------------------------
Ran 2 tests in 19.738s

FAILED (errors=1)

Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 22
Milliseconds      : 160
Ticks             : 221605576
TotalDays         : 0.000256487935185185
TotalHours        : 0.00615571044444444
TotalMinutes      : 0.369342626666667
TotalSeconds      : 22.1605576
TotalMilliseconds : 22160.5576
```

## Execution of Login, test_edit_password, Logout without checking empty

```
test_login (__main__.AuthenticationLogin) ... ok
test_edit_password (__main__.PasswordEdit) ... test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
ERROR: test_edit_password (__main__.PasswordEdit) [6. current password not regular string]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 107, in test_edit_password
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
        (No symbol) [0x00DD6643]
        (No symbol) [0x00D6BE21]
        (No symbol) [0x00C6DA9D]
        (No symbol) [0x00CA1342]
        (No symbol) [0x00CA147B]
        (No symbol) [0x00CD8DC2]
        (No symbol) [0x00CBFDC4]
        (No symbol) [0x00CD6B09]
        (No symbol) [0x00CBFB76]
        (No symbol) [0x00C949C1]
        (No symbol) [0x00C95E5D]
        GetHandleVerifier [0x0104A142+2497106]
        GetHandleVerifier [0x010785D3+2686691]
        GetHandleVerifier [0x0107BB9C+2700460]
        GetHandleVerifier [0x00E83B10+635936]
        (No symbol) [0x00D74A1F]
        (No symbol) [0x00D7A418]
        (No symbol) [0x00D7A505]
        (No symbol) [0x00D8508B]
        BaseThreadInitThunk [0x76037BA9+25]
        RtlInitializeExceptionChain [0x7724BE3B+107]
        RtlClearBits [0x7724BDBF+191]


----------------------------------------------------------------------
Ran 3 tests in 83.823s

FAILED (errors=1)

Days              : 0
Hours             : 0
Minutes           : 1
Seconds           : 26
Milliseconds      : 675
Ticks             : 866752015
TotalDays         : 0.0010031852025463
TotalHours        : 0.0240764448611111
TotalMinutes      : 1.44458669166667
TotalSeconds      : 86.6752015
TotalMilliseconds : 86675.2015
```

## Execution of Login, test_edit_password, Logout with checking empty

```
test_login (__main__.AuthenticationLogin) ... ok
test_edit_password (__main__.PasswordEdit) ... test_logout (__main__.AuthenticationLogout) ... ok

======================================================================
ERROR: test_edit_password (__main__.PasswordEdit) [6. current password not regular string]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 109, in test_edit_password
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
        (No symbol) [0x00DD6643]
        (No symbol) [0x00D6BE21]
        (No symbol) [0x00C6DA9D]
        (No symbol) [0x00CA1342]
        (No symbol) [0x00CA147B]
        (No symbol) [0x00CD8DC2]
        (No symbol) [0x00CBFDC4]
        (No symbol) [0x00CD6B09]
        (No symbol) [0x00CBFB76]
        (No symbol) [0x00C949C1]
        (No symbol) [0x00C95E5D]
        GetHandleVerifier [0x0104A142+2497106]
        GetHandleVerifier [0x010785D3+2686691]
        GetHandleVerifier [0x0107BB9C+2700460]
        GetHandleVerifier [0x00E83B10+635936]
        (No symbol) [0x00D74A1F]
        (No symbol) [0x00D7A418]
        (No symbol) [0x00D7A505]
        (No symbol) [0x00D8508B]
        BaseThreadInitThunk [0x76037BA9+25]
        RtlInitializeExceptionChain [0x7724BE3B+107]
        RtlClearBits [0x7724BDBF+191]


----------------------------------------------------------------------
Ran 3 tests in 83.900s

FAILED (errors=1)

Days              : 0
Hours             : 0
Minutes           : 1
Seconds           : 26
Milliseconds      : 615
Ticks             : 866159826
TotalDays         : 0.00100249979861111
TotalHours        : 0.0240599951666667
TotalMinutes      : 1.44359971
TotalSeconds      : 86.6159826
TotalMilliseconds : 86615.9826
```

## Execution of Login, test_verify_account, test_delete_account, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_verify_account (__main__.AccountManagement) ... ok
test_delete_account (__main__.AccountManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

----------------------------------------------------------------------
Ran 4 tests in 38.765s

OK

Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 39
Milliseconds      : 253
Ticks             : 392536637
TotalDays         : 0.000454324811342593
TotalHours        : 0.0109037954722222
TotalMinutes      : 0.654227728333333
TotalSeconds      : 39.2536637
TotalMilliseconds : 39253.6637
```

## Execution of Login, test_view_cm, test_view_pm, test_view_cm, test_view_detail_pm, test_view_detail_cm, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_pm (__main__.MaintenanceManagement) ... ok
test_view_cm (__main__.MaintenanceManagement) ... ok
test_view_detail_pm (__main__.MaintenanceManagement) ... ok
test_view_detail_cm (__main__.MaintenanceManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

----------------------------------------------------------------------
Ran 6 tests in 65.119s

OK

Days              : 0
Hours             : 0
Minutes           : 1
Seconds           : 5
Milliseconds      : 641
Ticks             : 656411177
TotalDays         : 0.000759735158564815
TotalHours        : 0.0182336438055556
TotalMinutes      : 1.09401862833333
TotalSeconds      : 65.6411177
TotalMilliseconds : 65641.1177
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
        (No symbol) [0x00786643]
        (No symbol) [0x0071BE21]
        (No symbol) [0x0061DA9D]
        (No symbol) [0x00651342]
        (No symbol) [0x0065147B]
        (No symbol) [0x00688DC2]
        (No symbol) [0x0066FDC4]
        (No symbol) [0x00686B09]
        (No symbol) [0x0066FB76]
        (No symbol) [0x006449C1]
        (No symbol) [0x00645E5D]
        GetHandleVerifier [0x009FA142+2497106]
        GetHandleVerifier [0x00A285D3+2686691]
        GetHandleVerifier [0x00A2BB9C+2700460]
        GetHandleVerifier [0x00833B10+635936]
        (No symbol) [0x00724A1F]
        (No symbol) [0x0072A418]
        (No symbol) [0x0072A505]
        (No symbol) [0x0073508B]
        BaseThreadInitThunk [0x76037BA9+25]
        RtlInitializeExceptionChain [0x7724BE3B+107]
        RtlClearBits [0x7724BDBF+191]


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
        (No symbol) [0x00786643]
        (No symbol) [0x0071BE21]
        (No symbol) [0x0061DA9D]
        (No symbol) [0x00651342]
        (No symbol) [0x0065147B]
        (No symbol) [0x00688DC2]
        (No symbol) [0x0066FDC4]
        (No symbol) [0x00686B09]
        (No symbol) [0x0066FB76]
        (No symbol) [0x006449C1]
        (No symbol) [0x00645E5D]
        GetHandleVerifier [0x009FA142+2497106]
        GetHandleVerifier [0x00A285D3+2686691]
        GetHandleVerifier [0x00A2BB9C+2700460]
        GetHandleVerifier [0x00833B10+635936]
        (No symbol) [0x00724A1F]
        (No symbol) [0x0072A418]
        (No symbol) [0x0072A505]
        (No symbol) [0x0073508B]
        BaseThreadInitThunk [0x76037BA9+25]
        RtlInitializeExceptionChain [0x7724BE3B+107]
        RtlClearBits [0x7724BDBF+191]


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
Ran 6 tests in 261.288s

FAILED (failures=4, errors=2)

Days              : 0
Hours             : 0
Minutes           : 4
Seconds           : 25
Milliseconds      : 789
Ticks             : 2657896002
TotalDays         : 0.00307626852083333
TotalHours        : 0.0738304445
TotalMinutes      : 4.42982667
TotalSeconds      : 265.7896002
TotalMilliseconds : 265789.6002
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
        (No symbol) [0x00796643]
        (No symbol) [0x0072BE21]
        (No symbol) [0x0062DA9D]
        (No symbol) [0x00661342]
        (No symbol) [0x0066147B]
        (No symbol) [0x00698DC2]
        (No symbol) [0x0067FDC4]
        (No symbol) [0x00696B09]
        (No symbol) [0x0067FB76]
        (No symbol) [0x006549C1]
        (No symbol) [0x00655E5D]
        GetHandleVerifier [0x00A0A142+2497106]
        GetHandleVerifier [0x00A385D3+2686691]
        GetHandleVerifier [0x00A3BB9C+2700460]
        GetHandleVerifier [0x00843B10+635936]
        (No symbol) [0x00734A1F]
        (No symbol) [0x0073A418]
        (No symbol) [0x0073A505]
        (No symbol) [0x0074508B]
        BaseThreadInitThunk [0x767A7BA9+25]
        RtlInitializeExceptionChain [0x774ABE3B+107]
        RtlClearBits [0x774ABDBF+191]


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
        (No symbol) [0x00796643]
        (No symbol) [0x0072BE21]
        (No symbol) [0x0062DA9D]
        (No symbol) [0x00661342]
        (No symbol) [0x0066147B]
        (No symbol) [0x00698DC2]
        (No symbol) [0x0067FDC4]
        (No symbol) [0x00696B09]
        (No symbol) [0x0067FB76]
        (No symbol) [0x006549C1]
        (No symbol) [0x00655E5D]
        GetHandleVerifier [0x00A0A142+2497106]
        GetHandleVerifier [0x00A385D3+2686691]
        GetHandleVerifier [0x00A3BB9C+2700460]
        GetHandleVerifier [0x00843B10+635936]
        (No symbol) [0x00734A1F]
        (No symbol) [0x0073A418]
        (No symbol) [0x0073A505]
        (No symbol) [0x0074508B]
        BaseThreadInitThunk [0x767A7BA9+25]
        RtlInitializeExceptionChain [0x774ABE3B+107]
        RtlClearBits [0x774ABDBF+191]


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
Ran 6 tests in 247.195s

FAILED (failures=4, errors=2)

Days              : 0
Hours             : 0
Minutes           : 4
Seconds           : 11
Milliseconds      : 647
Ticks             : 2516475236
TotalDays         : 0.0029125870787037
TotalHours        : 0.0699020898888889
TotalMinutes      : 4.19412539333333
TotalSeconds      : 251.6475236
TotalMilliseconds : 251647.5236
```

## Execution of login, test_view_site, test_add_site, test_delete_site, logout

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
Ran 5 tests in 199.485s

FAILED (failures=2)

Days              : 0
Hours             : 0
Minutes           : 3
Seconds           : 23
Milliseconds      : 368
Ticks             : 2033682209
TotalDays         : 0.00235379885300926
TotalHours        : 0.0564911724722222
TotalMinutes      : 3.38947034833333
TotalSeconds      : 203.3682209
TotalMilliseconds : 203368.2209
```

## Execution of login, test_view_distribution, test_add_distribution, test_edit_distribution, test_delete_distribution, logout

```
test_login (__main__.AuthenticationLogin) ... ok
test_view_distribution (__main__.DistributionManagement) ... ok
test_add_distribution (__main__.DistributionManagement) ... ok
test_edit_distribution (__main__.DistributionManagement) ... ok
test_delete_distribution (__main__.DistributionManagement) ... ok
test_logout (__main__.AuthenticationLogout) ... ok

----------------------------------------------------------------------
Ran 6 tests in 103.212s

OK

Days              : 0
Hours             : 0
Minutes           : 1
Seconds           : 43
Milliseconds      : 654
Ticks             : 1036542844
TotalDays         : 0.00119970236574074
TotalHours        : 0.0287928567777778
TotalMinutes      : 1.72757140666667
TotalSeconds      : 103.6542844
TotalMilliseconds : 103654.2844
```

## Execution of login, test_view_stock, test_add_stock, test_edit_stock, test_delete_stock, test_view_stock_recommendation, logout

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
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 666, in test_edit_stock
    self.assertEqual(stock_view["keterangan"], stock_edit["keterangan"])
AssertionError: 'Ceng[206 chars]eksi. Pancit hilofagus moa palam babas segala [162 chars]ana.' != 'Ceng[206 chars]eksi.Pancit hilofagus moa palam babas segala k[161 chars]ana.'
- Cengkeh parestesia hipersensitif filibuster kekel tayibah rukam tridarma. Aruda kirab sekapar cik cangkuk akhlaki. Cupar sawah pasit kadim olanda suluk umbra fraktur. Perikemanusiaan biah gelitar setip ekstrospeksi. Pancit hilofagus moa palam babas segala kalsium. Cele mulato kusanin nobelium antonim ngakngikngok celepuk trisep. Lumuh sederum sipatung salina pendopo. Tania bongkrek tipis polis baba istanggi remas lana.
?                                                                                                                                                                                                                        -
+ Cengkeh parestesia hipersensitif filibuster kekel tayibah rukam tridarma. Aruda kirab sekapar cik cangkuk akhlaki. Cupar sawah pasit kadim olanda suluk umbra fraktur. Perikemanusiaan biah gelitar setip ekstrospeksi.Pancit hilofagus moa palam babas segala kalsium. Cele mulato kusanin nobelium antonim ngakngikngok celepuk trisep. Lumuh sederum sipatung salina pendopo. Tania bongkrek tipis polis baba istanggi remas lana.


----------------------------------------------------------------------
Ran 7 tests in 209.443s

FAILED (failures=1)

Days              : 0
Hours             : 0
Minutes           : 3
Seconds           : 31
Milliseconds      : 882
Ticks             : 2118822111
TotalDays         : 0.00245234040625
TotalHours        : 0.05885616975
TotalMinutes      : 3.531370185
TotalSeconds      : 211.8822111
TotalMilliseconds : 211882.2111
```

## Execution of login, test_view_site_stock, test_add_site_stock, test_edit_site_stock, test_delete_site_stock, logout

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
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 827, in test_edit_site_stock
    self.assertEqual(ref_des_view, ref_des_detail)
AssertionError: '7c049' != ''
- 7c049
+


----------------------------------------------------------------------
Ran 6 tests in 186.682s

FAILED (failures=1)

Days              : 0
Hours             : 0
Minutes           : 3
Seconds           : 9
Milliseconds      : 444
Ticks             : 1894441059
TotalDays         : 0.00219264011458333
TotalHours        : 0.05262336275
TotalMinutes      : 3.157401765
TotalSeconds      : 189.4441059
TotalMilliseconds : 189444.1059
```

## execution all except edit password

```
test_login (__main__.AuthenticationLogin) ... ok
test_verify_account (__main__.AccountManagement) ... ok
test_delete_account (__main__.AccountManagement) ... ok
test_view_pm (__main__.MaintenanceManagement) ... ok
test_view_cm (__main__.MaintenanceManagement) ... ok
test_view_detail_pm (__main__.MaintenanceManagement) ... ok
test_view_detail_cm (__main__.MaintenanceManagement) ... ok
test_view_expert (__main__.ExpertManagement) ... ok
test_add_expert (__main__.ExpertManagement) ... test_edit_expert (__main__.ExpertManagement) ... test_delete_expert (__main__.ExpertManagement) ... ok
test_view_site (__main__.SiteRadarManagement) ... ok
test_add_site (__main__.SiteRadarManagement) ... test_delete_site (__main__.SiteRadarManagement) ... ok
test_view_distribution (__main__.DistributionManagement) ... ok
test_add_distribution (__main__.DistributionManagement) ... ok
test_edit_distribution (__main__.DistributionManagement) ... ok
test_delete_distribution (__main__.DistributionManagement) ... ok
test_view_stock (__main__.StockManagement) ... ok
test_add_stock (__main__.StockManagement) ... ok
test_edit_stock (__main__.StockManagement) ... test_delete_stock (__main__.StockManagement) ... ok
test_view_stock_recommendation (__main__.StockManagement) ... ok
test_view_site_stock (__main__.SiteRadarStockManagement) ... ok
test_add_site_stock (__main__.SiteRadarStockManagement) ... ok
test_edit_site_stock (__main__.SiteRadarStockManagement) ... test_delete_site_stock (__main__.SiteRadarStockManagement) ... ok
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
        (No symbol) [0x00706643]
        (No symbol) [0x0069BE21]
        (No symbol) [0x0059DA9D]
        (No symbol) [0x005D1342]
        (No symbol) [0x005D147B]
        (No symbol) [0x00608DC2]
        (No symbol) [0x005EFDC4]
        (No symbol) [0x00606B09]
        (No symbol) [0x005EFB76]
        (No symbol) [0x005C49C1]
        (No symbol) [0x005C5E5D]
        GetHandleVerifier [0x0097A142+2497106]
        GetHandleVerifier [0x009A85D3+2686691]
        GetHandleVerifier [0x009ABB9C+2700460]
        GetHandleVerifier [0x007B3B10+635936]
        (No symbol) [0x006A4A1F]
        (No symbol) [0x006AA418]
        (No symbol) [0x006AA505]
        (No symbol) [0x006B508B]
        BaseThreadInitThunk [0x76897BA9+25]
        RtlInitializeExceptionChain [0x7726BE3B+107]
        RtlClearBits [0x7726BDBF+191]


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
        (No symbol) [0x00706643]
        (No symbol) [0x0069BE21]
        (No symbol) [0x0059DA9D]
        (No symbol) [0x005D1342]
        (No symbol) [0x005D147B]
        (No symbol) [0x00608DC2]
        (No symbol) [0x005EFDC4]
        (No symbol) [0x00606B09]
        (No symbol) [0x005EFB76]
        (No symbol) [0x005C49C1]
        (No symbol) [0x005C5E5D]
        GetHandleVerifier [0x0097A142+2497106]
        GetHandleVerifier [0x009A85D3+2686691]
        GetHandleVerifier [0x009ABB9C+2700460]
        GetHandleVerifier [0x007B3B10+635936]
        (No symbol) [0x006A4A1F]
        (No symbol) [0x006AA418]
        (No symbol) [0x006AA505]
        (No symbol) [0x006B508B]
        BaseThreadInitThunk [0x76897BA9+25]
        RtlInitializeExceptionChain [0x7726BE3B+107]
        RtlClearBits [0x7726BDBF+191]


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

======================================================================
FAIL: test_add_site (__main__.SiteRadarManagement) (<subtest>)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 447, in test_add_site
    self.assertEqual(message, "Data Created!")
AssertionError: '' != 'Data Created!'
+ Data Created!

======================================================================
FAIL: test_edit_stock (__main__.StockManagement) [1. checking whether the data in the list view is the same as in the edit form]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 666, in test_edit_stock
    self.assertEqual(stock_view["keterangan"], stock_edit["keterangan"])
AssertionError: 'Banc[125 chars]irma. Deltoid ordonansi usak cepat multiplikas[169 chars]pia.' != 'Banc[125 chars]irma.Deltoid ordonansi usak cepat multiplikasi[168 chars]pia.'
- Bancang detente kimiawi mundam pantau. Lenong lengkara pemendak paragog gedana-gedini baterai. Nominatif disilabik devosi fonon firma. Deltoid ordonansi usak cepat multiplikasi jasad. Pedoman brompit autoktonos tenok lampik maliki sangyang abrasi. Dogel ginding mahajana prasangka prive. Rayan dungas luar lumayan balui tomboi neurologi presbiopia.
?                                                                                                                                       -
+ Bancang detente kimiawi mundam pantau. Lenong lengkara pemendak paragog gedana-gedini baterai. Nominatif disilabik devosi fonon firma.Deltoid ordonansi usak cepat multiplikasi jasad. Pedoman brompit autoktonos tenok lampik maliki sangyang abrasi. Dogel ginding mahajana prasangka prive. Rayan dungas luar lumayan balui tomboi neurologi presbiopia.


======================================================================
FAIL: test_edit_site_stock (__main__.SiteRadarStockManagement) [1. check whether the data is the same as the one in the view all page]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\main.py", line 827, in test_edit_site_stock
    self.assertEqual(ref_des_view, ref_des_detail)
AssertionError: '9c326' != ''
- 9c326
+


----------------------------------------------------------------------
Ran 28 tests in 879.311s

FAILED (failures=10, errors=2)

Days              : 0
Hours             : 0
Minutes           : 14
Seconds           : 51
Milliseconds      : 444
Ticks             : 8914444772
TotalDays         : 0.010317644412037
TotalHours        : 0.247623465888889
TotalMinutes      : 14.8574079533333
TotalSeconds      : 891.4444772
TotalMilliseconds : 891444.4772
```
