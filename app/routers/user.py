from app import oauth2
from .. import schemas, models, utils
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException, APIRouter
from ..database import get_db


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Userdetails)
def register(user: schemas.RegisterUser, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email).first()
    useername_taken = db.query(models.User).filter(
        models.User.username == user.username).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="email already exists")
    if useername_taken:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="username taken. please choose a diiferent username")

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.Userdetails)
def get_user(id: int, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} does not exist")
    return user
