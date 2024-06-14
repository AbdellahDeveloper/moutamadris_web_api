from fastapi import FastAPI, Response, status
from moutamadris_api import moutamadris, IncorrectCredentialsError, HEADERS, Language, get_enum_by_value, AdditionalInfos_Providers, AdditionalInfos_Types
import uvicorn

app = FastAPI()

def SwitchLanguage(lang: str, moutamadris_instance: moutamadris):
    """
    Change the language preference of the Moutamadris instance.
    
    Args:
    - lang (str) -> (Optional): The language code ('fr' for French, 'ar' for Arabic).
    - moutamadris_instance (moutamadris): The Moutamadris instance to update.
    """
    match lang:
        case 'fr':
            moutamadris_instance.ChangeMoutamadrisLanguage(language=Language.FRENCH)
        case 'ar':
            moutamadris_instance.ChangeMoutamadrisLanguage(language=Language.ARABIC)

def getMoutamadris(idToken: str) -> moutamadris:
    """
    Initialize and authenticate a Moutamadris instance using an ID token.
    
    Args:
    - idToken (str) -> (Optional): The ID token for authentication.
    
    Returns:
    - moutamadris: The authenticated Moutamadris instance, or None if authentication fails.
    """
    if not idToken.strip():
        return None
    
    moutamadris_instance = moutamadris(idToken=idToken)
    moutamadris_instance.session.get('https://massarservice.men.gov.ma/moutamadris/Account', headers=HEADERS)
    
    if 'idToken' in moutamadris_instance.session.cookies.get_dict():
        return moutamadris_instance
    else: 
        return None

@app.get("/api/get_id_token")
def GetIDToken(email: str, password: str, response: Response):
    """
    Retrieve the ID token for a Moutamadris account using email and password.
    
    Args:
    - email (str): The email address of the Moutamadris account.
    - password (str): The password of the Moutamadris account.
    
    Returns:
    - dict: The ID token or an error message.
    """
    if not email.strip() or not password.strip():
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'status': 400, 'message': 'Email or password is empty'}
    try:
        return moutamadris(email, password).GetIdToken()
    except IncorrectCredentialsError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'status': 400, 'message': 'Email or password is incorrect'}

@app.get("/api/get_account_infos")
def GetAccountInfos(response: Response, idToken: str, lang: str = ''):
    """
    Retrieve account information for the logged-in user.
    
    Args:
    
    - idToken (str) -> (Optional): The ID token for authentication.
    - lang (str) -> (Optional): The preferred language for the response ('fr' or 'ar').
    
    Returns:
    - dict: The account informations or an error message.
    """
    moutamadris_instance = getMoutamadris(idToken=idToken)
    if not moutamadris_instance:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'status': 400, 'message': 'ID token is incorrect'}
    SwitchLanguage(lang, moutamadris_instance)
    response.status_code = status.HTTP_200_OK
    return moutamadris_instance.GetAccountInfos()

@app.get("/api/get_educational_periods")
def GetEducationalPeriods(response: Response, idToken: str, lang: str = ''):
    """
    Retrieve educational periods for the logged-in user.
    
    Args:
    
    - idToken (str) -> (Optional): The ID token for authentication.
    - lang (str) -> (Optional): The preferred language for the response ('fr' or 'ar').
    
    Returns:
    - dict: The educational periods or an error message.
    """
    moutamadris_instance = getMoutamadris(idToken=idToken)
    if not moutamadris_instance:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'status': 400, 'message': 'ID token is incorrect'}
    SwitchLanguage(lang, moutamadris_instance)
    response.status_code = status.HTTP_200_OK
    return moutamadris_instance.GetEducationalPeriod()

@app.get("/api/get_all_marks")
def GetAllMarks(response: Response, study_year_id: str, session_id: str, idToken: str, lang: str = ''):
    """
    Retrieve all marks for a given study year and session.
    
    Args:
    
    - study_year_id (str): The study year ID.
    - session_id (str): The session ID.
    - idToken (str) -> (Optional): The ID token for authentication.
    - lang (str) -> (Optional): The preferred language for the response ('fr' or 'ar').
    
    Returns:
    - dict: The marks or an error message.
    """
    moutamadris_instance = getMoutamadris(idToken=idToken)
    if not moutamadris_instance:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'status': 400, 'message': 'ID token is incorrect'}
    SwitchLanguage(lang, moutamadris_instance)
    response.status_code = status.HTTP_200_OK
    return moutamadris_instance.GetAllMarks(sessionID=session_id, studyYearID=study_year_id)

