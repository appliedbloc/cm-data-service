from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "YOU NEED A ENV FILE"
    admin_email: str = "YOU NEED A ENV FILE"
    aws_default_region: str = 'YOU NEED A ENV FILE'
    aws_cognito_domain: str = 'YOU NEED A ENV FILE'
    aws_cognito_user_pool_id: str = 'YOU NEED A ENV FILE'
    aws_cognito_user_pool_client_id: str = 'YOU NEED A ENV FILE'
    aws_cognito_user_pool_client_secret: str = 'YOU NEED A ENV FILE'
    aws_cognito_redirect_url: str = 'YOU NEED A ENV FILE'

    class Config:
        env_file = "dev.env"
