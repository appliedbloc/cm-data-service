from fastapi import Depends, FastAPI
from starlette.middleware.cors import CORSMiddleware
import models
from database import SessionLocal, engine
from routers import organizations, users, campaigns, needs, donations

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    organizations.router,
    prefix="/organizations",
    tags=["organizations"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    campaigns.router,
    prefix="/campaigns",
    tags=["campaigns"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    needs.router,
    prefix="/needs",
    tags=["needs"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    donations.router,
    prefix="/donations",
    tags=["donations"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)