#!/bin/bash

echo "========================================"
echo " Network Scanner Pro - Installation"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "Python version:"
python3 --version
echo ""

# Install dependencies
echo "Installing dependencies..."
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo " Installation completed successfully!"
    echo "========================================"
    echo ""
    echo "To run the application:"
    echo "  - GUI Mode: python3 app.py"
    echo "  - CLI Mode: python3 src/main.py -t 192.168.1.0/24"
    echo ""
else
    echo ""
    echo "ERROR: Installation failed!"
    exit 1
fi