@app.get("/api/get_academic_journey")
def GetAcedemicJourney(response: Response, idToken: str, lang: str = ''):
    """
    Retrieve the academic journey of the logged-in user.
    
    Args:
    
    - idToken (str) -> (Optional): The ID token for authentication.
    - lang (str) -> (Optional): The preferred language for the response ('fr' or 'ar').
    
    Returns:
    - dict: The academic journey or an error message.
    """
    moutamadris_instance = getMoutamadris(idToken=idToken)
    if not moutamadris_instance:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'status': 400, 'message': 'ID token is incorrect'}
    SwitchLanguage(lang, moutamadris_instance)
    response.status_code = status.HTTP_200_OK
    return moutamadris_instance.GetAcademicJourney()

@app.post("/api/update_additional_infos")
def UpdateAdditionalInfos(response: Response, provider: str, type: str, phone_number: str, idToken: str):
    """
    Update additional information for the logged-in user.
    
    Args:
    
    - provider (str): The telecommunications provider.
    - type (str): The type of phone number owner.
    - phone_number (str): The phone number to update.
    - idToken (str) -> (Optional): The ID token for authentication.
    
    Returns:
    - dict: A success message or an error message.
    """
    moutamadris_instance = getMoutamadris(idToken=idToken)
    response.status_code = status.HTTP_400_BAD_REQUEST
    if not moutamadris_instance:
        return {'status': 400, 'message': 'ID token is incorrect'}
    
    provider_enum = get_enum_by_value(provider, AdditionalInfos_Providers)
    if not provider_enum:
        return {'status': 400, 'message': f'{provider} provider is not available'}
    
    type_enum = get_enum_by_value(type, AdditionalInfos_Types)
    if not type_enum:
        return {'status': 400, 'message': f'type: {type} is not available'}
    
    if not phone_number:
        return {'status': 400, 'message': 'Phone number field is empty'}
    
    response.status_code = status.HTTP_200_OK
    return moutamadris_instance.UpdateAdditionalInfos(provider=provider_enum, type=type_enum, phoneNumber=phone_number)

@app.post("/api/update_recovery_email")
def UpdateRecoveryEmail(response: Response, email: str, idToken: str):
    """
    Update the recovery email address for the logged-in user.
    
    Args:
    
    - email (str): The new recovery email address.
    - idToken (str) -> (Optional): The ID token for authentication.
    
    Returns:
    - dict: A success message or an error message.
    """
    moutamadris_instance = getMoutamadris(idToken=idToken)
    response.status_code = status.HTTP_400_BAD_REQUEST
    if not moutamadris_instance:
        return {'status': 400, 'message': 'ID token is incorrect'}
    
    if not email:
        return {'status': 400, 'message': 'Email field is empty'}
    
    response.status_code = status.HTTP_200_OK
    return moutamadris_instance.UpdateRecoveryEmail(email=email)

@app.post("/api/change_password")
def ChangePassword(response: Response, old_password: str, new_password: str, idToken: str):
    """
    Change the password for the logged-in user.
    
    Args:
    
    - old_password (str): The current password.
    - new_password (str): The new password.
    - idToken (str) -> (Optional): The ID token for authentication.
    
    Returns:
    - dict: A success message or an error message.
    """
    moutamadris_instance = getMoutamadris(idToken=idToken)
    response.status_code = status.HTTP_400_BAD_REQUEST
    if not moutamadris_instance:
        return {'status': 400, 'message': 'ID token is incorrect'}
    
    if not old_password:
        return {'status': 400, 'message': 'Old password field is empty'}
    
    if not new_password:
        return {'status': 400, 'message': 'New password field is empty'}

    response.status_code = status.HTTP_200_OK
    return moutamadris_instance.ChangePassword(old_password=old_password, new_password=new_password)

@app.post("/api/reset_mfa")
def ResetMFA(response: Response, idToken: str):
    """
    Reset multi-factor authentication (MFA) settings for the logged-in user.
    
    Args:
    
    - idToken (str) -> (Optional): The ID token for authentication.
    
    Returns:
    - dict: A success message or an error message.
    """
    moutamadris_instance = getMoutamadris(idToken=idToken)
    response.status_code = status.HTTP_400_BAD_REQUEST
    if not moutamadris_instance:
        return {'status': 400, 'message': 'ID token is incorrect'}
    
    response.status_code = status.HTTP_200_OK
    return moutamadris_instance.ResetMFA()
