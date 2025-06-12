# 🎮 Gesture-Controlled T-Rex Game

Control the Chrome Dinosaur game using hand gestures with real-time AI tracking! Perfect for creating impressive LinkedIn demos showcasing computer vision and machine learning skills.

## 🎯 What It Does

Lift your index finger to make the T-Rex jump - it's that simple! The AI tracks your hand in real-time and controls the game seamlessly.

## ✨ Key Features

- **🧠 Real-time Hand Tracking**: MediaPipe AI running live in browser
- **👁️ Computer Vision**: Advanced 21-point hand landmark detection
- **🎮 Gesture Control**: Lift index finger = T-Rex jumps
- **📱 Single Screen Demo**: Game and AI tracking visible simultaneously
- **🚀 Zero Setup**: No installation required - runs entirely in browser
- **⚡ Optimized Performance**: 15 FPS processing for smooth gameplay

## 🚀 Quick Start

1. **Open the game**: Double-click `simple_gesture_game.html` 
2. **Allow camera access** when prompted
3. **Show your hand** to the camera
4. **Lift your index finger** to make T-Rex jump!

## 🎮 How to Play

- **👊 Keep fist closed**: T-Rex runs normally
- **☝️ Lift index finger**: T-Rex jumps instantly
- **📏 Optimal distance**: Keep hand 1-2 feet from camera
- **💡 Good lighting**: Ensures better hand detection

## 🔬 Technology Stack

- **MediaPipe**: Google's ML framework for hand tracking
- **JavaScript**: Real-time gesture processing and game control
- **HTML5 Canvas**: Live hand tracking visualization
- **WebGL**: GPU-accelerated neural network processing
- **PostMessage API**: Secure cross-frame communication

## 🎬 Perfect for Demos

The interface shows both the game AND the AI working together:
- ✅ Live camera feed with hand tracking overlay
- ✅ Real-time gesture detection (red dot = finger up, blue = down)
- ✅ Status indicators for camera and hand detection
- ✅ Clean, professional UI perfect for recording

## 🔧 Technical Implementation

### Hand Tracking Pipeline
1. **MediaPipe Analysis**: Detects 21 hand landmarks in real-time
2. **Gesture Recognition**: Compares index finger tip vs PIP joint position
3. **Jump Detection**: Triggers when finger lifts above threshold
4. **Game Control**: Sends spacebar event to T-Rex game via PostMessage

### Performance Optimizations
- **15 FPS Processing**: Balanced speed vs accuracy
- **Reduced Resolution**: 480x360 for optimal performance
- **Simplified Rendering**: Only key hand landmarks drawn
- **Efficient Updates**: DOM changes only when status changes
- **Model Complexity 0**: Fastest MediaPipe hand tracking model

## 📁 Project Files

```
├── 🎮 simple_gesture_game.html    # Main working game (OPEN THIS!)
├── 🦕 t-rex-runner/              # Chrome Dinosaur game files
└── 📖 README.md                  # This file
```

## 🎥 Recording Tips for LinkedIn

1. **Full-screen** the game for best video quality
2. **Good lighting** ensures reliable hand tracking  
3. **Demonstrate clearly**: Show fist → lift finger → T-Rex jumps
4. **Highlight the AI**: Point out the real-time hand tracking overlay
5. **Keep it short**: 30-60 seconds is perfect for social media

## 🌟 What This Demonstrates

- **Machine Learning in Browser**: Real-time neural network processing
- **Computer Vision**: 21-point hand landmark detection
- **Modern Web APIs**: MediaDevices, Canvas, WebGL, PostMessage
- **Performance Optimization**: Efficient real-time processing
- **UI/UX Design**: Clean interface for professional demos
- **Cross-Frame Communication**: Secure iframe interaction

## 💡 Technical Highlights

- **Zero Installation**: Pure browser-based implementation
- **Real-time AI**: 15 FPS hand tracking with sub-100ms latency
- **Secure Architecture**: PostMessage for safe iframe communication
- **Mobile-Ready**: Responsive design works on various screen sizes
- **Optimized Performance**: Reduced model complexity for smooth operation

## 🤝 Credits

- **T-Rex Game**: Google Chrome Team
- **Hand Tracking**: Google MediaPipe
- **AI Integration**: Custom gesture recognition implementation

## 📱 Great for Social Posts

Perfect hashtags:
```
#AI #MachineLearning #ComputerVision #MediaPipe #JavaScript
#WebDevelopment #GestureControl #TechDemo #Programming #Innovation
```

---

🎮 **Ready to play?** Open `simple_gesture_game.html` and start controlling T-Rex with your gestures! 