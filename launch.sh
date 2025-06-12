#!/bin/bash
# T-Rex Gesture Control Launcher

echo "🚀 Launching AI-Powered T-Rex Game..."
echo "🤖 Features: Real-time Hand Gesture Control using MediaPipe Neural Network"
echo ""
echo "📋 Instructions:"
echo "   1. Allow camera access when prompted"
echo "   2. Position your hand in front of the camera"
echo "   3. Make a fist to let the T-Rex run"
echo "   4. Lift your index finger to make the T-Rex jump!"
echo ""
echo "🎬 Perfect for recording LinkedIn demos!"
echo ""

# Check if game.html exists
if [ ! -f "game.html" ]; then
    echo "❌ game.html not found!"
    exit 1
fi

# Open the game page
open game.html

echo "✅ Game launched! Enjoy your AI-powered gaming experience!"
