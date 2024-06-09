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

The `components` directory in the `frontend` folder houses all the reusable components used throughout the SocialNet platform. These components are designed to be modular and reusable, promoting consistency and efficiency in the development process. We have adopted the Atomic Design system to structure our components, ensuring a clear hierarchy and reusability. Each component serves a specific purpose, contributing to the overall functionality and user experience of the application.

### Feed Component
The `Feed` component is a central part of the SocialNet platform, responsible for displaying the main feed of tweets and updates from users that the authenticated user follows. This component integrates several functionalities to provide a dynamic and engaging user experience.

#### Key Features:

- **Session Integration**: The `Feed` component takes a `session` prop, which contains the user's session information. This is used to fetch and display user-specific data.
- **Fetching Tweets**: Utilizes the `fetchTweets` function to retrieve the latest tweets from users the authenticated user follows. The tweets are fetched initially when the component mounts and can be refreshed manually.
- **Profile Picture**: Fetches the profile picture of the authenticated user using the `fetchProfilePicture` function to display it in the tweet box.
- **Tweetbox Integration**: Includes the `Tweetbox` component, allowing users to post new tweets directly from the feed.
- **Real-time Updates**: Provides a refresh button to manually update the feed, ensuring users see the most recent tweets. Toast notifications are used to give feedback during the refresh process.
- **Responsive Design**: Ensures that the feed is displayed correctly across different screen sizes and devices.

#### How It Works:

- **State Management**: Uses React's `useState` hook to manage the state of tweets and the user's profile picture.
- **Effect Hooks**: 
  - `useEffect` to fetch tweets when the component mounts or when the session changes.
  - `useEffect` to fetch the user's profile picture when the session changes.
- **Refresh Functionality**: The `handleRefresh` function is triggered when the refresh button is clicked. It fetches the latest tweets and updates the state, displaying a loading toast notification during the process.

### Sidebar Component

The `Sidebar` component serves as the main navigation hub for the SocialNet platform, providing users with easy access to various sections of the application. It dynamically displays different navigation options based on the user's role and authentication status, enhancing the overall user experience and ensuring efficient navigation.

#### Key Features:

- **Dynamic Navigation**: Displays different navigation options based on the user's role (e.g., admin, premium, regular user). This ensures that users see only the options relevant to them.
- **Session Integration**: The `Sidebar` component takes a `session` prop, which contains the user's session information. This is used to fetch and display user-specific data.
- **User Data Fetching**: Utilizes the `fetchUser` function to retrieve detailed user information, which is then used to customize the sidebar options.
- **Navigation Options**:
  - **Home**: Takes the user to the homepage.
  - **Trends**: Available for premium and admin users, takes the user to the trends page.
  - **Profile**: Takes the user to their profile page.
  - **Notifications**: Placeholder for future notifications functionality.
  - **Messages**: Placeholder for future messaging functionality.
  - **Manage**: Available only for admin users, takes the user to the admin management page.
  - **Sign Out**: Logs the user out and refreshes the session.

#### How It Works:

- **State Management**: Uses React's `useState` hook to manage the state of user data.
- **Effect Hooks**: 
  - `useEffect` to fetch user data when the component mounts or when the session changes.
- **Navigation Functions**:
  - **goToHome**: Navigates to the homepage.
  - **goToExplore**: Navigates to the trends page.
  - **goToProfile**: Navigates to the user's profile page.
  - **goToAdmin**: Navigates to the admin management page.
  - **logout**: Logs the user out and refreshes the session.

#### User Flow:

1. The user logs into the SocialNet platform.
2. The `Sidebar` component is rendered, displaying navigation options based on the user's role and session information.
3. The user can click on various navigation options to move between different sections of the platform.
4. If the user is an admin, they have additional options like managing the platform.
5. The user can log out by clicking the "Sign Out" option, which will end their session and refresh the page.

This component ensures that users have a seamless and intuitive navigation experience, making it easy to access different parts of the SocialNet platform based on their roles and permissions.

### SidebarRow Component

The `SidebarRow` component is a reusable component used within the `Sidebar` to render individual navigation options. It is designed to be modular and interactive, enhancing the navigation experience for users by providing a consistent look and feel across different navigation items.

#### Key Features:

- **Icon and Title Display**: Each `SidebarRow` displays an icon and a title, making it easy for users to identify different navigation options at a glance.
- **Click Handling**: Supports an optional `onClick` handler, allowing for custom actions when a user clicks on the navigation item.
- **Responsive Design**: Adapts to different screen sizes, with the title being hidden on smaller screens to save space and only showing the icon.
- **Interactive Styling**: Changes appearance on hover, providing visual feedback to the user and enhancing the interactive experience.

#### How It Works:

- **Props**: 
  - `Icon`: A React component that renders an SVG icon.
  - `Title`: A string that represents the title of the navigation item.
  - `onClick`: An optional function that is executed when the `SidebarRow` is clicked.
- **Styling**: 
  - The component uses Tailwind CSS classes to style the icon and title, ensuring a consistent and modern appearance.
  - It includes hover effects that change the background color and text color, providing interactive feedback.
