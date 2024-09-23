# 安裝 Git Bash (2.46.0)64bits
## 確保wget跟md5sum for windows已安裝(ref#1)

### (ref#1)
下載 Git for Windows：
    wget --version
    md5sum --version
安裝 wget：
下載 wget：
    前往 GNU Wget for Windows，並下載合適的 Windows 版本（通常是 wget.exe）。
    將 wget 解壓到指定的目錄：

1. 將其解壓縮到 C:\wget 目錄。
2. 將 wget 添加到系統環境變量：
3. 右鍵點擊「此電腦」，選擇「屬性」。
4. 點擊「高級系統設置」。
5. 點擊「環境變量」。
6. 在「系統變量」中找到 Path，選擇「編輯」。
7. 點擊「新建」，然後添加你解壓的 wget.exe 所在的文件夾路徑，例如 C:\wget。

# 利用llama3提供的網址在llama3-main中執行./download.sh(有24小時效性)
# 選擇8b-instruct
--2024-09-11 20:57:25--  https://download6.llamameta.net/8b_instruction_tuned/checklist.chk?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoia2dwaHo5bGF3NjU0aDcwdXA3ZmQ4cGNvIiwiUmVzb3VyY2UiOiJodHRwczpcL1wvZG93bmxvYWQ2LmxsYW1hbWV0YS5uZXRcLyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3MjYxNDM0OTB9fX1dfQ__&Signature=SQsafuEOIuA0I4HqbY5Iud6-i0O82X0Ol0y59b1lPGFjcNPAIM1sXZqkLLcgWj~VBmPWQ~11SIgzBgZp~hn49ezKwjRK4M2jI-2wZR0C5up1fkcDVHQCEo4wt-S9qe03JMxD3UgKiXSzAXi-MMuDUgTH2rrWOJoBA-d1vbP0S8CZAFKpxDR496eSUKm4R5S2FIdCoL0f4Q-bFl~-M~pVoMgD6Vq1GL-hCC4dsr5Ge28HEItlnfJttc1BiYeCoPZVKps7hbaKwt82znZ0RQQcgeNDnWYZlJIHNV2u2-AWyQEIEVYaVRYRcoB1pYkEaNRAULLn9xf4Zy3Q7Yv-ENDppQ__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=982262640550077
Resolving download6.llamameta.net (download6.llamameta.net)... 13.35.35.11, 13.35.35.7, 13.35.35.46, ...
Connecting to download6.llamameta.net (download6.llamameta.net)|13.35.35.11|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 150 [binary/octet-stream]
Saving to: './Meta-Llama-3-8B-Instruct/checklist.chk'

     0K                                                       100%  768K=0s

2024-09-11 20:57:25 (768 KB/s) - './Meta-Llama-3-8B-Instruct/checklist.chk' saved [150/150]

Checking checksums
consolidated.00.pth: OK
params.json: OK
tokenizer.model: OK

# 參考https://medium.com/@softaverse/llama-3%E4%BE%86%E4%BA%86-%E6%9C%AC%E7%AF%87%E4%B8%80%E6%AD%A5%E6%AD%A5%E6%95%99%E4%BD%A0%E5%A6%82%E4%BD%95%E5%9C%A8%E6%9C%AC%E6%A9%9F%E5%AE%89%E8%A3%9D%E4%BD%BF%E7%94%A8-bc9efad57bd2


使用Ollama：簡單易用的開源 LLM 操作平台
Ollama 是一個開源的大型語言模型平台，允許使用者在本地端運行各種模型，如 Llama 3 等。它的設計目標是優化模型的設置和配置過程，包括 GPU 的使用。


# 在終端機執行
ollama run llama3

https://ywctech.net/ml-ai/ollama-first-try/#api-%e4%bb%8b%e9%9d%a2


# 目前打算在終端機執行自己的LLM MODEL
## 1.更改LLAMA3 8b-instruct的component

### 取得 Ollama 的公鑰
#### 1.
cat ~/.ollama/id_ed25519.pub
取得公鑰後，將其添加到指定的位置（根據圖片，應該是在 Ollama 的設定中，點擊 settings 連結添加）。
如果你已經修改了 Llama3 或想要推送一個新的模型，可以按照以下步驟操作：

## 2.將自己的model放到https://ollama.com/上傳
## 3.再到終端機執行ollama run llama3_edited_by_yuhao
