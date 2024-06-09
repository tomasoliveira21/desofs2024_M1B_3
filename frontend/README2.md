# Frontend

## Table of Contents

## Frontend Goal

Our goal for the frontend of SocialNet is to create a highly interactive and visually appealing social networking platform inspired by Twitter. Utilizing the latest technologies such as Next.js, Tailwind CSS, Supabase, and React, we aim to deliver a seamless user experience with real-time interactions and responsive design. Our focus is on crafting an intuitive interface that encourages user engagement and fosters a vibrant online community. By leveraging the strengths of these modern tools, we strive to build a frontend that is not only functional but also scalable and maintainable, ensuring a robust and dynamic social networking experience.

## Supabase initialization

The supabase.ts file initializes and configures the Supabase client for our Next.js project. It imports the createClientComponentClient function from the @supabase/auth-helpers-nextjs package and exports an instance of the Supabase client, enabling seamless integration and interaction with Supabase services, such as authentication and database operations, within our Next.js components.

## Frontend Middleware

It was also created a [middleware](../../../frontend/src/middleware.ts) to manage user authentication using Supabase. The middleware checks if a user is logged in before allowing access to most pages. Certain URLs, like `/reset`, are publicly accessible without authentication. If the user is not authenticated and tries to access a protected page, they are redirected to the login page. This ensures that only authenticated users can access specific parts of the application.

## API Calls

The API calls in our frontend are organized in the `frontend/src/api` directory. These functions handle various operations related to tweets, user profiles, and trends, interacting with the backend services to fetch and post data as required.

### Fetching Tweets

The `fetchTweets.ts` file contains the function to retrieve the latest tweets from the backend. This function interacts with the database to provide real-time updates and display the most recent tweets on the user's feed.

### Fetching Tweets by User

The `fetchTweetsByUser.ts` file provides the functionality to fetch tweets posted by a specific user. This is used to display a user's tweet history on their profile page.

### Posting a Tweet

The `postTweet.ts` file includes the function to post a new tweet. This handles the creation of a tweet, ensuring it is stored in the database and immediately reflected in the user's feed.

### Deleting a Tweet

The `deleteTweet.ts` file contains the function to delete an existing tweet. This allows users to remove their tweets from the platform, with updates reflected in real-time.

### Fetching User Information

The `fetchUser.ts` file includes the function to retrieve detailed information about a specific user. This is used to populate user profiles with relevant data.

### Fetching Multiple Users

The `fetchUsers.ts` file provides the functionality to fetch a list of users. This can be used for features such as user search or displaying followers/following lists.

### Fetching Profile Picture

The `fetchProfilePicture.ts` file contains the function to fetch a user's profile picture. This ensures profile pictures are dynamically loaded and updated as needed.

### Posting Profile Picture

The `postProfilePicture.ts` file includes the function to upload and update a user's profile picture. This allows users to customize their profiles with a personal image.

### Fetching Trends

The `fetchTrends.ts` file provides the functionality to fetch the latest trending topics. This is used to display current popular topics and hashtags on the platform.


## Views

The views in our frontend application represent the different pages and visual layouts that users interact with. Each view is designed to provide a seamless and intuitive user experience, ensuring that navigation and interaction are straightforward and engaging. Utilizing Next.js and React, we structure our views to be dynamic and responsive, catering to various user actions and data flows. Below is a breakdown of the key views implemented in the SocialNet frontend, detailing their functionalities and the components they encompass.


### Login View

The Login view is responsible for handling user authentication in the SocialNet platform. This view provides a simple and intuitive interface for users to log in to their accounts or reset their passwords if needed. The functionality is powered by Supabase for authentication and leverages Next.js and React for seamless navigation and state management.

#### Key Features:

- **Email and Password Login**: Users can enter their email and password to log in to their accounts. The credentials are validated using Supabase's `signInWithPassword` method.
- **Password Reset**: Users who have forgotten their password can initiate a password reset process. By toggling the "Forgot Password?" link, the view switches to a password reset interface where users can request a reset email.
- **Error Handling**: The view provides feedback for various authentication states, including successful login, failed login attempts, and errors during the password reset process.
- **Responsive Design**: The layout is designed to be responsive, ensuring a consistent user experience across different devices.

#### Code Overview:

- **State Management**: The component uses React's `useState` hook to manage form data, reset password toggle, and messages.
- **Form Handling**: Input fields for email and password are dynamically controlled, updating the component's state on change.
- **Authentication Functions**:
  - `login`: This async function attempts to log in the user with the provided email and password. On success, it redirects the user to the home page. On failure, it displays an error message.
  - `sendResetPassword`: This async function sends a password reset email to the user. It handles potential errors and provides appropriate feedback.
- **Navigation**: Uses Next.js `useRouter` hook for client-side navigation post-login.


### Reset Password View

