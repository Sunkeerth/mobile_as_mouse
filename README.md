 Gyro Phone Mouse

Overview
"Gyro Phone Mouse" is a web-based application that transforms your smartphone or tablet into a versatile remote control for your computer. It allows you to:
- Use your device as a touchpad to control the mouse.
- Perform left-click, right-click, and pinch-to-zoom gestures.
- Draw directly on your mobile screen and see it reflected on your computer.
- Use your device for editing purposes, such as presentations (PPT), modeling, and other creative tasks.

This project is ideal for remote work, presentations, or creative projects where a traditional mouse or touchpad is unavailable or inconvenient.

 Features
- **Mouse Movement:** Swipe on your phone/tablet screen to move the computer mouse.
- **Left & Right Click:** Tap buttons on the screen to perform mouse clicks.
- **Pinch-to-Zoom:** Use a two-finger gesture to zoom in and out.
- **Drawing Mode:** Draw on your mobile screen and see it appear on your computer in real-time.
- **Editing & Modeling:** Use your device to edit presentations (PPT), 3D models, or other creative projects.
- **Wireless Control:** Connects over WiFi, requiring no physical connection.
- **Cross-Platform:** Works on any device with a modern web browser.

---

 Technologies Used
- **Frontend:** HTML, CSS, JavaScript (Socket.IO for real-time communication)
- **Backend:** Python, Flask, Flask-SocketIO
- **Automation:** PyAutoGUI (for simulating mouse actions and drawing)
- **Drawing Integration:** HTML5 Canvas (for drawing on the mobile screen)



Usage
 **Mouse Control**
- **Move Mouse:** Swipe on the phone/tablet screen.
- **Left Click:** Tap the "Left Click" button.
- **Right Click:** Tap the "Right Click" button.
- **Zoom In/Out:** Use a two-finger pinch gesture.

 **Drawing Mode**
- Enable drawing mode by tapping the "Draw" button on the screen.
- Draw on your mobile screen using your finger or stylus.
- See your drawing appear on your computer in real-time.

 **Editing & Modeling**
- Use your device to:
  - Edit presentations (PPT) by navigating slides and making annotations.
  - Manipulate 3D models or creative projects with precision.
  - Perform other editing tasks that require a touch interface.

 Troubleshooting
- **Connection Issues:**
  - Ensure that both devices are on the same WiFi network.
  - Replace `<your-pc-ip>` with the actual IP of your computer.
- **Touch Gestures Not Working:**
  - Try a different browser on your phone/tablet.
  - Ensure that your browser supports touch events.
- **Drawing Not Appearing:**
  - Check if the drawing mode is enabled.
  - Ensure that the backend is running and connected.

 Future Enhancements
- **Multi-Touch Support:** Add support for more advanced multi-touch gestures.
- **Customizable Buttons:** Allow users to customize buttons for specific tasks.
- **Integration with Creative Software:** Add direct integration with tools like Photoshop, Blender, or PowerPoint.
- **Offline Mode:** Enable offline functionality for local use without WiFi.


 Contributing
Contributions are welcome! If you'd like to contribute, please:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

Acknowledgments
- **Flask** and **Flask-SocketIO** for enabling real-time communication.
- **PyAutoGUI** for simulating mouse and keyboard actions.
- **HTML5 Canvas** for enabling drawing functionality.

---
