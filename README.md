# 🔍 Network Scanner Pro

<div align="center">

![Version](https://img.shields.io/badge/versiyon-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Lisans](https://img.shields.io/badge/lisans-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Modern arayüze sahip profesyonel, çapraz platform ağ tarayıcısı**

[Özellikler](#-özellikler) • [Kurulum](#-kurulum) • [Kullanım](#-kullanım) • [Sorun Giderme](#-sorun-giderme) • [SSS](#-sık-sorulan-sorular)

</div>

---

## 📸 Ekran Görüntüleri

### Ana Arayüz
Modern, koyu temalı kullanıcı dostu arayüz

### Tarama Sonuçları
Gerçek zamanlı port tarama ve host keşfi

### HTML Rapor
Profesyonel, detaylı tarama raporları

---

## ✨ Özellikler

### 🎨 Görsel Özellikler
- **Modern Koyu Tema** - Göz yormayan, profesyonel arayüz
- **Gerçek Zamanlı İstatistikler** - Anlık tarama ilerlemesi
- **Sidebar Tasarım** - Düzenli ve temiz kullanıcı arayüzü
- **Renkli İkon Sistemi** - Görsel geri bildirim

### ⚡ Teknik Özellikler
- **Çoklu İş Parçacığı** - 10-500 thread ile hızlı tarama
- **Host Keşfi** - Otomatik canlı cihaz tespiti
- **Port Tarama** - TCP port kontrolü ve servis tanıma
- **Esnek Port Seçimi** - Tekli, çoklu veya aralık desteği
- **Zaman Aşımı Ayarı** - 0.1-5.0 saniye arası özelleştirme

### 📊 Raporlama
- **JSON Export** - Programatik kullanım için
- **CSV Export** - Excel'e aktarım için
- **TXT Export** - Basit metin raporu
- **HTML Rapor** - Grafikli, profesyonel sunumlar

### 🌐 Uyumluluk
- Windows 10/11
- Linux (Ubuntu, Debian, Fedora, vb.)
- macOS (Intel & Apple Silicon)

---

## 📥 Kurulum

### Gereksinimler
- Python 3.8 veya üstü
- pip (Python paket yöneticisi)
- Internet bağlantısı (kurulum için)

### Hızlı Kurulum (Önerilen)

#### Windows Kullanıcıları İçin

1. **Projeyi İndirin**
   - GitHub'dan "Code" → "Download ZIP" tıklayın
   - ZIP dosyasını masaüstüne çıkarın

2. **Kurulum Dosyasını Çalıştırın**
   - `install.bat` dosyasına çift tıklayın
   - Kurulum otomatik olarak tamamlanacaktır

3. **Programı Başlatın**
   - `app.py` dosyasına çift tıklayın

#### Linux / macOS Kullanıcıları İçin

1. **Projeyi İndirin**
```bash
git clone https://github.com/Bor-Code/NetworkScanner.git
cd NetworkScanner
```

2. **Kurulum Scriptini Çalıştırılabilir Yapın**
```bash
chmod +x install.sh
```

3. **Kurulumu Başlatın**
```bash
./install.sh
```

4. **Programı Başlatın**
```bash
python3 app.py
```

### Manuel Kurulum (İleri Seviye)
```bash
# Depoyu klonlayın
git clone https://github.com/Bor-Code/NetworkScanner.git
cd NetworkScanner

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Programı çalıştırın
python app.py
```

---

## 🚀 Kullanım

### GUI Modu (Grafiksel Arayüz)

#### 1. Programı Başlatma
```bash
# Windows
python app.py

# Linux/Mac
python3 app.py
```

#### 2. Tarama Yapılandırması

**Target IP/Range (Hedef IP/Aralık):**
- Tek IP: `192.168.1.1`
- IP Aralığı (CIDR): `192.168.1.0/24`
- Alt ağ: `10.0.0.0/16`

**Ports (Portlar):**
- Tekli port: `80`
- Çoklu port: `80,443,8080`
- Port aralığı: `1-1000`
- Karışık: `22,80,443,3000-3100,8080`

**Threads (İş Parçacıkları):**
- Minimum: 10 (yavaş ama güvenli)
- Varsayılan: 100 (optimal)
- Maksimum: 500 (hızlı ama ağıra yük bindirir)

**Timeout (Zaman Aşımı):**
- Hızlı: 0.5 saniye
- Varsayılan: 1.0 saniye
- Güvenli: 2.0 saniye

#### 3. Tarama Başlatma
1. Sol panelde bilgileri doldurun
2. "▶ Start Scan" butonuna tıklayın
3. Sonuçları sağ panelde izleyin
4. İstatistikler üstte gerçek zamanlı güncellenir

#### 4. Sonuçları Kaydetme
- 💾 **Save Results**: JSON/CSV/TXT formatında kaydet
- 📊 **HTML Report**: Profesyonel HTML raporu oluştur
- 🗑 **Clear Results**: Ekranı temizle

---

### CLI Modu (Komut Satırı)

#### Temel Kullanım
```bash
# Basit ağ taraması
python src/main.py -t 192.168.1.0/24

# Belirli portları tara
python src/main.py -t 192.168.1.1 -p 80,443,8080

# Port aralığı tara
python src/main.py -t 192.168.1.0/24 -p 1-1000

# Sonuçları dosyaya kaydet
python src/main.py -t 192.168.1.0/24 -o sonuclar.json -f json
```

#### Gelişmiş Parametreler
```bash
# Özel thread sayısı ve timeout
python src/main.py -t 192.168.1.0/24 -T 200 --timeout 0.5

# CSV formatında kaydet
python src/main.py -t 192.168.1.0/24 -o rapor.csv -f csv

# Hızlı tarama (az port, yüksek thread)
python src/main.py -t 192.168.1.0/24 -p 80,443 -T 300 --timeout 0.3
```

#### Tüm Parametreler

| Parametre | Açıklama | Örnek |
|-----------|----------|-------|
| `-t, --target` | Hedef IP veya CIDR | `192.168.1.0/24` |
| `-p, --ports` | Taranacak portlar | `80,443,8080` |
| `-T, --threads` | Thread sayısı | `100` |
| `--timeout` | Bağlantı zaman aşımı | `1.0` |
| `-o, --output` | Çıktı dosyası | `sonuc.json` |
| `-f, --format` | Dosya formatı | `json/csv/txt` |

---

## 🛠️ Sorun Giderme

### Yaygın Problemler ve Çözümleri

#### ❌ Problem: "Python bulunamadı" hatası

**Çözüm:**
```bash
# Python kurulu mu kontrol edin
python --version

# Kurulu değilse:
# Windows: https://www.python.org/downloads/ adresinden indirin
# Linux: sudo apt install python3 python3-pip
# macOS: brew install python3
```

#### ❌ Problem: "ModuleNotFoundError: No module named 'scapy'"

**Çözüm:**
```bash
# Bağımlılıkları yeniden yükleyin
pip install -r requirements.txt

# veya tek tek
pip install scapy colorama pyyaml python-nmap
```

#### ❌ Problem: "Permission denied" (Yetki hatası)

**Çözüm:**
```bash
# Linux/Mac için yönetici izni
sudo python3 app.py

# Windows için: PowerShell'i "Yönetici olarak çalıştır"
```

#### ❌ Problem: GUI açılmıyor / pencere görünmüyor

**Çözüm:**
```bash
# tkinter kurulu mu kontrol edin
python -m tkinter

# Linux'ta tkinter kurulumu
sudo apt-get install python3-tk

# macOS'ta (Homebrew ile)
brew install python-tk
```

#### ❌ Problem: Tarama çok yavaş

**Çözüm:**
- Thread sayısını artırın (100 → 200)
- Timeout süresini azaltın (1.0 → 0.5)
- Daha az port tarayın
- Daha küçük IP aralığı seçin

#### ❌ Problem: "No active hosts found" (Aktif host bulunamadı)

**Çözüm:**
- IP aralığını kontrol edin
- Firewall'u geçici kapatın
- Ağ bağlantısını kontrol edin
- Timeout süresini artırın (1.0 → 2.0)

#### ❌ Problem: Bazı portlar bulunamıyor

**Çözüm:**
- Timeout süresini artırın
- Thread sayısını azaltın (stabilite için)
- Hedef firewall'ı kontrol edin
- Yönetici izniyle çalıştırın

#### ❌ Problem: HTML rapor oluşturulmuyor

**Çözüm:**
```bash
# Yazma izni olmayan klasör seçilmiş olabilir
# Masaüstüne veya Belgeler klasörüne kaydetmeyi deneyin
```

---

## 🔒 Güvenlik ve Yasal Uyarı

### ⚠️ ÖNEMLİ UYARI
Bu araç yalnızca eğitim amaçlı ve yetkili test senaryoları için tasarlanmıştır.

### Yasal Kullanım

#### ✅ İzin Verilen Kullanımlar:
- Kendi ağınızı test etme
- Yazılı izin alınmış sistemleri tarama
- Eğitim ortamlarında öğrenme
- Güvenlik denetimi (yetki dahilinde)

#### ❌ Yasadışı Kullanımlar:
- İzinsiz ağları tarama
- Başkalarının sistemlerine yetkisiz erişim
- Kötü niyetli amaçlarla kullanım
- Yasal izin olmadan kurumsal ağları tarama

### Sorumluluk Reddi
Bu yazılımın geliştiricileri:
- Yanlış kullanımdan sorumlu değildir
- Herhangi bir zarardan sorumlu tutulamaz
- Kullanıcıların yasal yükümlülüklerini üstlenir
- Yerel yasalara uyulmasını önerir

**Kullanmadan önce mutlaka izin alın!**

---

## 📚 Sık Sorulan Sorular (SSS)

### Genel Sorular

**S: Program ücretsiz mi?**  
C: Evet, tamamen açık kaynak ve ücretsizdir (MIT Lisansı).

**S: Hangi işletim sistemlerinde çalışır?**  
C: Windows 10/11, Linux, macOS'ta sorunsuz çalışır.

**S: Antivirüs programım uyarı veriyor, neden?**  
C: Port tarama araçları bazen false-positive tetikler. Kaynak kodu inceleyebilirsiniz.

**S: İnternet gerekli mi?**  
C: Sadece kurulum için. Tarama internet gerektirmez.

### Teknik Sorular

**S: En hızlı tarama ayarları neler?**  
C: 200-300 thread, 0.3-0.5 timeout, az sayıda port.

**S: Hangi portlar varsayılan olarak taranır?**  
C: 21, 22, 23, 25, 80, 443, 445, 3389, 8080

**S: CIDR notasyonu nedir?**  
C: /24 = 256 IP, /16 = 65,536 IP gibi.

**S: Birden fazla ağı aynı anda tarayabilir miyim?**  
C: CLI modunda birden fazla komut çalıştırabilirsiniz.

**S: Tarama sonuçlarını nasıl otomatikleştirebilirim?**  
C: CLI modunu cron job veya Task Scheduler ile kullanın.

### Sorun Giderme Soruları

**S: "Scan completed" diyor ama sonuç yok?**  
C: Ağda aktif host olmayabilir veya firewall engelliyor.

**S: Program dondu, ne yapmalıyım?**  
C: "Stop Scan" butonuna basın veya programı yeniden başlatın.

**S: EXE dosyası nasıl oluşturulur?**  
C: `pip install pyinstaller` sonra `python build_windows.py`

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Nasıl katkıda bulunabilirsiniz:

### Hata Bildirimi
1. Issues sayfasına gidin
2. "New Issue" tıklayın
3. Hatayı detaylı açıklayın
4. Ekran görüntüsü ekleyin

### Özellik Önerisi
1. Issues sayfasında "Feature Request" açın
2. Önerinizi detaylandırın
3. Kullanım senaryosu yazın

### Kod Katkısı
1. Repoyu fork edin
2. Yeni branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/YeniOzellik`)
5. Pull Request açın

---

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.

```
MIT License - Özgürce kullanabilir, değiştirebilir ve dağıtabilirsiniz.
```

---

## 📧 İletişim

- **GitHub Issues**: [Sorun Bildirin](https://github.com/Bor-Code/NetworkScanner/issues)
- **Email**: non.mrbora@gmail.com

---

<div align="center">

⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐

Made with ❤️ by [Bor-Code](https://github.com/Bor-Code)

[⬆ Başa Dön](#-network-scanner-pro)

</div>

---

# 🔍 Network Scanner Pro

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Professional cross-platform network scanner with modern GUI**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Troubleshooting](#-troubleshooting) • [FAQ](#-frequently-asked-questions)

</div>

---

## 📸 Screenshots

### Main Interface
Modern, dark-themed user-friendly interface

### Scan Results
Real-time port scanning and host discovery

### HTML Report
Professional, detailed scan reports

---

## ✨ Features

### 🎨 Visual Features
- **Modern Dark Theme** - Eye-friendly, professional interface
- **Real-Time Statistics** - Live scan progress tracking
- **Sidebar Design** - Clean and organized UI
- **Colorful Icon System** - Visual feedback

### ⚡ Technical Features
- **Multi-Threading** - Fast scanning with 10-500 threads
- **Host Discovery** - Automatic live device detection
- **Port Scanning** - TCP port checking and service identification
- **Flexible Port Selection** - Single, multiple, or range support
- **Timeout Control** - 0.1-5.0 second customization

### 📊 Reporting
- **JSON Export** - For programmatic use
- **CSV Export** - Excel integration
- **TXT Export** - Simple text reports
- **HTML Report** - Professional presentations with graphics

### 🌐 Compatibility
- Windows 10/11
- Linux (Ubuntu, Debian, Fedora, etc.)
- macOS (Intel & Apple Silicon)

---

## 📥 Installation

### Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for installation)

### Quick Install (Recommended)

#### For Windows Users

1. **Download the Project**
   - Click "Code" → "Download ZIP" on GitHub
   - Extract the ZIP file to your desktop

2. **Run the Installer**
   - Double-click `install.bat`
   - Installation will complete automatically

3. **Launch the Program**
   - Double-click `app.py`

#### For Linux / macOS Users

1. **Download the Project**
```bash
git clone https://github.com/Bor-Code/NetworkScanner.git
cd NetworkScanner
```

2. **Make the Script Executable**
```bash
chmod +x install.sh
```

3. **Start Installation**
```bash
./install.sh
```

4. **Launch the Program**
```bash
python3 app.py
```

### Manual Installation (Advanced)
```bash
# Clone the repository
git clone https://github.com/Bor-Code/NetworkScanner.git
cd NetworkScanner

# Install dependencies
pip install -r requirements.txt

# Run the program
python app.py
```

---

## 🚀 Usage

### GUI Mode (Graphical Interface)

#### 1. Starting the Program
```bash
# Windows
python app.py

# Linux/Mac
python3 app.py
```

#### 2. Scan Configuration

**Target IP/Range:**
- Single IP: `192.168.1.1`
- IP Range (CIDR): `192.168.1.0/24`
- Subnet: `10.0.0.0/16`

**Ports:**
- Single port: `80`
- Multiple ports: `80,443,8080`
- Port range: `1-1000`
- Mixed: `22,80,443,3000-3100,8080`

**Threads:**
- Minimum: 10 (slow but safe)
- Default: 100 (optimal)
- Maximum: 500 (fast but network-intensive)

**Timeout:**
- Fast: 0.5 seconds
- Default: 1.0 seconds
- Safe: 2.0 seconds

#### 3. Starting a Scan
1. Fill in the information in the left panel
2. Click the "▶ Start Scan" button
3. Watch the results in the right panel
4. Statistics update in real-time at the top

#### 4. Saving Results
- 💾 **Save Results**: Save in JSON/CSV/TXT format
- 📊 **HTML Report**: Generate professional HTML report
- 🗑 **Clear Results**: Clear the screen

---

### CLI Mode (Command Line)

#### Basic Usage
```bash
# Simple network scan
python src/main.py -t 192.168.1.0/24

# Scan specific ports
python src/main.py -t 192.168.1.1 -p 80,443,8080

# Scan port range
python src/main.py -t 192.168.1.0/24 -p 1-1000

# Save results to file
python src/main.py -t 192.168.1.0/24 -o results.json -f json
```

#### Advanced Parameters
```bash
# Custom thread count and timeout
python src/main.py -t 192.168.1.0/24 -T 200 --timeout 0.5

# Save in CSV format
python src/main.py -t 192.168.1.0/24 -o report.csv -f csv

# Quick scan (few ports, high threads)
python src/main.py -t 192.168.1.0/24 -p 80,443 -T 300 --timeout 0.3
```

#### All Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `-t, --target` | Target IP or CIDR | `192.168.1.0/24` |
| `-p, --ports` | Ports to scan | `80,443,8080` |
| `-T, --threads` | Thread count | `100` |
| `--timeout` | Connection timeout | `1.0` |
| `-o, --output` | Output file | `result.json` |
| `-f, --format` | File format | `json/csv/txt` |

---

## 🛠️ Troubleshooting

### Common Problems and Solutions

#### ❌ Problem: "Python not found" error

**Solution:**
```bash
# Check if Python is installed
python --version

# If not installed:
# Windows: Download from https://www.python.org/downloads/
# Linux: sudo apt install python3 python3-pip
# macOS: brew install python3
```

#### ❌ Problem: "ModuleNotFoundError: No module named 'scapy'"

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt

# or individually
pip install scapy colorama pyyaml python-nmap
```

#### ❌ Problem: "Permission denied"

**Solution:**
```bash
# For Linux/Mac, use admin privileges
sudo python3 app.py

# Windows: Run PowerShell as Administrator
```

#### ❌ Problem: GUI doesn't open / window not visible

**Solution:**
```bash
# Check if tkinter is installed
python -m tkinter

# Install tkinter on Linux
sudo apt-get install python3-tk

# On macOS (with Homebrew)
brew install python-tk
```

#### ❌ Problem: Scan is too slow

**Solution:**
- Increase thread count (100 → 200)
- Decrease timeout (1.0 → 0.5)
- Scan fewer ports
- Choose smaller IP range

#### ❌ Problem: "No active hosts found"

**Solution:**
- Check IP range
- Temporarily disable firewall
- Check network connection
- Increase timeout (1.0 → 2.0)

#### ❌ Problem: Some ports not found

**Solution:**
- Increase timeout
- Decrease thread count (for stability)
- Check target firewall
- Run with administrator privileges

#### ❌ Problem: HTML report not generating

**Solution:**
```bash
# Might be a read-only folder
# Try saving to Desktop or Documents folder
```

---

## 🔒 Security and Legal Warning

### ⚠️ IMPORTANT WARNING
This tool is designed for educational purposes only and authorized testing scenarios.

### Legal Use

#### ✅ Permitted Uses:
- Testing your own network
- Scanning systems with written permission
- Learning in educational environments
- Security audits (with authorization)

#### ❌ Illegal Uses:
- Scanning unauthorized networks
- Unauthorized access to others' systems
- Malicious use
- Corporate network scanning without legal permission

### Disclaimer
The developers of this software:
- Are not responsible for misuse
- Cannot be held liable for any damages
- Assume users' legal obligations
- Recommend compliance with local laws

**Always obtain permission before use!**

---

## 📚 Frequently Asked Questions (FAQ)

### General Questions

**Q: Is the program free?**  
A: Yes, completely open-source and free (MIT License).

**Q: Which operating systems does it work on?**  
A: Works smoothly on Windows 10/11, Linux, macOS.

**Q: My antivirus is warning me, why?**  
A: Port scanning tools sometimes trigger false-positives. You can review the source code.

**Q: Is internet required?**  
A: Only for installation. Scanning doesn't require internet.

### Technical Questions

**Q: What are the fastest scan settings?**  
A: 200-300 threads, 0.3-0.5 timeout, few ports.

**Q: Which ports are scanned by default?**  
A: 21, 22, 23, 25, 80, 443, 445, 3389, 8080

**Q: What is CIDR notation?**  
A: /24 = 256 IPs, /16 = 65,536 IPs, etc.

**Q: Can I scan multiple networks simultaneously?**  
A: You can run multiple commands in CLI mode.

**Q: How can I automate scan results?**  
A: Use CLI mode with cron job or Task Scheduler.

### Troubleshooting Questions

**Q: It says "Scan completed" but no results?**  
A: There may be no active hosts on the network or firewall is blocking.

**Q: Program froze, what should I do?**  
A: Press "Stop Scan" button or restart the program.

**Q: How to create EXE file?**  
A: `pip install pyinstaller` then `python build_windows.py`

---

## 🤝 Contributing

We welcome your contributions! How you can contribute:

### Bug Report
1. Go to Issues page
2. Click "New Issue"
3. Describe the bug in detail
4. Add screenshots

### Feature Request
1. Open "Feature Request" on Issues page
2. Detail your suggestion
3. Write use case

### Code Contribution
1. Fork the repo
2. Create new branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Added new feature'`)
4. Push your branch (`git push origin feature/NewFeature`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the MIT License. See LICENSE file for details.

```
MIT License - You can freely use, modify, and distribute.
```

---

## 📧 Contact

- **GitHub Issues**: [Report Issue](https://github.com/Bor-Code/NetworkScanner/issues)
- **Email**: non.mrbora@gmail.com

---

<div align="center">

⭐ If you liked the project, don't forget to star it! ⭐

Made with ❤️ by [Bor-Code](https://github.com/Bor-Code)

[⬆ Back to Top](#-network-scanner-pro)

</div>
