# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Notes |
| --- | --- | --- |
| 404 | ![screenshot](documentation/validation/html/html-validation-404.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. |
| About | ![screenshot](documentation/validation/html/html-validation-about.png) | Pass: No Errors |
| Base/Home | ![screenshot](documentation/validation/html/html-validation-base.png) | Pass: No Errors |
| Booking Form | ![screenshot](documentation/validation/html/html-validation-booking_confirmation.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. |
| Cancel Booking Confirmation | ![screenshot](documentation/validation/html/html-validation-cancel_booking_confirmation.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. |
| Delete Review Confirmation | ![screenshot](documentation/validation/html/html-validation-confirm_delete_review.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. |
| Logout Confirmation | ![screenshot](documentation/validation/html/html-validation-logout_confirmation.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. |
| Contact | ![screenshot](documentation/validation/html/html-validation-contact.png) | Pass: No Errors |
| Review Edit | ![screenshot](documentation/validation/html/html-validation-edit_review.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. |
| Itinerary Cards | ![screenshot](documentation/validation/html/html-validation-itineraries.png) | Pass: No Errors |
| Itinerary Delete Confirmation | ![screenshot](documentation/validation/html/html-validation-cancel_booking_confirmation.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. |
| Itinerary Details | ![screenshot](documentation/validation/html/html-validation-itinerary_detail.png) | Pass: No Errors |
| Login | ![screenshot](documentation/validation/html/html-validation-login.png) | Pass: No Errors |
| Delete Profile Confirmation | ![screenshot](documentation/validation/html/html-validation-profile_delete_confirmation.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. |
| Edit Profile | ![screenshot](documentation/validation/html/html-validation-edit_profile.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. |
| Profile | ![screenshot](documentation/validation/html/html-validation-profile.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. |
| Sign Up | ![screenshot](documentation/validation/html/html-validation-signup.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files. Which passed with no errors.

![screenshot](documentation/validation/css/css_validation.png)

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| modal-handler.js | ![screenshot](documentation//validation/js/js_validation.png) | Pass: No Errors - 1 'Undefined' message as bootstrap link is in the base.html file. |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Validation For Trip-Easy App
| File | Screenshot | Notes |
| --- | --- | --- |
| asgi.py | ![screenshot](documentation/validation/python/tripeasy/tripeasy_asgi.png) | Pass: No Errors |
| settings.py | ![screenshot](documentation/validation/python/tripeasy/tripeasy_settings.png) | Pass: No Errors |
| urls.py | ![screenshot](documentation/validation/python/tripeasy/tripeasy_urls.png) | Pass: No Errors |
| wsgi.py | ![screenshot](documentation/validation/python/tripeasy/tripeasy_wsgi.png) | Pass: No Errors |

#### Validation For Booking App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](documentation/validation/python/booking/booking_admin.png) | Pass: No Errors |
| apps.py | ![screenshot](documentation/validation/python/booking/booking_apps.png) | Pass: No Errors |
| forms.py | ![screenshot](documentation/validation/python/booking/booking_forms.png) | Pass: No Errors |
| models.py | ![screenshot](documentation/validation/python/booking/booking_models.png) | Pass: No Errors |
| urls.py | ![screenshot](documentation/validation/python/booking/booking_urls.png) | Pass: No Errors |
| views.py | ![screenshot](documentation/validation/python/booking/booking_views.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser_chrome.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser_firefox.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser_edge.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/mobile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/tablet.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/desktop.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

### Booking App Templates - Mobile Testing
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/lighthouse/mobile/light-home.png) | Some minor performance warnings |
| About | Mobile | ![screenshot](documentation/lighthouse/mobile/light-about.png) | Some minor performance warnings |
| Itineraries | Mobile | ![screenshot](documentation/lighthouse/mobile/light-itineraries.png) | Some minor performance warnings |
| Itinerary Detail | Mobile | ![screenshot](documentation/lighthouse/mobile/light-itinerary-detail.png) | Some minor performance warnings |
| Contact | Mobile | ![screenshot](documentation/lighthouse/mobile/light-contact.png) | Some minor performance warnings |
| Profile | Mobile | ![screenshot](documentation/lighthouse/mobile/light-profile.png) | Some minor performance warnings |
| Login | Mobile | ![screenshot](documentation/lighthouse/mobile/light-login.png) | Some minor performance warnings |
| Sign Up | Mobile | ![screenshot](documentation/lighthouse/mobile/light-signup.png) | Some minor performance warnings |
| 404 | Mobile | ![screenshot](documentation/lighthouse/mobile/light-404.png) | Some minor performance warnings |

### Booking App Templates - Desktop Testing
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot](documentation/lighthouse/desktop/light-desk-home.png) | Some minor performance warnings |
| About | Desktop | ![screenshot](documentation/lighthouse/desktop/light-desk-about.png) | Some minor performance warnings |
| Itineraries | Desktop | ![screenshot](documentation/lighthouse/desktop/light-desk-itineraries.png) | Some minor performance warnings) |
| Itinerary Detail | Desktop | ![screenshot](documentation/lighthouse/desktop/light-desk-itinerary-detail.png) | Some minor performance warnings |
| Contact | Desktop | ![screenshot](documentation/lighthouse/desktop/light-desk-contact.png) | Some minor performance warnings |
| Profile | Desktop | ![screenshot](documentation/lighthouse/desktop/light-desk-profile.png) | Some minor performance warnings |
| Login | Desktop | ![screenshot](documentation/lighthouse/desktop/light-desk-login.png) | Some minor performance warnings |
| Sign Up | Desktop | ![screenshot](documentation/lighthouse/desktop/light-desk-signup.png) | Some minor performance warnings |
| 404 | Desktop | ![screenshot](documentation/lighthouse/desktop/light-desk-404.png) | Some minor performance warnings |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Click on About link in navbar | Redirection to About page | Pass | |
| | Click on Itineraries link in navbar | Redirection to Itineraries page | Pass | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Click on Profile link in navbar | Redirection to Profile page | Pass | |
| | Click on Login link in navbar | Redirection to Login page | Pass | |
| | Click on Sign Up link in navbar | Redirection to Sign Up page | Pass | |
| | Click on Log Out link in navbar | Log out and Redirection to Home page | Pass | |
| | Click on Social links in Footer | Redirection to corresponding social page | Pass | |
| Home page | | | | |
| | Click on Explore Itineraries button on hero image | Redirection to Itineraries page | Pass | |
| | Click on Featured Itineraries View Details button | Redirection to that itinerary's details page | Pass | |
| Itineraries page | | | | |
| | Click on any itinerary's View Details button | Redirection to that itinerary's details page | Pass | |
| Itinerary Details Page | | | | |
| | Click on Book Now button | Redirect to booking confirmation page | Pass | |
| | Click on back button | Redirect to reservation list page | Pass | |
| | Click on back button | Redirect to reservation list page | Pass | |
| | Click on back button | Redirect to reservation list page | Pass | |
| | Click on back button | Redirect to reservation list page | Pass | |
| Booking Confirmation Page | | | | |
| | Click on Confirm Booking button | Redirect to Profile confirmation page | Pass | |
| | Click on Cancel button | Redirect to itinerary page | Pass | |
| Contact Page | | | | |
| |  Enter name | Redirect to Contact Form | Pass | |
| |  Enter valid email address | Redirect to Contact Form | Pass | |
| | Enter message | Redirect to Contact Form | Pass | |
| | Click on Submit button | Redirect to Contact page | Pass | |
| | Click on Google Map | Navigates as it should | Pass | |
| Login Page | | | | |
| | Enter valid Username | Field will only accept registered users | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click on Log In button | Redirects user to Home Page | Pass |
| | Click on Sign Up button | Redirects user to Sign Up Page | Pass |
| Sign Up Page | | | | |
| | Enter valid Username | Field will only accept username format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click Register button | Redirects user to home page | Pass | |
| Log Out Page | | | | |
| | Click Logout button | Logs out user, Redirects user to Home page | Pass |
| | Click Cancel button | Keeps user logged in, redirects to Home page | Pass |
| Profile Page | | | | |
| | Click on the Edit Profile button | Redirects to Edit Profile page | Pass | |
| | Click on the Delete Account button | Redirects to Delete Account Confirmation page | Pass | |
| | Click on the Cancel booking button | Redirects to Delete Booking Confirmation page | Pass | |
| Edit Profile Page | | | | |
| | Enter user details | Field will only accept email format | Pass | |
| | Click on the Save Changes button | Redirects to Profile page | Pass | |
| | Click on the Cancel button | Redirects to Profile page | Pass | |
| Delete Account Confirmation Page | | | | |
| | Click on the Delete My Account button | Deletes account and redirects to Home page | Pass | |
| | Click on the Cancel button | Redirects to Profile page without deleting account | Pass | |
| Delete Booking Confirmation Page | | | | |
| | Click on the Yes, Cancel button | Deletes booking and redirects to Profile page | Pass | |
| | Click on the No, Go Back button | Keeps booking and redirects to Profile page | Pass | |
| | Click on the Cancel booking button | Redirects to Delete Booking Confirmation page | Pass | |
| Site Navigations - Logged Out User | | | | |
| | Navigate to any login required URL | Give option to Login or Sign Up | Pass | |


## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a user I want to log into my account so that I can access my saved trips and profile settings. | ![screenshot](documentation/features/site-pages/profilewithbooking.png) |
|As a user I want to recover my account if I forget my password, so that I can regain access without creating a new account. | ![screenshot](documentation/features/site-pages/contactpage.png) |
| As a user I want to sign up for an account so that I can access the website's features. | ![screenshot](documentation/features/site-pages/signup.png) |
| As a user I want to log out of my account so that my session is securely ended. | ![screenshot](documentation/features/site-pages/logout.png) |
| As a user I want to book a trip from the itinerary page so that I can reserve my spot. | ![screenshot](documentation/features/site-pages/itin2.png) |
| As a user I want to update my account information so that I can keep my details accurate. | ![screenshot](documentation/features/site-pages/editprofile.png) |
| As an admin I want to create, update, or delete itineraries, so that I can keep the trip offerings up-to-date. | ![screenshot](documentation/features/site-pages/itinadmin.png) |
| As an admin I want to view and manage user bookings so that I can handle any issues or changes efficiently. | ![screenshot](documentation/features/site-pages/bookingadmin.png) |


## Bugs

- Navbar items wouldn't align on right.

    - To fix this, I had to remove css for header display:flex for them to align to the right.

- Raw html showing on homepage cards.

    ![screenshot](documentation/bugs/rawhtmlbug.png)

    - To fix this, I had to add 'safe' to base home.html

- Card buttons not staying at the bottom.

    ![screenshot](documentation/bugs/buttonsbug.png)

    - To fix this, I wrapped the card contents in a separate div and added css to the button : margin-top: auto;

- Logo not showing.

    ![screenshot](documentation/bugs/logobug.png)

    - To fix this, I had to resize the logo image as the file size was too large.

- Footer not staying fixed to the bottom of the page on soame pages.

    ![screenshot](documentation/bugs/footerbug.png)

    - To fix this I had to set the .homepage height to 100vh.

- Extra zeros being displayed on prices.

    - To fix this, I had to add a float format so new code is: <p><strong>Price:</strong> £{{ itinerary.price|floatformat:"0" }}pp</p> anywhere there was a price.

- Too many itineraries showing in the features section.

    - To fix this, I had to add 'slice' to {% for itinerary in itineraries|slice:":6" %} in the home.html file so that it will now only display 6.

## Unfixed Bugs

There are no remaining bugs that I am aware of.