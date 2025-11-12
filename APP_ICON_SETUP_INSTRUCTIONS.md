# Alternate App Icon Setup Instructions for Fiz

This guide will walk you through setting up alternate app icons in your Xcode project so users can select their preferred Fiz icon from within the app.

---

## 📋 Overview

Your app currently has **6 app icon options**:
1. **Correct** (Default - ships with the app)
2. Regular Pose
3. Happy Smirk
4. Incorrect
5. Leaderboard
6. New High Score

---

## 🎨 Step 1: Prepare Your App Icon Images

You'll need **1024x1024px PNG files** for each icon variant (without transparency for best results).

### File naming convention:
Create PNG files with these exact names:
- `AppIcon-Correct.png` (Your default icon - also goes in the main AppIcon set)
- `AppIcon-RegularPose.png`
- `AppIcon-HappySmirk.png`
- `AppIcon-Incorrect.png`
- `AppIcon-Leaderboard.png`
- `AppIcon-NewHighScore.png`

**Important**: Each file should be **1024x1024px** and ideally without transparency (solid background).

---

## 📁 Step 2: Add Icons to Your Xcode Project

### A. Add the Default Icon (Correct)
1. Open your Xcode project
2. In the **Project Navigator** (left sidebar), find `Assets.xcassets`
3. Click on **AppIcon** (the existing app icon set)
4. Drag and drop your `AppIcon-Correct.png` file into the **1024x1024 slot** (iPhone App iOS 1024pt)
5. Xcode will automatically generate all required sizes

### B. Create Alternate Icon Sets
For each of the 5 alternate icons, repeat these steps:

1. In `Assets.xcassets`, **right-click** in the empty space
2. Select **App Icons & Launch Images → New iOS App Icon**
3. Name it exactly as follows (match the code):
   - `AppIcon-RegularPose`
   - `AppIcon-HappySmirk`
   - `AppIcon-Incorrect`
   - `AppIcon-Leaderboard`
   - `AppIcon-NewHighScore`

4. For each new icon set, drag the corresponding 1024x1024 PNG into the slot

**Visual example of what you'll see in Assets.xcassets:**
```
Assets.xcassets/
├── AppIcon (default - uses AppIcon-Correct.png)
├── AppIcon-RegularPose
├── AppIcon-HappySmirk
├── AppIcon-Incorrect
├── AppIcon-Leaderboard
└── AppIcon-NewHighScore
```

---

## ⚙️ Step 3: Configure Info.plist

1. In Xcode, find your `Info.plist` file (usually in the project root or in the Fiz folder)
2. **Right-click** anywhere in the property list and select **Add Row**
3. Type: `CFBundleIcons` (or select "Icon files (iOS 5)" from the dropdown)
4. Click the disclosure triangle to expand it
5. Add a new row inside and name it: `CFBundleAlternateIcons`
6. Make sure it's a **Dictionary** type
7. Add entries for each alternate icon:

### Info.plist structure:
```xml
<key>CFBundleIcons</key>
<dict>
    <key>CFBundleAlternateIcons</key>
    <dict>
        <key>AppIcon-RegularPose</key>
        <dict>
            <key>CFBundleIconFiles</key>
            <array>
                <string>AppIcon-RegularPose</string>
            </array>
            <key>UIPrerenderedIcon</key>
            <false/>
        </dict>
        <key>AppIcon-HappySmirk</key>
        <dict>
            <key>CFBundleIconFiles</key>
            <array>
                <string>AppIcon-HappySmirk</string>
            </array>
            <key>UIPrerenderedIcon</key>
            <false/>
        </dict>
        <key>AppIcon-Incorrect</key>
        <dict>
            <key>CFBundleIconFiles</key>
            <array>
                <string>AppIcon-Incorrect</string>
            </array>
            <key>UIPrerenderedIcon</key>
            <false/>
        </dict>
        <key>AppIcon-Leaderboard</key>
        <dict>
            <key>CFBundleIconFiles</key>
            <array>
                <string>AppIcon-Leaderboard</string>
            </array>
            <key>UIPrerenderedIcon</key>
            <false/>
        </dict>
        <key>AppIcon-NewHighScore</key>
        <dict>
            <key>CFBundleIconFiles</key>
            <array>
                <string>AppIcon-NewHighScore</string>
            </array>
            <key>UIPrerenderedIcon</key>
            <false/>
        </dict>
    </dict>
</dict>
```

