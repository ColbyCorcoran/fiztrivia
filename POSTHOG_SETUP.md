# PostHog Analytics Setup for Fiz

## Overview
All code has been integrated! You just need to add the PostHog SDK package to Xcode.

## Steps to Add PostHog SDK

### 1. Open Xcode Project
- Open `Fiz.xcodeproj` in Xcode

### 2. Add Swift Package Dependency
1. In Xcode, go to **File → Add Package Dependencies...**
2. In the search bar, enter: `https://github.com/PostHog/posthog-ios`
3. Select the `posthog-ios` package
4. Choose version rule: **Up to Next Major Version** with **3.0.0**
5. Click **Add Package**
6. In the target selection dialog, make sure **Fiz** target is selected
7. Click **Add Package** again

### 3. Build and Test
1. Build the project (⌘+B)
2. If there are any build errors, clean the build folder (⌘+Shift+K) and rebuild

## What's Been Integrated

### ✅ Analytics Manager (`Fiz/Utils/AnalyticsManager.swift`)
- Opt-in analytics system (disabled by default)
- Privacy-focused configuration (no auto-tracking)
- All tracking methods implemented

### ✅ Settings Toggle (`PersonalizationSettingsView`)
- "Share Anonymous Analytics" toggle added
- Clear privacy description
- Located in Personalization settings

### ✅ Event Tracking
Automatically tracks these events (only when user opts in):

1. **app_opened** - When app becomes active
2. **app_backgrounded** - When app goes to background
3. **setting_changed** - When difficulty mode changes
   - Properties: `setting`, `value`
4. **category_completed** - When all questions in a category/subcategory are answered
   - Properties: `category`, `difficulty_mode`, `questions_answered`
5. **single_category_mode_enabled** - When user enables single category mode
   - Properties: `category`
6. **single_category_mode_disabled** - When user disables single category mode

### ✅ Privacy Features
- **Opt-in only** - Analytics disabled by default
- **No personal data** - No usernames, locations, or question answers tracked
- **Clear consent** - User sees toggle with explanation
- **Data clearing** - When user opts out, all data is reset

## Testing

After adding the package:

1. **Build the app** - Should compile without errors
2. **Navigate to Settings → Personalization**
3. **Enable "Share Anonymous Analytics"**
4. **Open PostHog dashboard** at https://us.posthog.com
5. **Check for events**:
   - `app_opened` should appear immediately
   - Try changing difficulty mode
   - Try completing a category

## Configuration

The AnalyticsManager is already configured with:
- **API Key**: `phc_pPTqusdmpJSoGYjymsgdz6BX6lcnUfuZzkKGw713JeZ`
- **Host**: `https://us.posthog.com`

No additional configuration needed!

## Troubleshooting

### Package won't add
- Make sure you have internet connection
- Try closing and reopening Xcode
- Search for the exact URL: `https://github.com/PostHog/posthog-ios`

### Build errors
- Clean build folder (⌘+Shift+K)
- Restart Xcode
- Make sure you selected the correct target (Fiz)

### No events showing in PostHog
- Verify analytics toggle is ON in Settings
- Check PostHog dashboard URL is correct
- Events may take a few minutes to appear
- Try triggering multiple events (open/close app, change settings)

## Next Steps

Once the package is added and building:
1. Test on a device/simulator
2. Enable analytics in settings
3. Verify events appear in PostHog dashboard
4. You're all set! 🎉