The Reset Password view allows users to update their password if they have forgotten it or need to change it for security reasons. This view is designed to be straightforward and secure, guiding users through the process of setting a new password.

#### Key Features:

- **Password Input**: Users can enter a new password and confirm it to ensure both fields match. This helps to prevent errors during password entry.
- **Password Visibility Toggle**: A feature that allows users to toggle the visibility of their password inputs, making it easier to verify what they have typed.
- **Validation and Update**: The view includes validation to ensure that the new password and the confirm password fields match. It uses Supabase's `updateUser` method to securely update the user's password.
- **Error Handling**: If there are any issues during the password update process, appropriate error messages are displayed to inform the user.

#### How It Works:

- **State Management**: The component uses React's `useState` hook to manage the password and confirm password inputs, as well as to toggle the password visibility.
- **Form Handling**: Input fields for the new password and confirm password are dynamically controlled, updating the component's state on change.
- **Password Confirmation**:
  - Before updating the password, the function checks if the password and confirm password fields match. If they do not, an alert is shown.
  - If the passwords match, Supabase's `updateUser` method is called to update the password. Upon success, the user is redirected to the home page.

#### User Flow:

1. The user navigates to the Reset Password view.
2. They enter their new password and confirm it.
3. They can toggle the visibility of the password fields to ensure accuracy.
4. Upon submitting, the passwords are validated to ensure they match.
5. If the validation passes, the password is updated using Supabase.
6. The user is redirected to the home page upon successful password update.

This view ensures that users can easily and securely reset their passwords, maintaining the overall security and usability of the SocialNet platform.

### Homepage View

The Homepage view serves as the central hub of the SocialNet platform, providing users with access to the main functionalities such as viewing the feed, interacting with widgets, and navigating via the sidebar. This view is designed to be dynamic and responsive, ensuring a smooth and engaging user experience.

#### Key Features:

- **Session Management**: The view manages user sessions, ensuring that only authenticated users can access the homepage. It retrieves the current session using Supabase's `getSession` method and updates the component state accordingly.
- **Loading State**: A loading indicator is displayed while the user session is being verified, enhancing the user experience during authentication.
- **Sidebar Navigation**: The sidebar component provides easy navigation to various sections of the platform, including user profile, settings, and other essential links.
- **Feed**: The feed component displays the latest posts and updates from other users, allowing for real-time interaction and engagement.
- **Widgets**: The widgets component includes additional interactive elements, such as trending topics and suggestions, enriching the user's experience on the platform.
- **Toaster Notifications**: The view integrates `react-hot-toast` and `react-toastify` for providing real-time notifications and feedback to the user.

#### How It Works:

- **Session Handling**: The component uses React's `useState` and `useEffect` hooks to manage and retrieve the user session from Supabase.
- **Components Integration**: 
  - **Sidebar**: Renders the sidebar with the current session data, ensuring that user-specific information is displayed.
  - **Feed**: Displays the main content feed, utilizing the session data to fetch and render posts relevant to the user.
  - **Widgets**: Adds supplementary interactive elements to the homepage, enhancing user engagement.
- **Notifications**: `Toaster` and `ToastContainer` are used to display various notifications and alerts to the user, providing immediate feedback and enhancing the overall user experience.

#### User Flow:

1. The user navigates to the Homepage view.
2. The component checks for an existing user session.
3. If a session is found, the homepage components (Sidebar, Feed, Widgets) are rendered.
4. If no session is found, a loading indicator is displayed until the session is verified.
5. Users can navigate through the sidebar, interact with the feed, and engage with widgets.
6. Real-time notifications and feedback are provided via toast messages.

This view ensures that authenticated users have a seamless and interactive experience on the SocialNet platform, providing them with all the necessary tools and information to stay engaged and connected.

### Profile View

The Profile view is designed to provide users with a comprehensive overview of their personal information, including their tweets and profile picture. This view allows users to manage and update their profile details, ensuring a personalized and engaging experience on the SocialNet platform.

#### Key Features:

- **User Session Management**: The view verifies the user's session, ensuring only authenticated users can access and modify their profile information.
- **Profile Information Display**: Displays user information such as username and email, fetched from the backend using Supabase.
- **Tweets by User**: Retrieves and displays the tweets posted by the user, providing a personalized feed on their profile page.
- **Profile Picture Management**: Allows users to upload and change their profile picture. The selected image is displayed and updated in real-time.
- **Loading States**: Displays loading indicators while fetching user data and tweets to ensure a smooth user experience.

#### How It Works:

- **Session Handling**: The component uses React's `useState` and `useEffect` hooks to manage and retrieve the user session from Supabase.
- **Fetching Data**:
  - **User Data**: Fetches detailed user information such as username and email using the `fetchUser` function.
  - **Tweets**: Retrieves the user's tweets using the `fetchTweetsByUser` function.
  - **Profile Picture**: Fetches and updates the user's profile picture using the `fetchProfilePicture` and `postProfilePicture` functions.
