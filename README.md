
# Unofficial Moutamadris Rest API 💻
![Static Badge](https://img.shields.io/badge/Awesome%20Rest%20API-8A2BE2?logo=windows&logoColor=white)

## Host Your API
You can host your own moutamadris_rest_api for FREE in **RENDER** :
>[![Render](https://img.shields.io/badge/Render%20Hosting-ffffff?style=for-the-badge&logo=render&logoColor=black)](https://docs.render.com/deploy-fastapi)

## API Reference
Replace **{MOUTAMADRIS_WEB_API_URL}** with **Url of the hosted moutamadris api**

### Get ID Token
```
POST http://{MOUTAMADRIS_WEB_API_URL}/api/get_id_token
```
| Parameter  | Type     | Description                  |
| :--------- | :------- | :--------------------------- |
| `email`    | `string` | **Required**. User email     |
| `password` | `string` | **Required**. User password  |

#### Response:
![App Screenshot](https://github.com/AbdellahDeveloper/BypassAntivirus/blob/main/images_moutamadris_api/1.png?raw=true)

### Get Account Infos
```
GET http://{MOUTAMADRIS_WEB_API_URL}/api/get_account_infos
```
| Parameter | Type     | Description              |
| :-------- | :------- | :----------------------- |
| `idToken` | `string` | **Required**. ID token   |
| `lang`    | `string` | Optional. Language code  |

#### Response:
![App Screenshot](https://github.com/AbdellahDeveloper/BypassAntivirus/blob/main/images_moutamadris_api/2.png?raw=true)

### Get Educational Periods
```
GET http://{MOUTAMADRIS_WEB_API_URL}/api/get_educational_periods
```
| Parameter | Type     | Description              |
| :-------- | :------- | :----------------------- |
| `idToken` | `string` | **Required**. ID token   |
| `lang`    | `string` | Optional. Language code  |

#### Response:
![App Screenshot](https://github.com/AbdellahDeveloper/BypassAntivirus/blob/main/images_moutamadris_api/3.png?raw=true)

### Get All Marks
```
GET http://{MOUTAMADRIS_WEB_API_URL}/api/get_all_marks
```
| Parameter       | Type     | Description                      |
| :-------------- | :------- | :------------------------------ |
| `idToken` | `string` | **Required**. ID token          |
| `study_uear_id`  | `string` | **Required**. Study year ID   |
| `session_id` | `string` | **Required**. Session ID        |
| `lang`    | `string` | Optional. Language code  |

#### Response:
![App Screenshot](https://github.com/AbdellahDeveloper/BypassAntivirus/blob/main/images_moutamadris_api/4.png?raw=true)

### Get Academic Journey
```
GET http://{MOUTAMADRIS_WEB_API_URL}/api/get_academic_journey
```
| Parameter | Type     | Description              |
| :-------- | :------- | :----------------------- |
| `idToken` | `string` | **Required**. ID token    |
| `lang`    | `string` | Optional. Language code  |

#### Response:
![App Screenshot](https://github.com/AbdellahDeveloper/BypassAntivirus/blob/main/images_moutamadris_api/5.png?raw=true)

### Update Additional Infos
```
POST http://{MOUTAMADRIS_WEB_API_URL}/api/update_additional_infos
```
| Parameter           | Type     | Description                                   |
| :------------------------------------------------------------ | :------- | :----------------------------------------- |
| `idToken`          | `string` | **Required**. ID token                                   |
| `provider`        | `string` | **Required**. Provider of additional info                 |
| `type`           | `string` | **Required**. Type of additional info                           |
| `phone_number`      | `string` | **Required**. New phone number                           |

#### Response:
![App Screenshot](https://github.com/AbdellahDeveloper/BypassAntivirus/blob/main/images_moutamadris_api/6.png?raw=true)

### Update Recovery Email
```
POST http://{MOUTAMADRIS_WEB_API_URL}/api/update_recovery_email
```
| Parameter | Type    | Description              |
| :-------- | :------- | :---------------------------------- |
| `idToken` | `string` | **Required**. ID token                            |
| `email`    | `string` | **Required**. New email                           |

#### Response:
![App Screenshot](https://github.com/AbdellahDeveloper/BypassAntivirus/blob/main/images_moutamadris_api/6.png?raw=true)

### Change Password
```curl
POST http://{MOUTAMADRIS_WEB_API_URL}/api/change_password
```
| Parameter       | Type     | Description              |
| :---------------- | :------- | :--------------------------------- |
| `idToken`       | `string` | **Required**. ID token                        |
| `old_password` | `string` | **Required**. Old password                      |
| `new_password` | `string` | **Required**. New password                      |


## Reset MFA
```
POST http://{MOUTAMADRIS_WEB_API_URL}/api/reset_mfa
```
| Parameter | Type     | Description              |
| :-------- | :------- | :------------------------ |
| `idToken` | `string` | **Required**. ID token   |

#### Response:
![App Screenshot](https://github.com/AbdellahDeveloper/BypassAntivirus/blob/main/images_moutamadris_api/6.png?raw=true)


## 🛠 Built With
![Static Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

![Static Badge](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)


# Hi, I'm Abdellah Elidrissi! 👋

Passionate developer and student with a diverse skill set that spans across various domains. From Web Development utilizing technologies like Asp.net Core MVC, Node.js, HTML, CSS, JavaScript, and React, to Android Development with expertise in Java and Flutter, I've ventured into Desktop Development using WinForms in C# and even dived into the world of Games Development, specializing in Unreal Engine. Additionally, I have a knack for 3D Design, leveraging tools like Blender to bring creative ideas to life.

I embarked on this journey in the world of programming at the age of 13, and my trajectory has been a fascinating evolution, starting from desktop applications to conquering the realms of Android, Games, and finally Web Development. Currently, I'm studying at ENSA MARRAKECH.

With a genuine love for programming, I find joy in turning concepts into functional and aesthetically pleasing applications. I'm excited to see what challenges and innovations lie ahead in this ever-evolving field.
