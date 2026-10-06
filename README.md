# Socket-Python

一個以 Python 標準函式庫實作的互動式 TCP/UDP Socket 命令列工具。啟動伺服器與客戶端後，可在終端機輸入文字並互相傳送。

## 功能

- 支援 TCP 與 UDP。
- 可選擇伺服器或客戶端模式。
- 支援 IPv4 與 IPv6 位址。
- 預設使用連接埠 `8787`。
- 不需要安裝第三方 Python 套件。

## 系統需求

- Python 3
- 支援 IPv6 的作業系統（伺服器以 IPv6 通配位址監聽，並嘗試同時接受 IPv4 連線）

## 使用方式

請在專案根目錄開啟終端機執行：

```bash
python3 Socket.py [模式] [選項]
```

> Windows 可改用 `py` 、 `python`或 `python3`；macOS / Linux 通常使用 `python3`。

### 伺服器

以預設 TCP 連接埠 `8787` 啟動伺服器：

```bash
python3 Socket.py --server
```

啟動 UDP 伺服器：

```bash
python3 Socket.py --server --type udp
```

自訂連接埠：

```bash
python3 Socket.py --server --type tcp --port 9000
```

### 客戶端

連線到本機的 TCP 伺服器：

```bash
python3 Socket.py --client 127.0.0.1
```

連線到指定 IPv4 位址的 UDP 伺服器：

```bash
python3 Socket.py --client 192.168.1.20 --type udp
```

自訂連接埠或使用 IPv6 位址：

```bash
python3 Socket.py --client 2001:db8::1 --type tcp --port 9000
```

> 客戶端參數需提供 IP 位址；目前不支援以主機名稱（例如 `localhost` 或網域名稱）連線。

### 參數

| 參數 | 說明 |
| --- | --- |
| `-s`, `--server` | 以伺服器模式執行 |
| `-c IP`, `--client IP` | 以客戶端模式執行，並指定伺服器 IP 位址 |
| `-t`, `--type` | 通訊協定：`tcp` 或 `udp`，預設為 `tcp` |
| `-p`, `--port` | 連接埠，預設為 `8787` |
| `-v`, `--verbose` | 詳細模式選項（目前尚未有額外輸出，見「注意事項」） |
| `-h`, `--help` | 顯示說明 |

伺服器與客戶端模式必須擇一。查看命令列說明：

```bash
python3 Socket.py --help
```

## 互動操作

1. 在一個終端機啟動伺服器。
2. 在另一個終端機使用相同的協定與連接埠啟動客戶端。
3. 在任一端的提示符後輸入文字並按 Enter，即可傳送訊息。
4. 輸入 `exit` 可結束該端的互動程序。

若要從其他電腦連線，請使用伺服器可到達的 IP 位址，並確認防火牆允許該連接埠的 TCP 或 UDP 流量。

## 專案結構

```text
.
├── Socket.py                 # 命令列入口
├── README.md                 # 專案說明
├── sync.sh                   # 同步腳本（Linux / macOS）
├── w_sync.cmd                # 同步腳本（Windows）
└── func/
    ├── args_parse.py         # 命令列參數
    ├── config.py             # 預設連接埠與提示字
    ├── ip_handler/
    │   └── sk_ip.py          # IP 位址與通訊協定家族判斷
    ├── protocols/            # TCP/UDP 客戶端與伺服器
    │   ├── TCP_Client.py
    │   ├── TCP_Server.py
    │   ├── UDP_Client.py
    │   └── UDP_Server.py
    ├── send_recv/            # 訊息收發
    │   ├── sk_recv.py
    │   └── sk_send.py
    └── ths/                  # 接收訊息的執行緒
        ├── sk_thread_tcp.py
        └── sk_thread_udp.py
```

## 注意事項

- TCP 伺服器目前只接受一個客戶端連線；若要接受其他客戶端，需重新啟動伺服器。
- UDP 伺服器會記錄最近收到封包的客戶端，伺服器端輸入的訊息會回覆給該客戶端。
- TCP 是串流協定，沒有內建訊息邊界；大量或快速傳送時，一次接收的資料可能不是恰好一筆輸入訊息。
- `--verbose` 目前僅作為命令列選項存在，程式尚未依此切換額外的詳細輸出。