- **Responsive Behavior**:
  - The title text is hidden on smaller screens (`hidden md:inline-flex`) to maintain a clean layout.
  - The component expands to fit the content (`max-w-fit`) and uses padding for spacing (`px-4 py-3`).

#### Code Overview:

The `SidebarRow` component is defined as a functional component in React. It takes in three props: `Icon`, `title`, and `onClick`. The component returns a `div` that contains the icon and the title, with styling and hover effects applied.

#### Usage:

The `SidebarRow` component is used within the `Sidebar` to render each navigation item. It allows for easy addition of new navigation options with consistent styling and behavior.

### TrendTable Component

The `TrendTable` component is designed to display a list of trending topics in a tabular format. It provides a clear and organized view of trends, including their position, name, and count, making it easy for users to see what is currently popular on the SocialNet platform.

#### Key Features:

- **Tabular Display**: Presents trending topics in a table format, with columns for position, name, and count. This structured layout makes it easy for users to scan and understand the trends at a glance.
- **Responsive Design**: The component includes responsive styling to ensure that the table displays correctly on different screen sizes and devices.
- **Hover Effects**: Rows change appearance on hover, providing visual feedback to the user and enhancing the interactive experience.
- **Dynamic Data Handling**: The component takes an array of trends as a prop and dynamically renders each trend as a row in the table.

#### How It Works:

- **Props**: 
  - `trends`: An array of trend objects, each containing `position`, `name`, and `count` properties.
- **Rendering Logic**:
  - The table only renders the header if there are trends to display. This ensures that the component remains clean and doesn't display unnecessary headers when there are no trends.
  - Each trend is mapped to a row in the table, displaying its position, name, and count in respective columns.
- **Styling**: 
  - Utilizes Tailwind CSS classes to style the table and its elements, ensuring a modern and clean appearance.
  - Includes hover effects to change the background color of rows when the user hovers over them, providing interactive feedback.

#### Usage:

The `TrendTable` component is used to display trending topics within the SocialNet platform. It can be included in any view where trends need to be displayed, such as the Trends view or the homepage.

### Tweet Component

The `Tweet` component is a core part of the SocialNet platform, responsible for rendering individual tweets. It displays the content of a tweet along with user information, timestamps, and interactive icons for user engagement. This component ensures that tweets are presented in a visually appealing and functional manner.

#### Key Features:

- **User Information**: Displays the username and profile picture of the user who posted the tweet. If the user information is not available, it falls back to displaying the user UUID.
- **Timestamp**: Utilizes the `TimeAgo` component to display the time elapsed since the tweet was posted, providing a relative timestamp.
- **Interactive Icons**: Includes icons for comments, retweets, likes, and sharing, allowing users to interact with the tweet. The icons are styled for a clean and modern look.
- **Admin Controls**: For admin users, a delete icon is displayed, allowing them to remove inappropriate or unwanted tweets. This enhances the moderation capabilities of the platform.
- **Image Support**: If a tweet contains an image, it is displayed below the tweet content, enhancing the visual appeal of the tweet.
- **Responsive Design**: The component is styled to be responsive, ensuring it looks good on various screen sizes and devices.

#### How It Works:

- **Props**: 
  - `tweet`: The tweet object containing all the necessary information (content, timestamp, user details, etc.).
  - `isAdmin`: A boolean indicating whether the current user is an admin.
  - `userInfo`: Information about the user who posted the tweet.
  - `session`: The current user session, used for authentication and actions like deleting a tweet.
  - `profilePicture`: The URL of the user's profile picture.
- **Delete Functionality**: 
  - `handleDelete`: An asynchronous function that calls the `deleteTweet` API to remove a tweet when the delete icon is clicked. This function is only available to admin users.
- **Styling**: 
  - The component uses Tailwind CSS classes for styling, ensuring a modern and consistent look.
  - Hover effects and cursor pointers are used to enhance the interactive elements.

#### User Flow:

1. The `Tweet` component receives the necessary props and renders the tweet content.
2. The user's profile picture and username are displayed alongside the tweet content.
3. A timestamp shows how long ago the tweet was posted.
4. Interactive icons for commenting, retweeting, liking, and sharing are displayed below the tweet content.
5. Admin users see an additional delete icon to remove tweets.
6. If the tweet contains an image, it is displayed below the text content.
7. Users can interact with the tweet using the provided icons.

This component ensures that tweets are displayed in a comprehensive and interactive manner, enhancing the user experience on the SocialNet platform.

### TweetBox Component

The `TweetBox` component allows users to create and post new tweets on the SocialNet platform. It provides a user-friendly interface for composing tweets, complete with options to add media and other content types. This component is essential for user interaction and content creation within the platform.

#### Key Features:

- **User Profile Picture**: Displays the user's profile picture alongside the tweet input box, providing a personalized touch to the tweeting experience.
- **Input Field**: A text input field where users can type their tweet content. The input is cleared after a tweet is successfully posted.
- **Media and Content Icons**: Includes icons for adding photos, searching, adding emojis, scheduling tweets, and adding locations, enhancing the functionality of the tweet creation process.
- **Submit Button**: A button to post the tweet. The button is disabled if the input field is empty, preventing empty tweets from being posted.
- **Responsive Design**: The component is designed to be responsive, ensuring a smooth user experience across different devices and screen sizes.