### Or using Xcode's plist editor:
```
CFBundleIcons (Dictionary)
└── CFBundleAlternateIcons (Dictionary)
    ├── AppIcon-RegularPose (Dictionary)
    │   ├── CFBundleIconFiles (Array)
    │   │   └── Item 0 (String): AppIcon-RegularPose
    │   └── UIPrerenderedIcon (Boolean): NO
    ├── AppIcon-HappySmirk (Dictionary)
    │   ├── CFBundleIconFiles (Array)
    │   │   └── Item 0 (String): AppIcon-HappySmirk
    │   └── UIPrerenderedIcon (Boolean): NO
    ├── AppIcon-Incorrect (Dictionary)
    │   ├── CFBundleIconFiles (Array)
    │   │   └── Item 0 (String): AppIcon-Incorrect
    │   └── UIPrerenderedIcon (Boolean): NO
    ├── AppIcon-Leaderboard (Dictionary)
    │   ├── CFBundleIconFiles (Array)
    │   │   └── Item 0 (String): AppIcon-Leaderboard
    │   └── UIPrerenderedIcon (Boolean): NO
    └── AppIcon-NewHighScore (Dictionary)
        ├── CFBundleIconFiles (Array)
        │   └── Item 0 (String): AppIcon-NewHighScore
        └── UIPrerenderedIcon (Boolean): NO
```

**⚠️ Important Notes:**
- The key names (e.g., `AppIcon-RegularPose`) **must exactly match** the icon set names in Assets.xcassets
- The string in `CFBundleIconFiles` array **must also exactly match** the icon set name
- Do **NOT** include "Correct" in `CFBundleAlternateIcons` - it's your default icon

---

## 🧪 Step 4: Test in Xcode

1. **Clean Build Folder**: In Xcode menu bar, go to **Product → Clean Build Folder** (Shift+Cmd+K)
2. **Build and Run**: Run your app on a real device or simulator (Cmd+R)
3. Go to **Settings → Personalization → App Icon**
4. Tap different icons to test switching
5. Press the home button and verify the icon changed on your home screen

---

## 📱 Step 5: Important Testing Notes

### Simulator Limitations:
- ✅ Icon switching **WILL work** in the simulator
- ✅ You'll see the icons in Settings
- ✅ The app will call the API successfully
- ❌ The home screen icon **may not update visually** in simulator
- ✅ **Always test on a real device** to see the actual home screen icon change

### Real Device Testing:
1. Connect your iPhone/iPad
2. Build and run on the device
3. Go to Settings → Personalization → App Icon
4. Tap an icon to switch
5. Press the home button (or swipe up on newer devices)
6. You should see the new icon on your home screen immediately
7. Check the App Library to see it there too

---

## 🔍 Troubleshooting

### Icons not appearing in Settings?
- Verify icon set names in `Assets.xcassets` exactly match the names in your code
- Check that all 6 icon sets exist in Assets.xcassets
- Ensure each icon set has the 1024x1024 image

### Icon not changing on home screen?
- Make sure you're testing on a **real device** (not simulator)
- Clean build folder and rebuild
- Check the Xcode console for any error messages when tapping an icon
- Verify `Info.plist` has `CFBundleAlternateIcons` configured correctly

### App crashes when selecting icon?
- Check the console error - likely a name mismatch
- Verify icon names in code match `Info.plist` match `Assets.xcassets`

### Icons look wrong?
- Ensure images are 1024x1024px
- Check that images don't have transparency (use solid backgrounds)
- Verify you're using PNG format

---

## ✅ Final Checklist

Before submitting to TestFlight/App Store:

- [ ] All 6 icon PNG files prepared (1024x1024px each)
- [ ] Default icon (AppIcon-Correct) added to main AppIcon set
- [ ] 5 alternate icon sets created in Assets.xcassets with exact names
- [ ] Info.plist configured with `CFBundleAlternateIcons`
- [ ] Tested on real device - icons switch correctly
- [ ] Home screen updates when icon is changed
- [ ] App Library shows correct icon

---

## 📚 Additional Resources

- [Apple's Human Interface Guidelines - App Icons](https://developer.apple.com/design/human-interface-guidelines/app-icons)
- [Apple Documentation - Alternate App Icons](https://developer.apple.com/documentation/uikit/uiapplication/2806818-setalternateiconname)

---

## 🎉 You're Done!

Once you've completed all steps, your users will be able to:
1. Open the app
2. Go to Settings → Personalization
3. Tap "App Icon"
4. Choose from 6 different Fiz mascot designs
5. See their selection immediately on their home screen

The app is already coded and ready - you just need to add the icon assets and configure the plist!
