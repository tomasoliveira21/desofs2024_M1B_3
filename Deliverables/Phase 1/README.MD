# Phase 1

## Use Cases diagrams

![Basic User](https://cdn.discordapp.com/attachments/1211743636325408809/1228063062884352000/Basic.drawio.png?ex=662aadda&is=661838da&hm=0b31c59d94d2936f784db863c4445cb59352830dabf6572e6c40cb718289eeea&)

```
@startuml
left to right direction
rectangle "Project: SocialNet" {
actor "User" as User
boundary "SocialNet System" as System

User --> System : Post Tweets
User --> System : Comment on Posts
User --> System : Like Posts
User --> System : Retweet Posts
User --> System : Follow Other Users
User --> System : Edit Profile
User --> System : Search for Posts
}
@enduml
```

![Premium User](https://cdn.discordapp.com/attachments/1211743636325408809/1228063063169831064/Premium.drawio.png?ex=662aadda&is=661838da&hm=395f84de432c122338a2a496a34515804c561d8da0158b0df1a501051ff9b8f0&)

```
@startuml
left to right direction

rectangle "Project: SocialNet" {
actor "Premium User" as Premium
boundary "SocialNet System" as System

Premium --> System : Post Tweets
Premium --> System : Comment on Posts
Premium --> System : Like Posts
Premium --> System : Retweet Posts
Premium --> System : Follow Other Users
Premium --> System : Edit Profile
Premium --> System : Search for Posts
Premium --> System : Access Trends
}
@enduml
```

![Admin User](https://cdn.discordapp.com/attachments/1211743636325408809/1228063063454908516/Admin.drawio.png?ex=662aadda&is=661838da&hm=8c8c05b6a873d1d3fc0616aefb82457c84d6d968a5b9bfbd5a739703421caef1&)

```
@startuml
left to right direction

rectangle "Project: SocialNet" {
actor "Admin User" as Admin
boundary "SocialNet System" as System


' Funcionalidades adicionais para Admin User
Admin --> System : Post Tweets
Admin --> System : Comment on Posts
Admin --> System : Like Posts
Admin --> System : Retweet Posts
Admin --> System : Follow Other Users
Admin --> System : Edit Profile
Admin --> System : Search for Posts
Admin --> System : Access Trends
Admin --> System : Access Control Panel
System --> Admin : Ban Users
System --> Admin : Delete Tweets
}
@enduml
```

![Post](https://cdn.discordapp.com/attachments/1211743636325408809/1228063063794516049/Tweet.drawio.png?ex=662aadda&is=661838da&hm=33034dcb2529a03d922c2b26a4679df90b3c22907bfc5b4b1c8ba00b339bf67f&)

```
@startuml
left to right direction
actor Author
actor Follower

rectangle "Project: SocialNet" {
  usecase "Post a Tweet" as Post
  usecase "Attach Image\nto Tweet" as Attach
  usecase "Retweet" as Retweet
  usecase "Like a Tweet" as Like

  Author --> Post : Posts
  Post ..> Attach : <<extend>>

  Follower --> Retweet : Can retweet
  Follower --> Like : Can like

}

@enduml
```

![Redirect to a ban page](https://cdn.discordapp.com/attachments/1211743636325408809/1230216138546217081/caseDiagramBannedUser.drawio.png?ex=6632830f&is=66200e0f&hm=5b972e1132920bcc71a5563dc3ebef1baf6893652b008124fbe3e4d3fc90f511&)

```
@startuml
left to right direction
rectangle "Project: SocialNet" {

actor User
boundary "SocialNet System" as System

User --> System : Attempt Login
System --> (Verify Ban Status)
(Verify Ban Status) .> (Redirect to Ban Page) : <<extends>>
}
@enduml
```