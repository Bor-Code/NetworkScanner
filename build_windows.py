import PyInstaller.__main__
import os
import sys

print("=" * 60)
print("  Network Scanner Pro - Windows Build")
print("=" * 60)
print()

if not os.path.exists('icon.ico'):
    print("⚠️  Warning: icon.ico not found!")
    print("   Using default icon...")
    icon_param = []
else:
    print("✓ Icon file found")
    icon_param = ['--icon=icon.ico']

print("Building executable...")
print()

try:
    PyInstaller.__main__.run([
        'app.py',
        '--name=NetworkScannerPro',
        '--onefile',
        '--windowed',
        *icon_param,
        '--add-data=src;src',
        '--hidden-import=tkinter',
        '--hidden-import=tkinter.ttk',
        '--hidden-import=tkinter.filedialog',
        '--hidden-import=tkinter.messagebox',
        '--hidden-import=scapy.all',
        '--hidden-import=colorama',
        '--clean',
        '--noconfirm',
    ])
    
    print()
    print("=" * 60)
    print("✓ Build completed successfully!")
    print("=" * 60)
    print()
    print("📦 Executable location: dist/NetworkScannerPro.exe")
    print()
    print("You can now distribute the .exe file!")
    print()
    
except Exception as e:
    print()
    print("=" * 60)
    print("❌ Build failed!")
    print("=" * 60)
    print()
    print(f"Error: {str(e)}")
    print()
    sys.exit(1)
