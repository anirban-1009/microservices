# Microservice APIs

- registration
- [register]
    
    ```bash
    curl --location 'http://localhost:8000/users/list/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data-raw '{
        "id": 1,
        "username": "uihduhd",
        "is_admin": false,
        "is_staff": true,
        "is_active": false,
        "date_joined": "2024-02-10T11:22:11.895233Z",
        "first_name": "test",
        "last_name": "name",
        "phone": "9999999999",
        "email": "test2@mail.com",
        "last_login": "2024-02-05T11:22:38.079967Z",
        "all_regions": false,
        "is_deleted": false,
        "password": "somepassword@123",
        "groups": [],
        "user_permissions": []
    }'
    ```
    
- list

```bash
curl --location 'http://localhost:8000/users/' \
--header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
--data ''
```

- detail

```bash
curl --location 'http://localhost:8000/users/detail/2' \
--header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
--data ''
```

- Login & Logout
    - login
    
    ```bash
    curl --location 'http://localhost:8000/users/login/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data-raw '{
        "username": "admin@mail.com",
        "password": "password@122"
    }'
    ```
    
    - logout
    
    ```bash
    curl --location --request POST 'http://localhost:8000/users/logout/' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf'
    ```
    
- Token Management
    - token-list
    
    ```bash
    curl --location 'http://localhost:8000/token/list/' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data ''
    ```
    
    - token-add
    
    ```bash
    curl --location 'http://localhost:8000/token/list/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data-raw '{
        "username": "admin@mail.com",
        "password": "password@122"
    }'
    ```
    
    - token-detail
    
    ```bash
    curl --location 'http://localhost:8000/token/detail/3eb72fa73c85f066ddc9b9846ed891ccc41c413a/' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data ''
    ```
    
    - token-delete
    
    ```bash
    curl --location --request DELETE 'http://localhost:8000/token/detail/21a82f093b4a03b5b54ac34039b0e546880c6e11/' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf'
    ```
    
    - token-update
    
    ```bash
    curl --location --request PUT 'http://localhost:8000/token/detail/ddceddb3914247898c18537e5901ba8e24177a7f/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data-raw '{
        "username": "admin@mail.com",
        "password": "password@122"
    }'
    ```
    
- Preference management
    - user-detail
    
    ```bash
    curl --location 'http://localhost:8000/preferences/user-detail/' \
    --header 'Authorization: Bearer 3eb72fa73c85f066ddc9b9846ed891ccc41c413a' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data ''
    ```
    
    - user-detail-update
    
    ```bash
    curl --location --request PATCH 'http://localhost:8000/preferences/user-detail/1/' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer 3eb72fa73c85f066ddc9b9846ed891ccc41c413a' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data '{
        "first_name": "something",
        "gender": "M"
    }'
    ```
    
    - user-communication
    
    ```bash
    curl --location 'http://localhost:8000/preferences/user-communications/' \
    --header 'Authorization: Bearer 3eb72fa73c85f066ddc9b9846ed891ccc41c413a' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data ''
    ```
    
    - user-communication-update
    
    ```bash
    curl --location --request PATCH 'http://localhost:8000/preferences/user-communication/1/' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer 3eb72fa73c85f066ddc9b9846ed891ccc41c413a' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data '{
        "receive_notifications": false
    }'
    ```
    
    - user-permission-detail
    
    ```bash
    curl --location 'http://localhost:8000/preferences/user-permissions/' \
    --header 'Authorization: Bearer 3eb72fa73c85f066ddc9b9846ed891ccc41c413a' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf'
    ```
    
    - user-group-detail
    
    ```bash
    curl --location 'http://localhost:8000/preferences/user-groups/' \
    --header 'Authorization: Bearer 3eb72fa73c85f066ddc9b9846ed891ccc41c413a' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf'
    ```
    
    - 
- Permission
    - permisssion-list
    
    ```bash
    curl --location 'http://localhost:8000/auth/permission-list' \
    --header 'Authorization: Bearer 3eb72fa73c85f066ddc9b9846ed891ccc41c413a' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf'
    ```
    
    - group-list
    
    ```bash
    curl --location --request GET 'http://localhost:8000/auth/groups' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data '{
        "name": "group2"
    }'
    ```
    
    - group-post
    
    ```bash
    curl --location 'http://localhost:8000/auth/groups/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data '{
        "name": "groupie3"
    }'
    ```
    
    - group-detail
    
    ```bash
    curl --location 'http://localhost:8000/auth/group/3/' \
    --header 'Authorization: Bearer 3eb72fa73c85f066ddc9b9846ed891ccc41c413a' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data ''
    ```
    
    - group-detail-update
    
    ```bash
    curl --location --request PATCH 'http://localhost:8000/auth/group/5/' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer 3eb72fa73c85f066ddc9b9846ed891ccc41c413a' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data '{
        "name": "gorp"
    }'
    ```
    
    - group-detail-permisssion-list
    
    ```bash
    curl --location 'http://localhost:8000/auth/permissions/' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf'
    ```
    
    - group-permission-detail
    
    ```bash
    curl --location --request PUT 'http://localhost:8000/auth/group/permissions/3/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: sessionid=ivkel87y0t90isl6nynjjjauc7akf0kf' \
    --data '{
        "permissions": [
            "change_permission"
        ]
    }'
    ```

# MindMap
![Mind Map](MindMap.png)