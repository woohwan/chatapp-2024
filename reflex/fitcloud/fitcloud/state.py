import reflex as rx
import requests

class SessionState(rx.State):
    accountId: str
    token: str

class FormState(rx.State):
    """The app state."""
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        print(form_data)
        # 인증
        success, session_id = authenticate(form_data["userId"], form_data["password"], form_data["mfaCode"])
        if success:
            SessionState.set_token = session_id
            SessionState.set_accountId = "532805286864"
            print(session_id)
        else:
            raise Exception("인증 에러")


def authenticate(username, password, mfa_code):
    # Prepare data for authentication
    data = {"userId": username, "password": password, "mfaCode": mfa_code}

    # Make a POST login request to the Dev FitCloud
    response = requests.post("https://aws-dev.fitcloud.co.kr/login", json=data)

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()

        # Check if the authentication was successful
        if json_data.get("result", {}).get("validLogin", False):
            # Return the session ID along with the success flag
            return True, json_data.get("session_id", "")
        else:
            # Return failure with an empty session ID
            return False, ""
    else:
        # Return failure with an empty session ID
        return False, ""