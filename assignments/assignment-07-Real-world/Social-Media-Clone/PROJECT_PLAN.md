Our new strict Phase 7 order
STEP 1 — Registration System ✅ currently incomplete

We finish everything related to registration:

Registration page
Username
Email
Password
Password confirmation
Custom form styling
Custom placeholders
Custom error messages
Password validation
Duplicate username handling
Email validation
Successful registration flow
Redirect after registration
Registration CSS
Responsive mobile/desktop design
Link to login
Copyright/footer
Security review
Test everything

Only when Step 1 is fully finished do we move on.

STEP 2 — Login & Account Recovery
2A — Login
Login functionality
Login form
Custom CSS
Error messages
Invalid credentials
Successful login
Redirect to Home
Remember authentication state
Logout
Responsive design
Login/register navigation
2B — Forgot Password
Forgot password page
Email form
Email validation
Password reset token
Reset email configuration
Password reset confirmation page
New password page
Custom CSS for every page
Success/error messages
2C — Forgot Username

We need to make an important design decision here.

Django does not normally provide a "forgot username" flow, because usernames are not usually recovered through a password reset.

For our app, we can create:

Forgot username?
       ↓
Enter registered email
       ↓
Django finds the account
       ↓
Username recovery response/email

We will build that as its own feature.

STEP 3 — Home Page

Only after authentication is completely finished.

We will build:

Complete page structure
Navigation
User menu
Profile shortcut
Logout
Main feed layout
Create-post area
Post cards
Profile pictures
Responsive desktop layout
Responsive mobile layout
Mobile navigation
CSS
JavaScript where actually useful
Empty-state UI
Error states
Loading states if needed

The design will be inspired by the general usability of social media, but original—not a direct copy of Facebook.

STEP 4 — Profile
Profile page
Profile header
Profile picture
Display name
Username
Bio
Location
Website
Date joined
Profile statistics
User's posts
Responsive design
Complete CSS
STEP 5 — Edit Profile
Edit profile page
Display name
Bio
Location
Website
Profile picture
Validation
Ownership security
Custom error messages
CSS
Responsive design
Success messages
Sub-step: Account settings

If needed:

Change password
Update email
Account settings page
Security considerations
Custom CSS
After those five steps

Then we move to:

STEP 6 → Posts
STEP 7 → Likes
STEP 8 → Comments
STEP 9 → Follow system
STEP 10 → Search
STEP 11 → Notifications
STEP 12 → Messaging

And each of those will also be completed fully before moving on.