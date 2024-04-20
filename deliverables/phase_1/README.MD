# Phase 1

**Application:** SocialNet

**Description:** a social network similiar to X (formerly Twitter).

- [Phase 1](#phase-1)
  - [Design](#design)
    - [Application Requirements](#application-requirements)
    - [Domain Model](#domain-model)
    - [Use Cases](#use-cases)
      - [User and Premium User](#user-and-premium-user)
      - [Tweet Interaction](#tweet-interaction)
      - [Banned Users](#banned-users)
  - [Implementation](#implementation)
  - [Technological Decisions](#technological-decisions)
    - [Tech-Stack](#tech-stack)
    - [Infrastructure - High-Level System Architecture Diagram](#infrastructure---high-level-system-architecture-diagram)
  - [Security Analysis](#security-analysis)
    - [Security Requirements](#security-requirements)
    - [Threat Model](#threat-model)
    - [ASVS Checklist](#asvs-checklist)
  - [Test Plan](#test-plan)


## Design

### Application Requirements

1. A Frontend
2. A Backend
3. A Database
4. An Authentication System (with at least 3 roles)
5. At least 3 aggregates in the domain model
6. Follow the Secure Systems Development Lifecycle (SSDLC) process

Here are the mockups for the frontend application:

![Home Page](img/home_page.png)

![Profile Page](img/profile_page.png)

### Domain Model

We are using PlantUML to design our Domain Model, with the first iteration being the following:

![SocialNet Domain Model](img/domain_model.svg)

We have the following agregates with the following entities:

- Authentication: `Users`, `Roles` and `User-Related Information`
- Tweets: `Tweets` and Tweet `Replies`
- Hashtags: `Hashtags` and `Hashtag Statistics`

The entity `MediaAttachment` is reusable by the various aggregates.

### Use Cases

#### User and Premium User

![User Use Cases](img/uc/basic_user_uc.svg)

The use case diagram provided illustrates the various interactions that a `Basic User` can have within a social media platform, presumably similar to Twitter. At the center of the diagram is the `User` represented by a stick figure icon connected to several actions via lines, indicating different functions or activities that the user can perform on the platform:

1. `Search for Posts`: Indicates the user's ability to search for and find posts published by other users on the platform.
2. `Edit Profile`: The user can modify the information in their personal profile.
3. `Follow Other Users`: This action allows the user to follow other users, which likely means they will see those users' updates in their news feed.
4. `Retweet Posts`: The user can share posts from other users with their own followers, a feature known as retweeting.
5. `Like Posts`: The user can express their enjoyment of a post by clicking a like button.
6. `Comment on Posts`: The user can add comments to posts, allowing for direct interaction with the published content.
7. `Post Tweets`: The user can create and publish their own posts.

![Premium User Use Cases](img/uc/premium_user_uc.svg)

The use case diagram illustrates the extended functionalities available to a `Premium User` within the SocialNet platform. Employing the principle of inheritance, the `Premium User` retains all the capabilities of a `Basic User, with the addition of an exclusive feature:

1. `Access Trends`: Unique to the Premium User, this feature provides access to the platform's trending topics and popular content, offering insights into what is currently engaging the community.

![Administrator User Use Cases](img/uc/admin_user_uc.svg)

The use case diagram presented delineates the specific capabilities afforded to an `Admin User` on the SocialNet. Building upon the concept of inheritance, it is clear that the `Admin User` inherits the full spectrum of functionalities of a `Premium User`, with the augmentation of several key administrative powers that are critical for platform management and moderation.

The exclusive administrative features include:

1. `Delete Tweets`: The Admin User has the authority to remove tweets from the platform that may be in violation of the platform's policies or for other administrative reasons.
2. `Ban Users`: This important capability allows the Admin User to restrict access to the platform for users who have breached the terms of service or engaged in prohibited activities.
3. `Access Control Panel`: The Admin User has privileged access to the platform's control panel, which enables them to oversee the platform's operations, modify settings, and perform a wide range of administrative tasks.

Abuse cases identified:
 
1. Posting a tweet that is longer than allowed
2. Trying to upload attachments that are bigger than allowed
3. Tring to like too many posts in a given period of time
4. Trying to follow too many users in a given period of time
5. Commenting on a post with more caracters than allowed
6. Performing searchs with SQL instructions or system paths
7. Posting Hashtags with SQL instructions or system paths

#### Tweet Interaction

![Tweet Interaction Use Cases](img/uc/tweet_interaction_uc.svg)

Abuse cases identified:

1. Posting too many tweets in a given period of time

#### Banned Users

![Ban Use Case](img/uc/ban_status.svg)

Abuse cases identified:

1. Accessing the website too many times in a given period of time

## Implementation

![Deployment Diagram](img/deployment.svg)

![Data Flow Diagram](img/dfd.svg)

Port description:

- `HTTPS`: port `443`
- `SQL`: port `5432` (Postgres)

## Technological Decisions

### Tech-Stack

- [Docker](https://docker.com) as the containerization and deployment technology
- [Python3 (3.12)](https://www.python.org/downloads/release/python-3120/) for the Backend
- [ReactJS](https://react.dev/) for the Frontend
- [Supabase](https://supabase.com/docs) (with the [Python Client](https://supabase.com/docs/reference/python/start)) for Authentication and Authorization
- [Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) to expose the application (custom domain to be defined)
- [Postgres](https://www.postgresql.org/) as the database engine

### Infrastructure - High-Level System Architecture Diagram

![Infrastructure](img/infrastructure.svg)

## Security Analysis

### Security Requirements

- Authentication
  - Multi-Factor Authentication: email or OTP codes using an authenticator
  - Least privilege: users will not be authorized to perform any actions they are not supposed
  - Addition Principle: roles will have incremental permissions
- HTTPS between users and frontend
- HTTPS between containers whenever possible (might not be possible due to endpoints not being exposed)
- Hashed and Salted passwords (provided by supabase)
- Private network within Docker: no exposed ports

Data that we consider sensitive within our domain model:

- User passwords
- User emails

### Threat Model

This is the Risk Matrix used to classify the threats:

![Risk Matrix](img/risk_matrix.svg)

We have modeled our domain and infrastructure on Threat Dragon and the Model is present at the folder [`threat-dragon`](threat-dragon).

The approach we took: analyze the [Data Flow Diagram](#implementation) and apply the [STRIDE model](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats#stride-model) to each component, trying to identify the threats and elaborate mitigations. After the classification according to the matrix we analyze if the threat is already mitigated by design choices or if further intervention is needed (in the coming phases).

The full report, with the security analysis for each infrastructure component, as well as the security analysis for the relationships between our domain entities is present at [`threat-analysis.pdf`](threat-dragon/threat-analysis.pdf).

### ASVS Checklist

Here are the results for the ASVS Checklist for this iteration.

![ASVS Results](asvs/results)

Please note that this is an ongoing process and certain entries marked as `Not Applicable` will be handled in Phase 2.

Full checklist available at [`asvs`](asvs)

## Test Plan

In this section we will be describing all tests that we define as needed to test the mitigations that are identified during the [threat modeling process](#threat-model).