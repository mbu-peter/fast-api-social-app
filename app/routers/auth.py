from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=['Users'])


@router.post('/login', response_model=schemas.Token)
def login(credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.username == credentials.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")
    if not utils.verify(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")
    # create a toke, return token
    access_token = oauth2.create_access_token(data={"username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