#### How It Works:

- **Props**: 
  - `session`: The user's session information, used for authentication when posting a tweet.
  - `profilePicture`: The URL of the user's profile picture, displayed next to the input field.
- **State Management**: Uses React's `useState` hook to manage the state of the tweet input field.
- **Form Submission**:
  - `handleSubmit`: An event handler that prevents the default form submission behavior, calls the `postTweet` function with the tweet content and session token, and then clears the input field.
- **Styling**: 
  - Utilizes Tailwind CSS classes for styling the input field, buttons, and icons, ensuring a modern and consistent appearance.
  - Includes hover effects and transition animations to enhance the interactive elements.

#### User Flow:

1. The user navigates to the TweetBox component.
2. The user's profile picture is displayed next to the input field.
3. The user types their tweet content into the input field.
4. The user can optionally click on icons to add photos, emojis, locations, etc.
5. The user clicks the "Tweet" button to post their tweet.
6. The `handleSubmit` function is triggered, posting the tweet to the backend and clearing the input field.

### UserInfo Component

The `UserInfo` component displays user-specific information such as the profile picture, username, and email. It also allows users to update their profile picture, providing a personalized and interactive experience on the SocialNet platform.

#### Key Features:

- **Profile Picture Display and Update**: Shows the user's profile picture with an option to update it. The update button is conveniently placed over the image, making it easy for users to change their profile picture.
- **User Information Display**: Displays the username and email of the user in a clean and readable format.
- **Interactive Elements**: Includes hover and transition effects to enhance the user experience when interacting with the profile picture update button.

#### How It Works:

- **Props**: 
  - `selectedImage`: The URL of the user's current profile picture.
  - `handleImageChange`: A function to handle the event when a user selects a new profile picture.
  - `userName`: The username of the user.
  - `email`: The email address of the user.
- **Image Update Functionality**: 
  - The profile picture can be updated by clicking the edit icon over the image, which triggers the file input to select a new image.
  - The `handleImageChange` function is called when a new image is selected, allowing the parent component to handle the update logic.
- **Styling**: 
  - Uses Tailwind CSS classes to style the component, ensuring a modern and consistent look.
  - Includes hover and transition effects on the profile picture and edit icon to provide visual feedback and enhance interactivity.

#### User Flow:

1. The `UserInfo` component is rendered with the user's profile picture, username, and email.
2. The user sees their profile picture with an edit icon overlay.
3. The user can click the edit icon to select a new profile picture.
4. The `handleImageChange` function is triggered when a new image is selected, allowing the parent component to update the profile picture.
5. The username and email are displayed below the profile picture, providing a clear overview of the user's information.

### Widgets Component

The `Widgets` component is designed to enhance user engagement on the SocialNet platform by providing additional interactive elements and features. This component currently includes a search box for users to search content on the platform.

#### Key Features:

- **Search Box**: Provides a search input field where users can type queries to search for content on SocialNet. The search box includes a search icon and is styled to blend seamlessly with the platform's design.
- **Responsive Design**: The `Widgets` component is designed to be responsive, only displaying on larger screens (hidden on smaller screens). This ensures a clean and uncluttered interface on mobile devices while providing additional functionality on desktop.

#### How It Works:

- **Search Box**: 
  - Includes a search icon and an input field. The icon is styled with Tailwind CSS classes to match the platform's design.
  - The input field is styled to be transparent and outline-free, providing a clean look.
- **Styling**: 
  - Uses Tailwind CSS classes for styling, ensuring a modern and consistent appearance.
  - The component is wrapped in a div that is hidden on smaller screens (`hidden lg:inline`) to maintain a clean interface on mobile devices.

#### User Flow:

1. The `Widgets` component is rendered on larger screens (e.g., desktops and tablets).
2. The user sees a search box with a search icon.
3. The user can type queries into the search box to search for content on SocialNet.

## Error Handling
Effective error handling is crucial for providing a smooth and user-friendly experience on the SocialNet platform. We have implemented error handling mechanisms throughout the frontend application to ensure that users are informed of any issues promptly and clearly. 

### Key Features:

- **React-Toastify Integration**: We utilize the `react-toastify` library to display error and success toasts. This library provides an easy and flexible way to show notifications to users, enhancing the overall user experience.
- **Consistent Error Messaging**: All error messages are displayed in a consistent format, ensuring that users can easily recognize and understand the notifications.
- **Success Notifications**: In addition to error messages, success notifications are also shown using toasts to inform users of successful actions, such as posting a tweet or updating profile information.

### How It Works:

- **Error Handling in API Calls**: All API calls are wrapped in try-catch blocks to catch any errors that occur during data fetching or posting. When an error is caught, an error toast is displayed to the user.
- **Success Handling**: Similarly, when an action is successfully completed, such as a successful API call, a success toast is displayed to inform the user.
- **Toast Configuration**: The `react-toastify` library is configured to display toasts at the bottom-right corner of the screen, with options for auto-close and draggable interactions to enhance user experience.
