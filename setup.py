#!/usr/bin/env python3
"""
Setup script for T-Rex Gesture Control
Installs dependencies and checks system requirements
"""

import subprocess
import sys
import os
import cv2

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False

def check_camera():
    """Check if camera is available"""
    print("📷 Checking camera availability...")
    try:
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            cap.release()
            if ret:
                print("✅ Camera is working")
                return True
            else:
                print("⚠️  Camera detected but not working properly")
                return False
        else:
            print("❌ No camera detected")
            return False
    except Exception as e:
        print(f"❌ Camera check failed: {e}")
        return False

def create_launch_script():
    """Create a launch script for easy startup"""
    script_content = """#!/bin/bash
# T-Rex Gesture Control Launcher

echo "🦕 Starting T-Rex Gesture Control..."

# Check if game.html exists
if [ ! -f "game.html" ]; then
    echo "❌ game.html not found!"
    exit 1
fi

# Open the game in browser
echo "🎮 Opening game in browser..."
if command -v open >/dev/null 2>&1; then
    # macOS
    open game.html
elif command -v xdg-open >/dev/null 2>&1; then
    # Linux
    xdg-open game.html
elif command -v start >/dev/null 2>&1; then
    # Windows
    start game.html
else
    echo "Please open game.html in your browser manually"
fi

# Wait a moment for browser to load
echo "⏳ Waiting for game to load..."
sleep 3

# Start gesture control
echo "👋 Starting gesture control..."
echo "Position your hand in front of the camera and lift your index finger to jump!"
python gesture_control.py
"""
    
    with open("launch.sh", "w") as f:
        f.write(script_content)
    
    # Make executable on Unix systems
    if os.name != 'nt':
        os.chmod("launch.sh", 0o755)
    
    print("✅ Launch script created: launch.sh")

def main():
    """Main setup function"""
    print("🦕 T-Rex Gesture Control Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Check camera
    camera_ok = check_camera()
    
    # Create launch script
    create_launch_script()
    
    print("\n" + "=" * 40)
    print("🎉 Setup Complete!")
    print("\n📋 Next Steps:")
    print("1. Run: ./launch.sh (Unix) or python gesture_control.py")
    print("2. Open game.html in your browser if not opened automatically")
    print("3. Position your hand in front of the camera")
    print("4. Lift your index finger to make T-Rex jump!")
    
    if not camera_ok:
        print("\n⚠️  Warning: Camera issues detected")
        print("   Make sure your camera is connected and not in use")
    
    print("\n🆘 If you need help, check README.md")

if __name__ == "__main__":
    main() 