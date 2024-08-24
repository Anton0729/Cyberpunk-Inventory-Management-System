import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi_pagination import add_pagination, paginate, Page
from sqlalchemy.orm import Session

from .models import Base, Item
from .models import User as UserModel
from .database import engine, get_db
from .schemas import ItemBase, ItemCreate, ItemUpdate, User
from auth.routes import router as auth_router
from auth.dependencies import get_current_user

app = FastAPI(title="Cyberpunk Inventory Management System")

# Auth routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])

Base.metadata.create_all(bind=engine)



@app.get("/items", response_model=Page[ItemBase], status_code=200)
def read_items(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    items = db.query(Item).all()
    return paginate(items)


@app.get("/items/{item_id}", response_model=ItemBase, status_code=200)
def read_item(item_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/item", response_model=ItemBase, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    try:
        existing_item = db.query(Item).filter(Item.name == item.name).first()
        if existing_item:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="An item with this name already exists.")
        # new_item = Item(**item.dict())
        new_item = Item(**item.model_dump())
        db.add(new_item)
        db.commit()
        return new_item

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.put("/item/{item_id}", response_model=ItemBase, status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_item = db.query(Item).filter(Item.id == item_id).one_or_none()
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Item not found")

    for var, value in vars(item).items():
        setattr(db_item, var, value) if value else None

    try:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_item


@app.delete("/item/{item_id}", response_model=ItemBase, status_code=status.HTTP_200_OK)
def delete_item(item_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return item



add_pagination(app)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8081, reload=True)