- **Image Upload**: Handles profile picture changes by allowing users to select a new image, which is then uploaded and displayed on their profile.
- **Components Integration**:
  - **Sidebar**: Provides navigation options and displays user-specific information.
  - **UserInfo**: Displays user details and manages profile picture updates.
  - **TweetComponent**: Renders each tweet posted by the user, integrating user data and profile picture for a cohesive display.

#### User Flow:

1. The user navigates to the Profile view.
2. The component checks for an existing user session.
3. If a session is found, user data, tweets, and profile picture are fetched and displayed.
4. The user can view their profile information and tweets.
5. The user can update their profile picture by selecting a new image, which is uploaded and displayed immediately.
6. All changes and updates are managed seamlessly, providing a dynamic and personalized profile page.

This view ensures that users have full control over their profile, allowing them to manage their personal information and view their activity on the SocialNet platform.

### Trends View (Premium/Admin Users - only)

The Trends view provides users with a comprehensive overview of the latest trending topics on the SocialNet platform. This view is designed to display trends dynamically, allowing users to stay updated with popular discussions and hashtags in real-time.

#### Key Features:

- **User Session Management**: The view ensures that only authenticated users can access the trends information by verifying the user session.
- **Fetching Trends**: Retrieves the latest trends from the backend using the `fetchTrends` function and displays them in a structured format.
- **Sidebar Navigation**: Integrates the sidebar component for easy navigation across different sections of the platform.
- **Trends Display**: Utilizes the `TrendTable` component to present the trending topics in a clean and organized manner.
- **Loading State**: Displays a loading indicator while the user session and trends data are being fetched, ensuring a smooth user experience.

#### How It Works:

- **Session Handling**: The component uses React's `useState` and `useEffect` hooks to manage and retrieve the user session from Supabase.
- **Fetching Data**:
  - **Trends Data**: Fetches the latest trends using the `fetchTrends` function once the user session is verified.
- **Components Integration**:
  - **Sidebar**: Provides navigation options and displays user-specific information.
  - **TrendTable**: Renders the trends in a tabular format, making it easy for users to see what topics are currently popular.

#### User Flow:

1. The user navigates to the Trends view.
2. The component checks for an existing user session.
3. If a session is found, the latest trends are fetched and displayed.
4. The user can view the trending topics in a tabular format.
5. The sidebar provides additional navigation options for the user.

This view ensures that users can easily access and stay updated with the latest trending topics on the SocialNet platform, enhancing their engagement with current discussions and popular content.

### Admin View (Admin Users - only)

The Admin view is designed for administrators of the SocialNet platform to manage and monitor posts and trends. This view provides robust tools to handle administrative tasks, ensuring smooth operation and moderation of the platform's content.

#### Key Features:

- **User Session Management**: The view ensures that only authenticated administrators can access the administrative functionalities by verifying the user session.
- **Fetching Trends**: Retrieves the latest trends using the `fetchTrends` function, allowing administrators to monitor current popular topics.
- **Fetching Tweets**: Fetches all tweets from the platform using the `fetchTweets` function, enabling administrators to review and manage user-generated content.
- **Sidebar Navigation**: Integrates the sidebar component for easy navigation to different sections of the platform.
- **Real-time Notifications**: Utilizes `react-hot-toast` and `react-toastify` for providing real-time notifications and feedback to administrators.
- **Refresh Functionality**: Includes a refresh button to update the list of tweets, ensuring administrators are viewing the most recent content.

#### How It Works:

- **Session Handling**: The component uses React's `useState` and `useEffect` hooks to manage and retrieve the user session from Supabase.
- **Fetching Data**:
  - **Trends Data**: Fetches the latest trends using the `fetchTrends` function once the user session is verified.
  - **Tweets Data**: Retrieves all tweets using the `fetchTweets` function, providing administrators with a comprehensive view of user activity.
- **Components Integration**:
  - **Sidebar**: Provides navigation options and displays user-specific information.
  - **TrendTable**: Renders the trends in a tabular format, making it easy for administrators to see current popular topics.
  - **TweetComponent**: Displays each tweet with administrative controls for managing content.
- **Refresh Mechanism**: Implements a refresh button that reloads the tweets, ensuring the display of up-to-date content.

#### User Flow:

1. The administrator navigates to the Admin view.
2. The component checks for an existing user session.
3. If a session is found, trends and tweets are fetched and displayed.
4. The administrator can view and manage trends and tweets.
5. The sidebar provides additional navigation options for the administrator.
6. The refresh button allows the administrator to update the list of tweets in real-time.
7. Real-time notifications are provided for actions performed by the administrator, enhancing the overall user experience.

This view ensures that administrators have the necessary tools and information to effectively manage and monitor the SocialNet platform, maintaining a high standard of content and user engagement.

## Components

## Error Handling

