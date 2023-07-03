# pioreactor-basic-auth-for-ui


This adds basic auth to access your Pioreactor UI.

> **Warning**
> The web server is still HTTP. Malicious users _on your network_ can read any data going back and forth, including an encoded version of the user/name password.


## Installation

1. On your leader Pioreactor, run
```
pio install-plugin pioreactor-basic-auth-for-ui
```
2. Next, execute:
```
pio run change_ui_credentials <ui_username> <ui_password>
```
4. Refresh the UI and you should be greeted with a pop up.
5. Add the API key from `pio run change_ui_credentials` to your config.ini
6. Finally, you should restart the leader now, or later.
